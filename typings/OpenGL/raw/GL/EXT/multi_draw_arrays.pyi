from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysEXT(mode, first, count, primcount) -> None: ...
@_f
def glMultiDrawElementsEXT(mode, count, type, indices, primcount) -> None: ...
