from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysEXT(mode, first, count, primcount) -> None: ...
@_f
def glMultiDrawElementsEXT(mode, count, type, indices, primcount) -> None: ...
