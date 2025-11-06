from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_DRAW_TO_PBUFFER_EXT: Incomplete
WGL_MAX_PBUFFER_HEIGHT_EXT: Incomplete
WGL_MAX_PBUFFER_PIXELS_EXT: Incomplete
WGL_MAX_PBUFFER_WIDTH_EXT: Incomplete
WGL_OPTIMAL_PBUFFER_HEIGHT_EXT: Incomplete
WGL_OPTIMAL_PBUFFER_WIDTH_EXT: Incomplete
WGL_PBUFFER_HEIGHT_EXT: Incomplete
WGL_PBUFFER_LARGEST_EXT: Incomplete
WGL_PBUFFER_WIDTH_EXT: Incomplete

@_f
def wglCreatePbufferEXT(hDC, iPixelFormat, iWidth, iHeight, piAttribList) -> None: ...
@_f
def wglDestroyPbufferEXT(hPbuffer) -> None: ...
@_f
def wglGetPbufferDCEXT(hPbuffer) -> None: ...
@_f
def wglQueryPbufferEXT(hPbuffer, iAttribute, piValue) -> None: ...
@_f
def wglReleasePbufferDCEXT(hPbuffer, hDC) -> None: ...
