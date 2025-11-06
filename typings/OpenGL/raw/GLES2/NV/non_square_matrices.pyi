from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FLOAT_MAT2x3_NV: Incomplete
GL_FLOAT_MAT2x4_NV: Incomplete
GL_FLOAT_MAT3x2_NV: Incomplete
GL_FLOAT_MAT3x4_NV: Incomplete
GL_FLOAT_MAT4x2_NV: Incomplete
GL_FLOAT_MAT4x3_NV: Incomplete

@_f
def glUniformMatrix2x3fvNV(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix2x4fvNV(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3x2fvNV(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3x4fvNV(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4x2fvNV(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4x3fvNV(location, count, transpose, value) -> None: ...
