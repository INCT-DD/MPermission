#!/usr/bin/env python3

from pathlib import Path
import subprocess
import os
import shutil
import zipfile

# Important paths

selfdir = Path(os.path.dirname(os.path.realpath(__file__)))
approot = str(selfdir.parent.parent)
libdir = approot + '/lib/'
extract_to = '/tmp/'
destination = approot + '/apk_sources/'


class Decompile:
    def run(self, apk_path):

        # checks if the required libraries exist

        print('Searching for required libraries...')

        libs = self.checklibs(libdir)

        if not len(libs) == 0:
            for missing in libs:
                print("The following library is missing: " + missing + 'please check your installation.')
                raise ModuleNotFoundError

        print('OK. Continuing...')

        # Prepare the environment for execution

        apk_name = apk_path.rsplit('/', 1)[-1]
        workingdir = extract_to + apk_name + '/'
        workingdir_raw = workingdir + 'raw/'
        workingdir_app = workingdir + 'app/'

        print('Rebuilding the required directory tree directory...')
        print('Deleting old directory tree...')

        if Path(workingdir).exists():
            try:
                shutil.rmtree(workingdir)
            except IOError:
                print("Couldn't remove the old directory. Please, remove it manually and try again.")
                raise IOError

        if Path(destination + apk_name).exists():
            try:
                shutil.rmtree(destination + apk_name)
            except IOError:
                print("Couldn't remove the old directory. Please, remove it manually and try again.")
                raise IOError

        print('OK. Continuing...')
        print('Recreating required directory tree...')

        try:
            os.mkdir(workingdir)
            os.mkdir(workingdir + 'raw/')
            os.mkdir(workingdir + 'app/')
        except IOError:
            print("Couldn't create the required directory tree. Please, check your permissions and try again.")
            raise IOError

        print('OK. Continuing...')
        print('Extracting ' + apk_name + 'contents. Please wait.')

        try:
            self.extract(apk_path, workingdir_raw)
        except IOError:
            print("Couldn't extract the zip file. Please, check your permissions and try again.")
            raise IOError

        print("Extracting readable assets...")

        try:
            self.getassets(apk_path, workingdir_app)
        except IOError:
            print("Couldn't extract the readable assets. Please, check your permissions and try again.")
            raise IOError

        print('Extracting *.dex files...')

        try:
            self.getdex(workingdir, )
        except IOError:
            print("Couldn't extract the *dex files. Please, check your permissions and try again.")
            raise IOError

        print('Extracting source files...')

        try:
            self.getsources(workingdir_raw, workingdir_app)
        except IOError:
            print("Couldn't extract the sources. Please, check your permissions and try again.")
            raise IOError

        print('Moving to destination...')

        try:
            shutil.move(workingdir, destination + apk_name)
        except IOError:
            print("Couldn't move the sources. Please, check your permissions and try again.")
            raise IOError

        print("Done.")

    def checklibs(self, path):
        missing = []

        if not Path(libdir + 'dex2jar').exists():
            missing.append('dex2jar')
        if not Path(libdir + 'apktool.jar').exists():
            missing.append('apktool')
        if not Path(libdir + 'jd-core-java.jar').exists():
            missing.append('jd-core-java')

        return missing

    def extract(self, file, folder):
        with zipfile.ZipFile(file, "r") as apk:
            apk.extractall(folder)

    def getassets(self, file, folder):
        subprocess.run(['java', '-jar', libdir + 'apktool.jar', 'd', file, '-f', '-o', folder])

    def getdex(self, folder):
        subprocess.run([libdir + 'dex2jar/d2j-dex2jar.sh', '-o', folder + 'dex2jar.jar', '--force', folder + 'classes'
                                                                                                             '.dex'])

    def getsources(self, origin, output):
        subprocess.run(['java', '-jar', libdir + 'jd-core-java.jar', origin + 'dex2jar.jar', output + 'src/'])
