#!/bin/bash

set -o errexit
set -o nounset

~/android-ndk-r7b/ndk-build
ant clean
ant uninstall
ant debug install
~/android-sdk-linux/platform-tools/adb shell am start -n uk.me.eldog.fface/.FaceCaptureActivity
~/android-sdk-linux/tools/logdog
