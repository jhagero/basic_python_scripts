from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DOUBLE_MAT2: Incomplete
GL_DOUBLE_MAT2x3: Incomplete
GL_DOUBLE_MAT2x4: Incomplete
GL_DOUBLE_MAT3: Incomplete
GL_DOUBLE_MAT3x2: Incomplete
GL_DOUBLE_MAT3x4: Incomplete
GL_DOUBLE_MAT4: Incomplete
GL_DOUBLE_MAT4x2: Incomplete
GL_DOUBLE_MAT4x3: Incomplete
GL_DOUBLE_VEC2: Incomplete
GL_DOUBLE_VEC3: Incomplete
GL_DOUBLE_VEC4: Incomplete
GL_RGB32I: Incomplete

@_f
def glGetVertexAttribLdv(index, pname, params) -> None: ...
@_f
def glVertexAttribL1d(index, x) -> None: ...
@_f
def glVertexAttribL1dv(index, v) -> None: ...
@_f
def glVertexAttribL2d(index, x, y) -> None: ...
@_f
def glVertexAttribL2dv(index, v) -> None: ...
@_f
def glVertexAttribL3d(index, x, y, z) -> None: ...
@_f
def glVertexAttribL3dv(index, v) -> None: ...
@_f
def glVertexAttribL4d(index, x, y, z, w) -> None: ...
@_f
def glVertexAttribL4dv(index, v) -> None: ...
@_f
def glVertexAttribLPointer(index, size, type, stride, pointer) -> None: ...
