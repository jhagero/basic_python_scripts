from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_GAMMA_EXCLUDE_DESKTOP_I3D: Incomplete
WGL_GAMMA_TABLE_SIZE_I3D: Incomplete

@_f
def wglGetGammaTableI3D(hDC, iEntries, puRed, puGreen, puBlue) -> None: ...
@_f
def wglGetGammaTableParametersI3D(hDC, iAttribute, piValue) -> None: ...
@_f
def wglSetGammaTableI3D(hDC, iEntries, puRed, puGreen, puBlue) -> None: ...
@_f
def wglSetGammaTableParametersI3D(hDC, iAttribute, piValue) -> None: ...
