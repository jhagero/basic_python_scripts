from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_LGPU_SEPARATE_STORAGE_BIT_NVX: Incomplete
GL_MAX_LGPU_GPUS_NVX: Incomplete

@_f
def glLGPUCopyImageSubDataNVX(sourceGpu, destinationGpuMask, srcName, srcTarget, srcLevel, srcX, srxY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, width, height, depth) -> None: ...
@_f
def glLGPUInterlockNVX() -> None: ...
@_f
def glLGPUNamedBufferSubDataNVX(gpuMask, buffer, offset, size, data) -> None: ...
