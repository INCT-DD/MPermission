"""
Analyze: collections permisisons within source project.
"""

import fnmatch
import os

# from Permissions import Permissions


class Analyze:
    """Analyze object that scrapes project source looking for permissions matches."""

    def __init__(self, project_root, package_name, permissions, ignore, api):
        """Init method of Analyze."""
        self.project_root = project_root
        self.package_name = package_name
        self.permissions = permissions
        self.report_file_name = "reports/source_report_" + self.package_name + ".txt"
        self.source_files = []
        self.lines = []
        self.ignore = ignore
        self.api = api

    def search_project_root(self):
        """Looks in the source root for matching files with permissions."""
        print("Analyzing from project root....")

        source_root = self.project_root + "/app/src/"
        matches = []

        if self.api == "":
            self.api = "23"

        try:
            module = __import__("PermissionsAPI" + self.api)
        except ImportError:
            print("Could not find \'PermissionsAPI" + self.api + ".py\' for your specified API level")
            print("Attempting to run against the default API level 23")
            self.api = "23"
            module = __import__("PermissionsAPI23")

        my_class = getattr(module, "PermissionsAPI" + self.api)
        instance = my_class()

        # Add any ignored group permissions to the set of individual perms
        #dangerous_permissions = Permissions().dangerous_permissions
        dangerous_permissions = instance.dangerous_permissions
        if len(self.ignore['groups']) > 0:
            for group in self.ignore['groups']:

                # Get the specific list of permission group and permissions
                ignored_permissions = dangerous_permissions[group]
                for permission in ignored_permissions:
                    dangerous_permission = "android.permission." + permission
                    self.ignore['individual'].add(dangerous_permission)

        # Ignore specific permissions
        if len(self.ignore['individual']) > 0:
            print("Based on config, ignoring the following permissions:")
            for permission in self.ignore['individual']:
                print("Ignoring: " + permission)

        # Search for matching java files
        for root, dirnames, filenames in os.walk(source_root):
            for filename in fnmatch.filter(filenames, "*.java"):
                matches.append(os.path.join(root, filename))
        for file in matches:
            current_file = ""
            with open(file) as java_file:
                for index, line in enumerate(java_file):
                    if "permission" in line:

                        # Ignore the line if it has an ignored permission,
                        # otherwise add the line to the source_lines list
                        for ignored_permission in self.ignore['individual']:
                            if ignored_permission in line:
                                break
                        else:
                            if current_file is not java_file.name:
                                current_file = java_file.name
                                self.lines.append(('{} {:>4}\n'.format("\nFile: ", current_file)))
                                self.source_files.append(current_file)
                            self.lines.append(('{}'.format(line.rstrip())))
        print("Analyzing finished!")

        # Print the source report
        with open(self.report_file_name, "w+") as report:
            print(" Source Report ".center(50, '-'), file=report)
            print("{}".format("Package: " + self.package_name), file=report)
            print(file=report)

            print(" Permissions Found in Files ".center(50, '-'), file=report)
            for line in self.source_files:
                print(line, file=report)
            print(file=report)

            print(" Occurrences in Source ".center(50, '-'), file=report)
            for line in self.lines:
                print(line, file=report)
        print("Source report printed! Location: " + self.report_file_name)
        return self.report_file_name
