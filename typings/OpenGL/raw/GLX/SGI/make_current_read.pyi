from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays

@_f
def glXGetCurrentReadDrawableSGI() -> None: ...
@_f
def glXMakeCurrentReadSGI(dpy, draw, read, ctx) -> None: ...
