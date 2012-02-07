#!/bin/bash

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

wget "http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.3.1/OpenCV-2.3.1a.tar.bz2"

tar -xcf OpenCV-2.3.1a.tar.bz2

cd OpenCV-2.3.1a.tar.bz2

cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=OFF -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON .

makea

sudo make install
sudo apt-get install python-setuptools
easy_install BeautifulSoup poster
