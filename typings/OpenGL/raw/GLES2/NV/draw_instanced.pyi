from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glDrawArraysInstancedNV(mode, first, count, primcount) -> None: ...
@_f
def glDrawElementsInstancedNV(mode, count, type, indices, primcount) -> None: ...
