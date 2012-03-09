#!/bin/bash

#
#   android-install.sh
#   ------------------
#   Installs the android NDK
#

set -o errexit
set -o nounset

DOWNLOAD_DIR="/tmp"

#
# Android NDK r7b
#
ANDROID_NDK_TAR="${DOWNLOAD_DIR}/android-ndk-r7b-linux-x86.tar.bz2"
curl --location "http://dl.google.com/android/ndk/android-ndk-r7b-linux-x86.tar.bz2" \
    --output "${ANDROID_NDK_TAR}"
tar -C "${HOME}" -xjf "${ANDROID_NDK_TAR}"
unset ANDROID_NDK_TAR

#
# OpenCV 2.3.1 Android
#
OPENCV_ANDROID_TAR="${DOWNLOAD_DIR}/android-OpenCV-2.3.1-android-bin.tar.bz2"
curl --location "http://sourceforge.net/projects/opencvlibrary/files/opencv-android/2.3.1/OpenCV-2.3.1-android-bin.tar.bz2" \
    --output "${OPENCV_ANDROID_TAR}"
tar -C "${HOME}" -xjf "${OPENCV_ANDROID_TAR}"
unset OPENCV_ANDROID_TAR
unset DOWNLOAD_DIR

