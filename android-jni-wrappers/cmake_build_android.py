#!/usr/bin/env python3
import os
import sys

project = sys.path[0]

args = {
    'NDK_HOME': 'D:\\Developer\\Android\\Sdk\\ndk',
    'NDK_VERSION': '25.1.8937393',
    'BUILD_DIR': 'build',
    'INSTALL_DIR': 'installed',
    'BUILD_TYPE': 'Release',
    'ANDROID_PLATFORM': '29',
    'ANDROID_STL': 'c++_static',
}
abiFilters = ["arm64-v8a"] # x86 x86_64 armeabi-v7a
ndk_toolchain = os.path.join(args['NDK_HOME'], args['NDK_VERSION'], 'build', 'cmake', 'android.toolchain.cmake')

if 'ANDROID_NDK_HOME' in os.environ:
    ndk_toolchain = os.path.join(os.environ['ANDROID_NDK_HOME'], 'build', 'cmake', 'android.toolchain.cmake')

if 'CMAKE_BUILD_TYPE' in os.environ:
    args['BUILD_TYPE'] = os.environ['CMAKE_BUILD_TYPE']

for abi in abiFilters:
    build_dir = os.path.join(project, args['BUILD_DIR'], abi)
    install_dir = os.path.join(project, args['INSTALL_DIR'], abi)
    cmdline = ' '.join(["cmake", "-G", 'Ninja',
                        "-B", build_dir,
                        "-S", project,
                        "-DCMAKE_CXX_STANDARD=14",
                        "-DCMAKE_BUILD_TYPE=" + args['BUILD_TYPE'],
                        "-DCMAKE_TOOLCHAIN_FILE=" + ndk_toolchain,
                        "-DCMAKE_INSTALL_PREFIX=" + install_dir,
                        "-DANDROID_ABI=" + abi,
                        "-DANDROID_PLATFORM=" + args['ANDROID_PLATFORM'],
                        "-DANDROID_STL=" + args['ANDROID_STL'],
                        "-DCMAKE_EXPORT_COMPILE_COMMANDS=TRUE"])
    print("Cmake configure " + abi + ": \n" + cmdline)
    if not os.system(cmdline):
        cmdline = ' '.join(["cmake", "--build", build_dir, "--config", args['BUILD_TYPE']])
        print("Cmake build " + abi + ": \n" + cmdline)
        if not os.system(cmdline):
            cmdline = ' '.join(["cmake", "-P", os.path.join(build_dir, "cmake_install.cmake")])
            print("Cmake install " + abi + ": \n" + cmdline)
            os.system(cmdline)