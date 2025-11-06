from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysIndirectBindlessNV(mode, indirect, drawCount, stride, vertexBufferCount) -> None: ...
@_f
def glMultiDrawElementsIndirectBindlessNV(mode, type, indirect, drawCount, stride, vertexBufferCount) -> None: ...
