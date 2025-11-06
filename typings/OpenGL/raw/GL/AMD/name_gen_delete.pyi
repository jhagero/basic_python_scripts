from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DATA_BUFFER_AMD: Incomplete
GL_PERFORMANCE_MONITOR_AMD: Incomplete
GL_QUERY_OBJECT_AMD: Incomplete
GL_SAMPLER_OBJECT_AMD: Incomplete
GL_VERTEX_ARRAY_OBJECT_AMD: Incomplete

@_f
def glDeleteNamesAMD(identifier, num, names) -> None: ...
@_f
def glGenNamesAMD(identifier, num, names) -> None: ...
@_f
def glIsNameAMD(identifier, name) -> None: ...
