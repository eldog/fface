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

sudo pip install Theano

cd /tmp
wget "http://developer.download.nvidia.com/compute/cuda/4_0/toolkit/"\
"cudatoolkit_4.0.17_linux_64_ubuntu10.10.run"
chmod +x cudatoolkit_4.0.17_linux_64_ubuntu10.10.run
sudo ./cudatoolkit_4.0.17_linux_64_ubuntu10.10.run

