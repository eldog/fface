#!/bin/bash

################################################################################
#
#   android-install.sh
#   
#   Installs the android development environment
#
#   The absence of eclipse is absolutely deliberate.
#
################################################################################

set -o errexit
set -o nounset

sudo apt-get install \
    git \
    curl

readonly DOWNLOAD_DIR='/tmp'

################################################################################
#
#   Android SDK r16
#
################################################################################

echo 'fetching android sdk...'
readonly ANDROID_SDK_TAR="${DOWNLOAD_DIR}/android-sdk_r16-linux.tgz"
curl --location 'http://dl.google.com/android/android-sdk_r16-linux.tgz' \
    --output "${ANDROID_SDK_TAR}"
tar -C "${HOME}" -xzf "${ANDROID_SDK_TAR}"

################################################################################
#
#   Android NDK r7b
#
################################################################################

echo 'fetching android ndk...'
readonly ANDROID_NDK_TAR="${DOWNLOAD_DIR}/android-ndk-r7b-linux-x86.tar.bz2"
curl --location \
     'http://dl.google.com/android/ndk/android-ndk-r7b-linux-x86.tar.bz2' \
     --output "${ANDROID_NDK_TAR}"
tar -C "${HOME}" -xjf "${ANDROID_NDK_TAR}"

################################################################################
#
#   OpenCV 2.3.1 Android
#
################################################################################

echo 'fetching opencv android...'
readonly OPENCV_ANDROID='OpenCV-2.3.1-android-bin.tar.bz2'
readonly OPENCV_ANDROID_TAR="${DOWNLOAD_DIR}/${OPENCV_ANDROID}"
open_cv_url='http://sourceforge.net/projects/opencvlibrary/files'
open_cv_url="${open_cv_url}/opencv-android/2.3.1"
readonly OPENCV_ANDROID_URL="${open_cv_url}/${OPENCV_ANDROID}"
unset open_cv_url
curl --location "${OPENCV_ANDROID_URL}" --output "${OPENCV_ANDROID_TAR}"
tar -C "${HOME}" -xjf "${OPENCV_ANDROID_TAR}"

################################################################################
#
#   logdog
#
################################################################################

echo 'fetching logdog...'
readonly LOG_DOG_DIR="${HOME}/logdog"
if [[ ! -d "${LOG_DOG_DIR}" ]]; then
    git clone git://github.com/dj-foxxy/logdog.git "${LOG_DOG_DIR}"
fi
readonly ANDROID_SDK_TOOL_DIR="${HOME}/android-sdk-linux/tools"
ln --force "${LOG_DOG_DIR}/src/logdog.py" "${ANDROID_SDK_TOOL_DIR}/logdog"

################################################################################
#
#   Start the SDK update
#
################################################################################

echo 'starting sdk update tool'
"${ANDROID_SDK_TOOL_DIR}"/android update sdk \
    --no-ui \
    --filter '1,2,3,4,5,6,7,8,9,10,11'

