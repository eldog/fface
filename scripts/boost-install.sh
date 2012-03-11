#!/bin/bash

################################################################################
#
#   boost-install.sh
#
#   Installs the boost libraries
#
################################################################################

set -o errexit
set -o nounset

sudo apt-get install --assume-yes \
    curl

boost_url='http://sourceforge.net/projects/boost/files'
boost_url="${boost_url}/boost/1.49.0/boost_1_49_0.tar.bz2/download"

readonly BOOST_URL="${boost_url}"
unset boost_url
readonly BOOST_TAR='/tmp/boost.tar.bz2'

curl --location "${BOOST_URL}" --output "${BOOST_TAR}"

readonly BOOST_DIR='/tmp/boost'

if [[ -d "${BOOST_DIR}" ]]; then
    rm -rf "${BOOST_DIR}"
fi

mkdir "${BOOST_DIR}"

tar \
    -C "${BOOST_DIR}" \
    --strip-components=1 \
    -xjf \
    "${BOOST_TAR}"

old_dir=`pwd`
cd "${BOOST_DIR}"
./bootstrap.sh
sudo ./b2 install
cd "${old_dir}"
unset old_dir

