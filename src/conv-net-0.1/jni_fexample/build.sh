#!/bin/bash

set -o errexit
set -o nounset

LD_LIBRARY_PATH=. 
export LD_LIBRARY_PATH

javac -verbose ConvNet.java
javah -jni -force -verbose ConvNet

gcc -shared -fPIC -I/usr/lib/jvm/default-java/include\
	    -I/usr/lib/jvm/default-java/include/linux\
	    ConvNet.cpp -o libConvNet.so

java ConvNet ../cnn/cnn.xml ../../../data/eccv2010_beauty_data/hotornot_face/female_18_RRRUHEA_face_0.jpg 
