from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV: Incomplete
GL_VERTEX_ARRAY_RANGE_LENGTH_NV: Incomplete
GL_VERTEX_ARRAY_RANGE_NV: Incomplete
GL_VERTEX_ARRAY_RANGE_POINTER_NV: Incomplete
GL_VERTEX_ARRAY_RANGE_VALID_NV: Incomplete

@_f
def glFlushVertexArrayRangeNV() -> None: ...
@_f
def glVertexArrayRangeNV(length, pointer) -> None: ...
