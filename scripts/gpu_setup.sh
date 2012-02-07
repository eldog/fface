#!/bin/bash

set -o errexit

LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/cuda/lib64"
CUDA_ROOT="/usr/local/cuda"
THEANO_FLAGS="cuda.root=/usr/local/cuda,device=gpu,floatX=float32"

