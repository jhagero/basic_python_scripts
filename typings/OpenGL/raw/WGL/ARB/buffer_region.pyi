from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_BACK_COLOR_BUFFER_BIT_ARB: Incomplete
WGL_DEPTH_BUFFER_BIT_ARB: Incomplete
WGL_FRONT_COLOR_BUFFER_BIT_ARB: Incomplete
WGL_STENCIL_BUFFER_BIT_ARB: Incomplete

@_f
def wglCreateBufferRegionARB(hDC, iLayerPlane, uType) -> None: ...
@_f
def wglDeleteBufferRegionARB(hRegion) -> None: ...
@_f
def wglRestoreBufferRegionARB(hRegion, x, y, width, height, xSrc, ySrc) -> None: ...
@_f
def wglSaveBufferRegionARB(hRegion, x, y, width, height) -> None: ...
