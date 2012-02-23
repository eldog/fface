#!/bin/bash

set -o errexit
set -o nounset

sudo apt-get install --assume-yes \
    build-essential \
    libgtk2.0-dev \
    libjpeg62-dev \
    libtiff4-dev \
    libjasper-dev \
    libopenexr-dev \
    cmake \
    python-dev \
    python-numpy \
    libtbb-dev \
    libeigen2-dev \
    yasm \
    libfaac-dev \
    libopencore-amrnb-dev \
    libopencore-amrwb-dev \
    libtheora-dev \
    libvorbis-dev \
    libxvidcore-dev

cd /tmp

N_THREADS=$(( `grep processor /proc/cpuinfo | wc -l` * 2 ))
OPENCV_TAR="OpenCV-2.3.1a.tar.bz2"
OPENCV_DIR="OpenCV-2.3.1"

if [[ -d "${OPENCV_TAR}" ]]
    then
        rm "${OPENCV_TAR}"
fi

wget "http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.3.1/${OPENCV_TAR}"

tar -xjf "${OPENCV_TAR}"

cd "${OPENCV_DIR}"

# turned off cuda on my laptop
cmake -D WITH_TBB=ON -D WITH_CUDA=NO -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON . 

make -j 4 #"${N_THREADS}"

sudo make install
sudo apt-get install python-setuptools
sudo easy_install BeautifulSoup poster
