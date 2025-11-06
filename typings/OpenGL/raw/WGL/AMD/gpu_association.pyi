from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_GPU_CLOCK_AMD: Incomplete
WGL_GPU_FASTEST_TARGET_GPUS_AMD: Incomplete
WGL_GPU_NUM_PIPES_AMD: Incomplete
WGL_GPU_NUM_RB_AMD: Incomplete
WGL_GPU_NUM_SIMD_AMD: Incomplete
WGL_GPU_NUM_SPI_AMD: Incomplete
WGL_GPU_OPENGL_VERSION_STRING_AMD: Incomplete
WGL_GPU_RAM_AMD: Incomplete
WGL_GPU_RENDERER_STRING_AMD: Incomplete
WGL_GPU_VENDOR_AMD: Incomplete

@_f
def wglBlitContextFramebufferAMD(dstCtx, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
@_f
def wglCreateAssociatedContextAMD(id) -> None: ...
@_f
def wglCreateAssociatedContextAttribsAMD(id, hShareContext, attribList) -> None: ...
@_f
def wglDeleteAssociatedContextAMD(hglrc) -> None: ...
@_f
def wglGetContextGPUIDAMD(hglrc) -> None: ...
@_f
def wglGetCurrentAssociatedContextAMD() -> None: ...
@_f
def wglGetGPUIDsAMD(maxCount, ids) -> None: ...
@_f
def wglGetGPUInfoAMD(id, property, dataType, size, data) -> None: ...
@_f
def wglMakeAssociatedContextCurrentAMD(hglrc) -> None: ...
