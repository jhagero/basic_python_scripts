from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysIndirectAMD(mode, indirect, primcount, stride) -> None: ...
@_f
def glMultiDrawElementsIndirectAMD(mode, type, indirect, primcount, stride) -> None: ...
