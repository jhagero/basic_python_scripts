from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

ERROR_INVALID_VERSION_ARB: Incomplete
WGL_CONTEXT_DEBUG_BIT_ARB: Incomplete
WGL_CONTEXT_FLAGS_ARB: Incomplete
WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB: Incomplete
WGL_CONTEXT_LAYER_PLANE_ARB: Incomplete
WGL_CONTEXT_MAJOR_VERSION_ARB: Incomplete
WGL_CONTEXT_MINOR_VERSION_ARB: Incomplete

@_f
def wglCreateContextAttribsARB(hDC, hShareContext, attribList) -> None: ...
