from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DRAW_INDIRECT_BUFFER: Incomplete
GL_DRAW_INDIRECT_BUFFER_BINDING: Incomplete

@_f
def glDrawArraysIndirect(mode, indirect) -> None: ...
@_f
def glDrawElementsIndirect(mode, type, indirect) -> None: ...
