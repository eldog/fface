#!/bin/bash

set -o errexit
set -o nounset

sudo apt-get --assume-yes build-dep \
    ffmpeg

readonly N_THREADS=$(( `grep processor /proc/cpuinfo | wc -l` * 2 ))
readonly FFMPEG_INSTALL_DIR='/tmp/ffmpeg'
if [[ -d "${FFMPEG_INSTALL_DIR}" ]]; then
    rm -rf "${FFMPEG_INSTALL_DIR}"
fi

echo 'fetching ffmpeg...'
git clone -b \
    release/0.7 https://github.com/FFmpeg/FFmpeg.git "${FFMPEG_INSTALL_DIR}"

old_dir=`pwd`
cd "${FFMPEG_INSTALL_DIR}"
./configure --enable-pic --enable-shared
make -j "${N_THREADS}"
sudo make install

cd "${old_dir}"
unset old_dir

