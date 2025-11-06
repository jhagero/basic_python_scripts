from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_POST_SUB_BUFFER_SUPPORTED_NV: Incomplete

@_f
def eglPostSubBufferNV(dpy, surface, x, y, width, height) -> None: ...
