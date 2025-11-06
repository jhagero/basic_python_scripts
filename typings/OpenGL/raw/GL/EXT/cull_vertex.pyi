from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CULL_VERTEX_EXT: Incomplete
GL_CULL_VERTEX_EYE_POSITION_EXT: Incomplete
GL_CULL_VERTEX_OBJECT_POSITION_EXT: Incomplete

@_f
def glCullParameterdvEXT(pname, params) -> None: ...
@_f
def glCullParameterfvEXT(pname, params) -> None: ...
