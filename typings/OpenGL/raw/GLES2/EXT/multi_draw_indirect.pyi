from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysIndirectEXT(mode, indirect, drawcount, stride) -> None: ...
@_f
def glMultiDrawElementsIndirectEXT(mode, type, indirect, drawcount, stride) -> None: ...
