from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ARRAY_BUFFER_ARB: Incomplete
GL_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_BUFFER_ACCESS_ARB: Incomplete
GL_BUFFER_MAPPED_ARB: Incomplete
GL_BUFFER_MAP_POINTER_ARB: Incomplete
GL_BUFFER_SIZE_ARB: Incomplete
GL_BUFFER_USAGE_ARB: Incomplete
GL_COLOR_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_DYNAMIC_COPY_ARB: Incomplete
GL_DYNAMIC_DRAW_ARB: Incomplete
GL_DYNAMIC_READ_ARB: Incomplete
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_ELEMENT_ARRAY_BUFFER_ARB: Incomplete
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_INDEX_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_READ_ONLY_ARB: Incomplete
GL_READ_WRITE_ARB: Incomplete
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_STATIC_COPY_ARB: Incomplete
GL_STATIC_DRAW_ARB: Incomplete
GL_STATIC_READ_ARB: Incomplete
GL_STREAM_COPY_ARB: Incomplete
GL_STREAM_DRAW_ARB: Incomplete
GL_STREAM_READ_ARB: Incomplete
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB: Incomplete
GL_WRITE_ONLY_ARB: Incomplete

@_f
def glBindBufferARB(target, buffer) -> None: ...
@_f
def glBufferDataARB(target, size, data, usage) -> None: ...
@_f
def glBufferSubDataARB(target, offset, size, data) -> None: ...
@_f
def glDeleteBuffersARB(n, buffers) -> None: ...
@_f
def glGenBuffersARB(n, buffers) -> None: ...
@_f
def glGetBufferParameterivARB(target, pname, params) -> None: ...
@_f
def glGetBufferPointervARB(target, pname, params) -> None: ...
@_f
def glGetBufferSubDataARB(target, offset, size, data) -> None: ...
@_f
def glIsBufferARB(buffer) -> None: ...
@_f
def glMapBufferARB(target, access) -> None: ...
@_f
def glUnmapBufferARB(target) -> None: ...
