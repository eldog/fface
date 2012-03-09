#!/bin/bash

#
#   setup.sh
#   --------
#   Installs all the required libraries.
#

set -o errexit
set -o nounset
set -o verbose

#
# Find the root of our repo
#
SCRIPT_SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SCRIPT_SOURCE" ] ; do 
    SCRIPT_SOURCE="$(readlink ${SCRIPT_SOURCE})"; done
REPO_ROOT_DIR="$( cd -P "$( dirname "$SCRIPT_SOURCE" )" && pwd )"

#
# Get our script directory
#
SCRIPT_BASE="scripts"
SCRIPT_DIR="${REPO_ROOT_DIR}/${SCRIPT_BASE}"
unset SCRIPT_BASE

ANDROID_INSTALL_SCRIPT="android-install.sh"
"${SCRIPT_DIR}/${ANDROID_INSTALL_SCRIPT}"


