#!/usr/bin/env python3

__author__ = 'piper'

import glob
import sys
import subprocess
import Harvest

def read_manifest(project_root):
    """Analyze manifest to see what permissions to request."""
    root_dir = project_root[:project_root.find('/') + 1]
    manifests = permissions = []
    for file in glob.glob(root_dir + "/**/AndroidManifest.xml", recursive=True):
        manifests.append(file)

    # Collect all permissions from each manifest
    line_number = 1
    with open(manifests[0]) as manifest:
        for line in manifest:
            line_number += 1
            if 'permission' in line:
                permission_line = line[(line.find('permission.') + len('permission.')):]
                permission = permission_line[:permission_line.find('"')]
                if permission not in permissions:
                    permissions.append(permission_line[:permission_line.find('"')])

    # Write add manifest to report
    line_number = 1
    with open("report.txt", "w") as report:
        print('--- Permissions from Manifest ---', file=report)
        for permission in permissions:
            print('{:>4} {}'.format(line_number, permission.rstrip()), file=report)
            line_number += 1
        print('-' * 20, file=report)


def decompile(decomp_path, apk_path, dest_path="./sample_apks/"):
    """
    Only decompile the provided APK. The decompiled APK will be
    left within the same directory.
    """
    subprocess.call(["./" + decomp_path, apk_path])
    subprocess.call(["mv", "android-scraper/tools/apk-decompiler/uncompressed", dest_path])


def read_config(config_file):
    """Takes a configuration file to decide which permissions to analyze."""
    line_number = 1
    with open(config_file) as config:
        for line in config:
            print('{:>4} {}'.format(line_number, line.rstrip()))
            line_number += 1

def main():
    """Primary driver of MPermission. """
    arguments = sys.argv
    source_path = ""
    if len(arguments) < 3:
        print("Error: missing arguments. ")
        exit(1)
    elif len(arguments) >= 3 and len(arguments) < 5:
        source_path = arguments[1]
        read_manifest(source_path)
        if '-d' in arguments:
            Harvest.search_project_root(source_path)


if __name__ == "__main__":
    main()
