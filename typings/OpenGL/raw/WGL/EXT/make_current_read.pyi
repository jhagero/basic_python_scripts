from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

ERROR_INVALID_PIXEL_TYPE_EXT: Incomplete

@_f
def wglGetCurrentReadDCEXT() -> None: ...
@_f
def wglMakeContextCurrentEXT(hDrawDC, hReadDC, hglrc) -> None: ...
