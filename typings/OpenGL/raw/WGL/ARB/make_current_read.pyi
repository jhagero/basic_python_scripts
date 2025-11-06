from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB: Incomplete
ERROR_INVALID_PIXEL_TYPE_ARB: Incomplete

@_f
def wglGetCurrentReadDCARB() -> None: ...
@_f
def wglMakeContextCurrentARB(hDrawDC, hReadDC, hglrc) -> None: ...
