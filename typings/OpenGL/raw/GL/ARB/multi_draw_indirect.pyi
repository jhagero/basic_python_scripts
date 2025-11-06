from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysIndirect(mode, indirect, drawcount, stride) -> None: ...
@_f
def glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride) -> None: ...
