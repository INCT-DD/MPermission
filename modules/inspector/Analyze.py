"""
Analyze: collections permissions within source project.
"""

import fnmatch
import os
import subprocess

from pathlib import Path
from importlib import import_module


class Analyze:
    """Analyze object that scrapes project source looking for permissions matches."""

    def __init__(self, apk_path, project_root, package_name, permissions, api):
        """Init method of Analyze."""
        self.apk_path = apk_path
        self.project_root = project_root
        self.package_name = package_name
        self.permissions = permissions
        self.source_files = []
        self.lines = []
        self.ignore = {
            'groups': set(),
            'individual': set()
        }
        self.api = api

        self.dir = Path(os.path.dirname(os.path.realpath(__file__)))
        self.approot = str(self.dir.parent.parent)
        self.exodus_analyzer = self.approot + '/lib/exodus-standalone/exodus_analyze.py'

        self.report_file_name = "reports/source_report_" + self.package_name + ".txt"
        self.tracker_report_file_name = self.approot + "/reports/trackers_" + self.package_name + ".json"

    def search_project_root(self):
        """Looks in the source root for matching files with permissions."""
        print("Analyzing from project root....")

        source_root = self.project_root + "/app/src/"
        matches = []

        if self.api == "":
            self.api = "23"

        try:
            module = import_module("modules.permissions.PermissionsAPI" + self.api)
        except ImportError:
            print("Could not find \'PermissionsAPI" + self.api + ".py\' for your specified API level")
            print("Attempting to run against the default API level 23")
            self.api = "23"
            module = import_module("modules.permissions.PermissionsAPI" + self.api)

        permissions_api = getattr(module, "PermissionsAPI" + self.api)
        instance = permissions_api()

        # Add any ignored group permissions to the set of individual perms
        # dangerous_permissions = Permissions().dangerous_permissions

        dangerous_permissions = instance.dangerous_permissions
        if len(self.ignore['groups']) > 0:
            for group in self.ignore['groups']:
                # Get the specific list of permission group and permissions
                ignored_permissions = dangerous_permissions[group]
                for permission in ignored_permissions:
                    dangerous_permission = "android.permission." + permission
                    self.ignore['individual'].add(dangerous_permission)

        # Search for matching java files
        for root, dirnames, filenames in os.walk(source_root):
            for filename in fnmatch.filter(filenames, "*.java"):
                matches.append(os.path.join(root, filename))
        for file in matches:
            current_file = ""
            with open(file) as java_file:
                for index, line in enumerate(java_file):
                    # Search for Permissions
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
        print("Source report printed! You can find it in the ./reports/ folder.")
        return self.report_file_name

    def search_trackers(self):
        print('Running tracker analyzer...')
        try:
            subprocess.run(['python', self.exodus_analyzer, '-j', '-o', self.tracker_report_file_name, self.apk_path])
        except Exception:
            print('Tracker analysis failed. Please check your permissions.')
            return False
        else:
            print('Trackers report printed! You can find it in the ./reports/ folder.')
            return self.tracker_report_file_name
