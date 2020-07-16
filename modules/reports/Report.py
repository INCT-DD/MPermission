"""
Report: Writes an analysis text file of the various over/under privileged
        permissions found during analysis.
"""
from modules.permissions.Permissions import Permissions
import json
import pandas
import re


class Report:
    """Report object to be printed."""

    def __init__(self, package_name, permissions, third_party_permissions):
        self.columns = ['from_manifest', 'third_party', 'dangerous_groups', 'dangerous_permission',
                        'requested_dangerous', 'under_requested_dangerous', 'over_requested_dangerous',
                        'application_libraries', 'trackers']
        self.data = dict(from_manifest=[], third_party=[], dangerous_groups=[], requested_dangerous=[],
                         under_requested_dangerous=[], over_requested_dangerous=[], application_libraries=[],
                         trackers=[])
        self.package_name = package_name
        self.permissions = permissions
        self.third_party_permissions = third_party_permissions
        self.report_filename = "reports/report_" + package_name + ".txt"
        self.analysis_report_filename = "reports/analysis_" + package_name
        self.resume_report_filename = "reports/" + package_name

    def print_analysis(self, requested_permissions, source_file, tracker_report):
        """Diffs the requested permissions against occurrences in source."""

        # Get permissions object
        permission = Permissions()

        permissions = set()
        for perm in requested_permissions:
            permissions.add(perm.rsplit('.', 1)[-1])

        requested_permissions_dict = permission.get_dangerous_permission_group(permissions)
        requested_permissions = set()
        for requested_perm_group in requested_permissions_dict.values():
            for requested in requested_perm_group:
                requested_permissions.add(requested)

        over_requested = requested_permissions_dict.copy()

        normal_permissions = set()
        dangerous_permissions = set()
        groups_to_remove = set()
        not_requested_files = set()
        not_requested_source_lines = set()

        # Reading source report for findings.
        with open(source_file) as source:
            for line in source:
                if "android.permission." in line:

                    # Skip line if it's commented
                    if line.lstrip().startswith("//"):
                        continue

                    # Check each line for normal permissions
                    for normal in permission.normal_permissions:
                        if normal in line:
                            normal_permissions.add(normal + ": " + line)

                    # Check each line to see if dangerous permission may exist
                    for dangerous_list in permission.dangerous_permissions.values():
                        for dangerous in dangerous_list:
                            if dangerous in line:
                                dangerous_permissions.add(dangerous + ": " + line)

                                # Possible not requested in Manifest
                                if dangerous not in requested_permissions:
                                    not_requested_files.add(source_file)
                                    not_requested_source_lines.add(line)
                                else:
                                    # Check for the group
                                    for permissions in requested_permissions_dict.values():
                                        if dangerous in permissions:
                                            for group, permissions in over_requested.items():
                                                if dangerous in permissions:
                                                    groups_to_remove.add(group)

            # Now remove those groups from requested groups
            for group in groups_to_remove:
                over_requested.pop(group)

        with open(self.analysis_report_filename + '.txt', "w+") as analysis:
            print(" Analysis Report ".center(50, '-'), file=analysis)
            print("{}".format("Package: " + self.package_name), file=analysis)
            print(file=analysis)

            print(" Permissions from Manifest ".center(50, '-'), file=analysis)
            for index, non_system_permission in enumerate(self.permissions):
                self.data['from_manifest'].append(non_system_permission)
                print('{:>4} {}'.format(index, non_system_permission), file=analysis)
            print(file=analysis)

            print(" Third Party Permissions ".center(50, '-'), file=analysis)
            for index, permission in enumerate(self.third_party_permissions):
                self.data['third_party'].append(permission)
                print('{:>4} {}'.format(index, permission), file=analysis)
            print(file=analysis)

            print(" Requested Dangerous Permissions ".center(50, '-'), file=analysis)
            for group, permissions in requested_permissions_dict.items():
                for permission in permissions:
                    self.data['dangerous_groups'].append(group)
                    self.data['requested_dangerous'].append(permission)
                    print(group + ": " + permission, file=analysis)
            print(file=analysis)

            print(" Dangerous Permissions ".center(50, '-'), file=analysis)
            print("{}".format("Total found: " + str(len(dangerous_permissions))), file=analysis)
            print(file=analysis)
            for permission in dangerous_permissions:
                print(permission, file=analysis)
            print(file=analysis)

            print(" Unrequested Dangerous (Under) ".center(50, '-'), file=analysis)
            for permission in not_requested_source_lines:
                quoted = re.compile('"[^"]*"')
                for value in quoted.findall(permission):
                    self.data['under_requested_dangerous'].append(value.replace('\"', ''))
                print(permission, file=analysis)
            print(file=analysis)

            print(" Requested Dangerous (Over) ".center(50, '-'), file=analysis)
            for requested in over_requested.values():
                for item in requested:
                    self.data['over_requested_dangerous'].append(item)
                print(requested, file=analysis)
            print(file=analysis)

            with open(self.analysis_report_filename + '.json', 'w') as json_file:
                json.dump(self.data, json_file)

            if tracker_report:
                with open(tracker_report, 'r') as tracker_file:
                    tracker_data = json.load(tracker_file)
                    for library in tracker_data['application']['libraries']:
                        self.data['application_libraries'].append(library)
                    for tracker in tracker_data['trackers']:
                        self.data['trackers'].append(tracker['name'])

            dataframe = pandas.DataFrame({key: pandas.Series(value) for key, value in self.data.items()})
            dataframe.to_csv(self.resume_report_filename + '.csv', encoding='utf-8', index=False)

            # Now print results to analysis file
        print("Analysis printed! You can find it in the ./reports/ folder.")
