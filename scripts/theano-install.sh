#!/bin/bash

################################################################################
#
#   theano-install.sh
#
#   Installs Theano and the cuda toolkit
#
################################################################################

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
    mercurial \
    gcc-4.4

readonly THEANO_DIR='/tmp/theano'
if [[ -d "${THEANO_DIR}" ]]; then
    sudo rm -rf "${THEANO_DIR}"
fi

################################################################################
#
#   Theano
#
################################################################################

echo 'fetching theano...'
git clone https://github.com/Theano/Theano.git "${THEANO_DIR}"
old_dir=`pwd`
cd "${THEANO_DIR}"
python setup.py build
sudo python setup.py install
cd "${old_dir}"
unset old_dir

sudo easy_install nose

################################################################################
#
#   nvidia driver and cuda toolkit
#
################################################################################

readonly NVIDIA_DRIVER_INSTALL_LOC='/tmp/nvidia-driver'
nvidia_driver_url='http://uk.download.nvidia.com/XFree86/Linux-x86_64/295.20'
nvidia_driver_url="${nvidia_driver_url}/NVIDIA-Linux-x86_64-295.20.run"
readonly NVIDIA_DRIVER_URL="${nvidia_driver_url}"
unset nvidia_driver_url
curl --location "${NVIDIA_DRIVER_URL}" --output "${NVIDIA_DRIVER_INSTALL_LOC}"
chmod +x "${NVIDIA_DRIVER_INSTALL_LOC}"
sudo "${NVIDIA_DRIVER_INSTALL_LOC}" -a -q

readonly CUDA_TOOLKIT_INSTALL_LOC='/tmp/cuda-toolkit'
cuda_toolkit_url='http://developer.download.nvidia.com/compute/cuda/4_0'
cuda_toolkit_url="${cuda_toolkit_url}/toolkit"
cuda_toolkit_url="${cuda_toolkit_url}/cudatoolkit_4.0.17_linux_64_"
cuda_toolkit_url="${cuda_toolkit_url}ubuntu10.10.run"
CUDA_TOOLKIT_URL="${cuda_toolkit_url}"
unset cuda_toolkit_url
curl --location "${CUDA_TOOLKIT_URL}" --output "${CUDA_TOOLKIT_INSTALL_LOC}"
chmod +x "${CUDA_TOOLKIT_INSTALL_LOC}"
sudo "${CUDA_TOOLKIT_INSTALL_LOC}"

readonly NVCC_BINDIR="${HOME}/.theano/nvcc-bindir"
if [[ ! -d "${NVCC_BINDIR}" ]]; then
    mkdir "${NVCC_BINDIR}"
fi
ln -s --force `which gcc-4.4` "${NVCC_BINDIR}/gcc" 
ln -s --force `which g++-4.4` "${NVCC_BINDIR}/g++"

cat << EOF > "${HOME}/.theanorc"
[cuda]
root = /usr/local/cuda
[global]
device = gpu
floatX = float32
[nvcc]
compiler_bindir = ${HOME}/.theano/nvcc-bindir

EOF
    
