from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D: Incomplete
WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D: Incomplete
WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D: Incomplete
WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D: Incomplete

@_f
def wglGetDigitalVideoParametersI3D(hDC, iAttribute, piValue) -> None: ...
@_f
def wglSetDigitalVideoParametersI3D(hDC, iAttribute, piValue) -> None: ...
