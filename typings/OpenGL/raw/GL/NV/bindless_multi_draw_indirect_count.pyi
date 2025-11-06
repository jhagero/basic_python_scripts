from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glMultiDrawArraysIndirectBindlessCountNV(mode, indirect, drawCount, maxDrawCount, stride, vertexBufferCount) -> None: ...
@_f
def glMultiDrawElementsIndirectBindlessCountNV(mode, type, indirect, drawCount, maxDrawCount, stride, vertexBufferCount) -> None: ...
