# Android Package (APK) Permission Analysis Tool
A simple tool to statically analyze permission references within decompiled Android apps.

## Context

With the release of Android 6.0 (Android M / API Level 23), users can now grant system and 3rd party permissions at runtime instead of during installation.

This increases an application's susceptibility to over and underprivileging. If a normal (as opposed to dangerous) permission is defined in the app manifest, the system grants that permission automatically -- even if the app is not using the permission directly. However, users can grant all permissions, including dangerous, within a permission group by requiring a single permission. This may result in overprivileging.

## Setup

APKPerm (Android PacKage PERMission) requires Python >=3.5 and the [latest openJDK release](https://openjdk.java.net/install/).

Before your first run, please execute the `setup.py`:

```bash
$ python3 ./setup.py
```

Once it's done, you'll find the appropriate libraries under the `modules/apk-decompiler/lib/` directory.

Bellow you'll find a list with all required third-party libraries:

### Dependencies

- [latest openjdk release](https://openjdk.java.net/install/)
- [apktools](https://ibotpeaches.github.io/Apktool/) (extracts readable xml from the apk file)
- [dex2jar](https://github.com/pxb1988/dex2jar) (converts the *.dex files inside an apk to *.jar files)
- [jd-core-java](https://github.com/nviennot/jd-core-java) (decompiles dex2jar *.jar output files to their *.java classes)

## Usage  

The tool can be run incrementally with the following flags:


```bash
$ python3 apkperm.py -d [--decompile] apk_path              # decompiles APK and moves it to sample_apk/ - This could take a few minutes depending on the size of the APK
$ python3 apkperm.py -a [--analyze]   decompiled_apk_path [android_api_version_number_targeted]   # analyze and prints source report / analysis report against the specified API level number
```

Or in a single pass, like this: 

```bash
$ python3 apkperm.py -f [--fullprocess]   apk_path [android_api_version_number_targeted]   # decompiles APK, analyzes against the specified API level number and prints source report / analysis report, then deletes the decompiled source folder
```


## Troubleshooting

In the event of any issues, please:

1. Make sure you have the latest versions of the required libraries;
2. Make sure the apps being examined are compatible with Android API 23 (Marshmallow) or greater.

In any case, please feel free to fill a bug report if you think something is wrong on our side.

## Acknowledgement

This tool is a partial rewrite of the original [MPermission](https://github.com/MPerm/MPermission) code, written by the following amazing and Free Software loving people:

* Piper Chester
* Daniel Krutz
* Cesar Perez
* Chris Jones

Big Hugs!

## References

1. http://developer.android.com/guide/topics/security/permissions.html#normal-dangerous
2. https://www.wikiwand.com/en/Android_application_package
3. https://git-scm.com/book/en/v2/Git-Tools-Submodules
4. https://github.com/kocsenc/android-scraper/tree/master/tools/apk-decompiler/
5. https://github.com/dan7800/MPermission/wiki
6. http://ibotpeaches.github.io/Apktool/
7. https://sourceforge.net/projects/dex2jar/files/
8. https://github.com/nviennot/jd-core-java
9. http://www.oracle.com/technetwork/pt/java/javase/downloads/index.html
10. https://www.mercurial-scm.org/