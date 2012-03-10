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
script_source="${BASH_SOURCE[0]}"
while [ -h "$script_source" ] ; do 
    script_source="$(readlink ${script_source})"; done
readonly REPO_ROOT_DIR="$( cd -P "$( dirname "$script_source" )" && pwd )"
unset script_source

#
#   Get our script directory
#
readonly SCRIPT_DIR="${REPO_ROOT_DIR}/scripts"

#
#   install the android stuff
#
readonly ANDROID_INSTALL_SCRIPT="android-install.sh"
"${SCRIPT_DIR}/${ANDROID_INSTALL_SCRIPT}"

#
#   install the theano stuff
#
#THEANO_INSTALL_SCRIPT="theano-install.sh"
#"${SCRIPT_DIR}/${THEANO_INSTALL_SCRIPT}"
#unset THEANO_INSTALL_SCRIPT

