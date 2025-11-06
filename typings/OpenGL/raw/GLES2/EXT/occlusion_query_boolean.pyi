from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ANY_SAMPLES_PASSED_CONSERVATIVE_EXT: Incomplete
GL_ANY_SAMPLES_PASSED_EXT: Incomplete
GL_CURRENT_QUERY_EXT: Incomplete
GL_QUERY_RESULT_AVAILABLE_EXT: Incomplete
GL_QUERY_RESULT_EXT: Incomplete

@_f
def glBeginQueryEXT(target, id) -> None: ...
@_f
def glDeleteQueriesEXT(n, ids) -> None: ...
@_f
def glEndQueryEXT(target) -> None: ...
@_f
def glGenQueriesEXT(n, ids) -> None: ...
@_f
def glGetQueryObjectuivEXT(id, pname, params) -> None: ...
@_f
def glGetQueryivEXT(target, pname, params) -> None: ...
@_f
def glIsQueryEXT(id) -> None: ...
