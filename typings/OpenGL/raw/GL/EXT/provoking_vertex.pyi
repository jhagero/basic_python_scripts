from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FIRST_VERTEX_CONVENTION_EXT: Incomplete
GL_LAST_VERTEX_CONVENTION_EXT: Incomplete
GL_PROVOKING_VERTEX_EXT: Incomplete
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT: Incomplete

@_f
def glProvokingVertexEXT(mode) -> None: ...
