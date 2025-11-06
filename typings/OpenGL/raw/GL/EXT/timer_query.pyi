from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TIME_ELAPSED_EXT: Incomplete

@_f
def glGetQueryObjecti64vEXT(id, pname, params) -> None: ...
@_f
def glGetQueryObjectui64vEXT(id, pname, params) -> None: ...
