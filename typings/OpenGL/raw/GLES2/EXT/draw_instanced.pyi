from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glDrawArraysInstancedEXT(mode, start, count, primcount) -> None: ...
@_f
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount) -> None: ...
