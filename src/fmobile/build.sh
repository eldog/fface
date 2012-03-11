#!/bin/bash

set -o errexit
set -o nounset

~/android-ndk-r7b/ndk-build
ant clean
ant uninstall
ant debug install
adb shell am start -n uk.me.eldog.fface/.FaceCaptureActivity
logdog
