#!/bin/bash

################################################################################
#
#   opencv-install.sh
#
#   Installs opencv 2.3
#
################################################################################

set -o errexit
set -o nounset

sudo apt-get build-dep opencv

readonly N_THREADS=$(( `grep processor /proc/cpuinfo | wc -l` * 2 ))
readonly OPENCV_TAR='OpenCV-2.3.1a.tar.bz2'
readonly OPENCV_DOWNLOAD_LOC="/tmp/${OPENCV_TAR}"
readonly OPENCV_DIR="${HOME}/opencv-2.3.1"

opencv_url='http://sourceforge.net/projects/opencvlibrary/files'
opencv_url="${opencv_url}/opencv-unix/2.3.1/${OPENCV_TAR}"
readonly OPENCV_URL="${opencv_url}"
unset opencv_url

echo 'fetching opencv...'
curl --location "${OPENCV_URL}" --output "${OPENCV_DOWNLOAD_LOC}"
if [[ -d "${OPENCV_DIR}" ]]; then
    rm -rf "${OPENCV_DIR}"
fi
mkdir "${OPENCV_DIR}"
tar -C "${OPENCV_DIR}" --strip-components=1 -xjf "${OPENCV_DOWNLOAD_LOC}"

old_dir=`pwd`
cd "${OPENCV_DIR}"
# turned off cuda so ubuntu updates don't mess up the nvidia drivers
cmake \
    -D WITH_TBB=ON \
    -D WITH_CUDA=NO \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D WITH_V4L=ON \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=ON . 
make -j "${N_THREADS}"
sudo make install
cd "${old_dir}"
unset old_dir

