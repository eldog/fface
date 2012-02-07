#!/bin/bash

set -o errexit
set -o nounset

sudo apt-get --assume-yes build-dep python-matplotlib
cd /tmp
git clone git@github.com:matplotlib/matplotlib.git
cd matplotlib
python setup.py build
sudo python setup.py install
