from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_STORAGE_CACHED_APPLE: Incomplete
GL_STORAGE_CLIENT_APPLE: Incomplete
GL_STORAGE_SHARED_APPLE: Incomplete
GL_VERTEX_ARRAY_RANGE_APPLE: Incomplete
GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE: Incomplete
GL_VERTEX_ARRAY_RANGE_POINTER_APPLE: Incomplete
GL_VERTEX_ARRAY_STORAGE_HINT_APPLE: Incomplete

@_f
def glFlushVertexArrayRangeAPPLE(length, pointer) -> None: ...
@_f
def glVertexArrayParameteriAPPLE(pname, param) -> None: ...
@_f
def glVertexArrayRangeAPPLE(length, pointer) -> None: ...
