#!/bin/bash

ant debug
cd bin/class
javah uk.me.eldog.fface.FaceCaptureView
mv uk_me_eldog_fface_FaceCaptureView.h ../../jni/
cd ../..
