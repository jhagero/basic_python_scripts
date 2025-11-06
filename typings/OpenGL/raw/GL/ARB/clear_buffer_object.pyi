from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glClearBufferData(target, internalformat, format, type, data) -> None: ...
@_f
def glClearBufferSubData(target, internalformat, offset, size, format, type, data) -> None: ...
