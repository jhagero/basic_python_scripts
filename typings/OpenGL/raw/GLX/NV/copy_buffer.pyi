from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays

@_f
def glXCopyBufferSubDataNV(dpy, readCtx, writeCtx, readTarget, writeTarget, readOffset, writeOffset, size) -> None: ...
@_f
def glXNamedCopyBufferSubDataNV(dpy, readCtx, writeCtx, readBuffer, writeBuffer, readOffset, writeOffset, size) -> None: ...
