from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TIMESTAMP: Incomplete
GL_TIME_ELAPSED: Incomplete

@_f
def glGetQueryObjecti64v(id, pname, params) -> None: ...
@_f
def glGetQueryObjectui64v(id, pname, params) -> None: ...
@_f
def glQueryCounter(id, target) -> None: ...
