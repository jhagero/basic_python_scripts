from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_DUAL_SOURCE_DRAW_BUFFERS: Incomplete
GL_ONE_MINUS_SRC1_ALPHA: Incomplete
GL_ONE_MINUS_SRC1_COLOR: Incomplete
GL_SRC1_ALPHA: Incomplete
GL_SRC1_COLOR: Incomplete

@_f
def glBindFragDataLocationIndexed(program, colorNumber, index, name) -> None: ...
@_f
def glGetFragDataIndex(program, name) -> None: ...
