import setuptools #enables develop
import os
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
from edgeml_pytorch.utils import findCUDA

if findCUDA() is not None:
    setuptools.setup(
        name='fastgrnn_cuda',
        ext_modules=[
            CUDAExtension('fastgrnn_cuda', [
                'edgeml_pytorch/cuda/fastgrnn_cuda.cpp',
                'edgeml_pytorch/cuda/fastgrnn_cuda_kernel.cu',
            ]),
        ],
        cmdclass={
            'build_ext': BuildExtension
        }
    )
