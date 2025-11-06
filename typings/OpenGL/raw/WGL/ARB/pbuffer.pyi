from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_DRAW_TO_PBUFFER_ARB: Incomplete
WGL_MAX_PBUFFER_HEIGHT_ARB: Incomplete
WGL_MAX_PBUFFER_PIXELS_ARB: Incomplete
WGL_MAX_PBUFFER_WIDTH_ARB: Incomplete
WGL_PBUFFER_HEIGHT_ARB: Incomplete
WGL_PBUFFER_LARGEST_ARB: Incomplete
WGL_PBUFFER_LOST_ARB: Incomplete
WGL_PBUFFER_WIDTH_ARB: Incomplete

@_f
def wglCreatePbufferARB(hDC, iPixelFormat, iWidth, iHeight, piAttribList) -> None: ...
@_f
def wglDestroyPbufferARB(hPbuffer) -> None: ...
@_f
def wglGetPbufferDCARB(hPbuffer) -> None: ...
@_f
def wglQueryPbufferARB(hPbuffer, iAttribute, piValue) -> None: ...
@_f
def wglReleasePbufferDCARB(hPbuffer, hDC) -> None: ...
