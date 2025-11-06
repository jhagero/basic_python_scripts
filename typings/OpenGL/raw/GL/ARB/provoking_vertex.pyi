from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FIRST_VERTEX_CONVENTION: Incomplete
GL_LAST_VERTEX_CONVENTION: Incomplete
GL_PROVOKING_VERTEX: Incomplete
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION: Incomplete

@_f
def glProvokingVertex(mode) -> None: ...
