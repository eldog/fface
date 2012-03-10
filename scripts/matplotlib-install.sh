#!/bin/bash

################################################################################
#
#   matplotlib-install.sh
#
#   Installs matplotlib
#
################################################################################

set -o errexit
set -o nounset

sudo apt-get --assume-yes build-dep \
    python-matplotlib

readonly MATPLOTLIB_INSTALL_DIR='/tmp/matplotlib'

if [[ -d "${MATPLOTLIB_INSTALL_DIR}" ]]; then
    rm -rf "${MATPLOTLIB_INSTALL_DIR}"
fi

echo "fetching matplotlib..."
git clone git://github.com/matplotlib/matplotlib.git "${MATPLOTLIB_INSTALL_DIR}"
old_dir=`pwd`
cd "${MATPLOTLIB_INSTALL_DIR}"
python setup.py build
sudo python setup.py install
cd "${old_dir}"
unset old_dir

