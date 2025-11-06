from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ARRAY_COUNT_EXT: Incomplete
GL_COLOR_ARRAY_EXT: Incomplete
GL_COLOR_ARRAY_POINTER_EXT: Incomplete
GL_COLOR_ARRAY_SIZE_EXT: Incomplete
GL_COLOR_ARRAY_STRIDE_EXT: Incomplete
GL_COLOR_ARRAY_TYPE_EXT: Incomplete
GL_EDGE_FLAG_ARRAY_COUNT_EXT: Incomplete
GL_EDGE_FLAG_ARRAY_EXT: Incomplete
GL_EDGE_FLAG_ARRAY_POINTER_EXT: Incomplete
GL_EDGE_FLAG_ARRAY_STRIDE_EXT: Incomplete
GL_INDEX_ARRAY_COUNT_EXT: Incomplete
GL_INDEX_ARRAY_EXT: Incomplete
GL_INDEX_ARRAY_POINTER_EXT: Incomplete
GL_INDEX_ARRAY_STRIDE_EXT: Incomplete
GL_INDEX_ARRAY_TYPE_EXT: Incomplete
GL_NORMAL_ARRAY_COUNT_EXT: Incomplete
GL_NORMAL_ARRAY_EXT: Incomplete
GL_NORMAL_ARRAY_POINTER_EXT: Incomplete
GL_NORMAL_ARRAY_STRIDE_EXT: Incomplete
GL_NORMAL_ARRAY_TYPE_EXT: Incomplete
GL_TEXTURE_COORD_ARRAY_COUNT_EXT: Incomplete
GL_TEXTURE_COORD_ARRAY_EXT: Incomplete
GL_TEXTURE_COORD_ARRAY_POINTER_EXT: Incomplete
GL_TEXTURE_COORD_ARRAY_SIZE_EXT: Incomplete
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT: Incomplete
GL_TEXTURE_COORD_ARRAY_TYPE_EXT: Incomplete
GL_VERTEX_ARRAY_COUNT_EXT: Incomplete
GL_VERTEX_ARRAY_EXT: Incomplete
GL_VERTEX_ARRAY_POINTER_EXT: Incomplete
GL_VERTEX_ARRAY_SIZE_EXT: Incomplete
GL_VERTEX_ARRAY_STRIDE_EXT: Incomplete
GL_VERTEX_ARRAY_TYPE_EXT: Incomplete

@_f
def glArrayElementEXT(i) -> None: ...
@_f
def glColorPointerEXT(size, type, stride, count, pointer) -> None: ...
@_f
def glDrawArraysEXT(mode, first, count) -> None: ...
@_f
def glEdgeFlagPointerEXT(stride, count, pointer) -> None: ...
@_f
def glGetPointervEXT(pname, params) -> None: ...
@_f
def glIndexPointerEXT(type, stride, count, pointer) -> None: ...
@_f
def glNormalPointerEXT(type, stride, count, pointer) -> None: ...
@_f
def glTexCoordPointerEXT(size, type, stride, count, pointer) -> None: ...
@_f
def glVertexPointerEXT(size, type, stride, count, pointer) -> None: ...
