# APK Decompiler Guide
This is a wholesome all in one solution to decompress an APK file to
readable xml and decompiled code.

## First time setup
Run the Python3 `setupDependencies.py` script
```
./setupDependencies.py
```
This will get the appropriate libraries under the `lib/` directory.

## Usage to decompress APK's

```
./apk_decompiler.sh path/to/app.apk
```

The result will be found in the script location under a `app.apk.uncompressed` directory.

## Implementation details
### Dependencies
- [latest openjdk release](https://openjdk.java.net/install/)
- [apktools](https://ibotpeaches.github.io/Apktool/)
- [dex2jar](https://github.com/pxb1988/dex2jar)
- [jd-core-java](https://github.com/nviennot/jd-core-java)


1. `apktools` - Extracts readable xml from the apk file;

2. `dex2jar` - Converts the classes.dex files inside an apk to a *.jar files;

3. `jd-core-java` - Decompiles dex2jar *.jar output files to their *.java classes.

To download all of the dependencies you can use the setupDependencies python script. 