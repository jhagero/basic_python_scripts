from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DOUBLE: Incomplete
GL_DOUBLE_MAT2_EXT: Incomplete
GL_DOUBLE_MAT2x3_EXT: Incomplete
GL_DOUBLE_MAT2x4_EXT: Incomplete
GL_DOUBLE_MAT3_EXT: Incomplete
GL_DOUBLE_MAT3x2_EXT: Incomplete
GL_DOUBLE_MAT3x4_EXT: Incomplete
GL_DOUBLE_MAT4_EXT: Incomplete
GL_DOUBLE_MAT4x2_EXT: Incomplete
GL_DOUBLE_MAT4x3_EXT: Incomplete
GL_DOUBLE_VEC2_EXT: Incomplete
GL_DOUBLE_VEC3_EXT: Incomplete
GL_DOUBLE_VEC4_EXT: Incomplete

@_f
def glGetVertexAttribLdvEXT(index, pname, params) -> None: ...
@_f
def glVertexAttribL1dEXT(index, x) -> None: ...
@_f
def glVertexAttribL1dvEXT(index, v) -> None: ...
@_f
def glVertexAttribL2dEXT(index, x, y) -> None: ...
@_f
def glVertexAttribL2dvEXT(index, v) -> None: ...
@_f
def glVertexAttribL3dEXT(index, x, y, z) -> None: ...
@_f
def glVertexAttribL3dvEXT(index, v) -> None: ...
@_f
def glVertexAttribL4dEXT(index, x, y, z, w) -> None: ...
@_f
def glVertexAttribL4dvEXT(index, v) -> None: ...
@_f
def glVertexAttribLPointerEXT(index, size, type, stride, pointer) -> None: ...
