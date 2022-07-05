import shutil
import stat
import os
import sys
import zipfile
import urllib.request

"""
- Downloads, unzips and makes dex2jar files executable
- Downloads and renames apk-tools
- Downloads and renames jd-core-java decompiler
"""

__DIR = os.path.dirname(os.path.realpath(__file__))
lib_dir = __DIR + "/lib/"

# URLS for libraries

exodus_standalone_url = "https://github.com/Exodus-Privacy/exodus-standalone/archive/refs/tags/v1.3.2.zip"
exodus_standalone_zip_destination = lib_dir + "exodus.zip"
dex2jar_url = "https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip"
dex2jar_zip_destination = lib_dir + "dex2jar.zip"
apktools_url = "https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.6.1.jar"
apktools_destination = lib_dir + "apktool.jar"
jdcore_url = "https://clojars.org/repo/org/clojars/razum2um/jd-core-java/1.2/jd-core-java-1.2.jar"
jdcore_destination = lib_dir + "jd-core-java.jar"


def main():
    if sys.version < '3':
        sys.exit("Please use Python3.")

    create_lib_dir()

    print("Downloading and installing required third-party libraries...")

    # Dex2Jar
    print("Downloading dex2jar...")
    urllib.request.urlretrieve(dex2jar_url, dex2jar_zip_destination)
    files_inzip = extract(dex2jar_zip_destination)

    # Rename dex2jar-version to dex2jar
    os.rename(lib_dir + files_inzip[0], lib_dir + "dex2jar")

    # Delete the zip file and make folder content executable
    os.remove(dex2jar_zip_destination)
    make_dir_executable(lib_dir + "dex2jar")

    # exodus-privacy
    print("Downloading exodus-standalone...")
    urllib.request.urlretrieve(exodus_standalone_url, exodus_standalone_zip_destination)
    files_inzip = extract(exodus_standalone_zip_destination)

    # Rename exodus-standalone-version to exodus-standalone
    os.rename(lib_dir + files_inzip[0], lib_dir + "exodus-standalone")

    # Delete the zip file and make folder content executable
    os.remove(exodus_standalone_zip_destination)
    make_dir_executable(lib_dir + "exodus-standalone")

    # apktools
    print("Downloading apktools...")
    urllib.request.urlretrieve(apktools_url, apktools_destination)

    # jd-core-java
    print("Downloading jd-core-java decompiler...")
    urllib.request.urlretrieve(jdcore_url, jdcore_destination)

    print("Installation complete.")


def extract(path_to_zip, folder=''):
    """
    Extract a zip
    :param path_to_zip:
    :param folder:
    """
    print("Extracting " + path_to_zip)
    with zipfile.ZipFile(path_to_zip, "r") as z:
        z.extractall(lib_dir + folder)
        return z.namelist()


def create_lib_dir():
    """
    Creates a /lib directory in the working directory if it doesn't already exist,
    if dir exists, deletes it and makes a new one.
    """
    if os.path.exists(lib_dir):
        print("Existing lib directory is being deleted...")
        shutil.rmtree(lib_dir)
    print("Creating new lib directory")
    os.makedirs(lib_dir)


def make_dir_executable(directory):
    """
    Makes .sh files in directory variable executable
    :param directory:
    """
    for file in os.listdir(directory):
        if ".sh" or ".py" in file:
            full_path = "/".join([directory, file])
            st = os.stat(full_path)
            os.chmod(full_path, st.st_mode | stat.S_IEXEC)


if __name__ == "__main__":
    main()
