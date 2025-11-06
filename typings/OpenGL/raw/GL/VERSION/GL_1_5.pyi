from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ARRAY_BUFFER: Incomplete
GL_ARRAY_BUFFER_BINDING: Incomplete
GL_BUFFER_ACCESS: Incomplete
GL_BUFFER_MAPPED: Incomplete
GL_BUFFER_MAP_POINTER: Incomplete
GL_BUFFER_SIZE: Incomplete
GL_BUFFER_USAGE: Incomplete
GL_COLOR_ARRAY_BUFFER_BINDING: Incomplete
GL_CURRENT_FOG_COORD: Incomplete
GL_CURRENT_QUERY: Incomplete
GL_DYNAMIC_COPY: Incomplete
GL_DYNAMIC_DRAW: Incomplete
GL_DYNAMIC_READ: Incomplete
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING: Incomplete
GL_ELEMENT_ARRAY_BUFFER: Incomplete
GL_ELEMENT_ARRAY_BUFFER_BINDING: Incomplete
GL_FOG_COORD: Incomplete
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING: Incomplete
GL_FOG_COORD_ARRAY: Incomplete
GL_FOG_COORD_ARRAY_BUFFER_BINDING: Incomplete
GL_FOG_COORD_ARRAY_POINTER: Incomplete
GL_FOG_COORD_ARRAY_STRIDE: Incomplete
GL_FOG_COORD_ARRAY_TYPE: Incomplete
GL_FOG_COORD_SRC: Incomplete
GL_INDEX_ARRAY_BUFFER_BINDING: Incomplete
GL_NORMAL_ARRAY_BUFFER_BINDING: Incomplete
GL_QUERY_COUNTER_BITS: Incomplete
GL_QUERY_RESULT: Incomplete
GL_QUERY_RESULT_AVAILABLE: Incomplete
GL_READ_ONLY: Incomplete
GL_READ_WRITE: Incomplete
GL_SAMPLES_PASSED: Incomplete
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING: Incomplete
GL_SRC0_ALPHA: Incomplete
GL_SRC0_RGB: Incomplete
GL_SRC1_ALPHA: Incomplete
GL_SRC1_RGB: Incomplete
GL_SRC2_ALPHA: Incomplete
GL_SRC2_RGB: Incomplete
GL_STATIC_COPY: Incomplete
GL_STATIC_DRAW: Incomplete
GL_STATIC_READ: Incomplete
GL_STREAM_COPY: Incomplete
GL_STREAM_DRAW: Incomplete
GL_STREAM_READ: Incomplete
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING: Incomplete
GL_VERTEX_ARRAY_BUFFER_BINDING: Incomplete
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: Incomplete
GL_WEIGHT_ARRAY_BUFFER_BINDING: Incomplete
GL_WRITE_ONLY: Incomplete

@_f
def glBeginQuery(target, id) -> None: ...
@_f
def glBindBuffer(target, buffer) -> None: ...
@_f
def glBufferData(target, size, data, usage) -> None: ...
@_f
def glBufferSubData(target, offset, size, data) -> None: ...
@_f
def glDeleteBuffers(n, buffers) -> None: ...
@_f
def glDeleteQueries(n, ids) -> None: ...
@_f
def glEndQuery(target) -> None: ...
@_f
def glGenBuffers(n, buffers) -> None: ...
@_f
def glGenQueries(n, ids) -> None: ...
@_f
def glGetBufferParameteriv(target, pname, params) -> None: ...
@_f
def glGetBufferPointerv(target, pname, params) -> None: ...
@_f
def glGetBufferSubData(target, offset, size, data) -> None: ...
@_f
def glGetQueryObjectiv(id, pname, params) -> None: ...
@_f
def glGetQueryObjectuiv(id, pname, params) -> None: ...
@_f
def glGetQueryiv(target, pname, params) -> None: ...
@_f
def glIsBuffer(buffer) -> None: ...
@_f
def glIsQuery(id) -> None: ...
@_f
def glMapBuffer(target, access) -> None: ...
@_f
def glUnmapBuffer(target) -> None: ...
