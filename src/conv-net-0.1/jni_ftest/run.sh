#!/bin/bash

set -o errexit
set -o nounset

LD_LIBRARY_PATH=. 
export LD_LIBRARY_PATH

java ConvNet ../../cnn/cnn.xml \
     ../../../../data/eccv2010_beauty_data/hotornot_face/female_18_RRRUHEA_face_0.jpg 
