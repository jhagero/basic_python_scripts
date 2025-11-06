from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_GPU_CLOCK_AMD: Incomplete
GLX_GPU_FASTEST_TARGET_GPUS_AMD: Incomplete
GLX_GPU_NUM_PIPES_AMD: Incomplete
GLX_GPU_NUM_RB_AMD: Incomplete
GLX_GPU_NUM_SIMD_AMD: Incomplete
GLX_GPU_NUM_SPI_AMD: Incomplete
GLX_GPU_OPENGL_VERSION_STRING_AMD: Incomplete
GLX_GPU_RAM_AMD: Incomplete
GLX_GPU_RENDERER_STRING_AMD: Incomplete
GLX_GPU_VENDOR_AMD: Incomplete

@_f
def glXBlitContextFramebufferAMD(dstCtx, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
@_f
def glXCreateAssociatedContextAMD(id, share_list) -> None: ...
@_f
def glXCreateAssociatedContextAttribsAMD(id, share_context, attribList) -> None: ...
@_f
def glXDeleteAssociatedContextAMD(ctx) -> None: ...
@_f
def glXGetContextGPUIDAMD(ctx) -> None: ...
@_f
def glXGetCurrentAssociatedContextAMD() -> None: ...
@_f
def glXGetGPUIDsAMD(maxCount, ids) -> None: ...
@_f
def glXGetGPUInfoAMD(id, property, dataType, size, data) -> None: ...
@_f
def glXMakeAssociatedContextCurrentAMD(ctx) -> None: ...
