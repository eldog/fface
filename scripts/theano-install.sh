#!/bin/bash

# Installs Theano and cuda toolkit

set nounset
set errexit
set errtrace

sudo apt-get install --assume-yes \
    python-numpy \
    libblas-dev \
    liblapack-dev \
    gfortran \
    python-dev \
    python-pip \
    mercurial

cd /tmp
git clone https://github.com/Theano/Theano.git
cd Theano
python setup.py build
sudo python setup.py install

sudo easy_install nose

cd /tmp
wget "http://uk.download.nvidia.com/XFree86/Linux-x86_64/295.20/NVIDIA-Linux-x86_64-295.20.run"
chmod +x NVIDIA-Linux-x86_64-295.20.run
sudo ./NVIDIA-Linux-x86_64-295.20.run

cd /tmp

wget "http://developer.download.nvidia.com/compute/cuda/4_0/toolkit/"\
"cudatoolkit_4.0.17_linux_64_ubuntu10.10.run"
chmod +x cudatoolkit_4.0.17_linux_64_ubuntu10.10.run
sudo ./cudatoolkit_4.0.17_linux_64_ubuntu10.10.run

