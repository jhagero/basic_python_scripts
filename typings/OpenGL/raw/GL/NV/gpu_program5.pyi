from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAGMENT_PROGRAM_INTERPOLATION_OFFSET_BITS_NV: Incomplete
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_NV: Incomplete
GL_MAX_GEOMETRY_PROGRAM_INVOCATIONS_NV: Incomplete
GL_MAX_PROGRAM_SUBROUTINE_NUM_NV: Incomplete
GL_MAX_PROGRAM_SUBROUTINE_PARAMETERS_NV: Incomplete
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_NV: Incomplete
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_NV: Incomplete
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_NV: Incomplete

@_f
def glGetProgramSubroutineParameteruivNV(target, index, param) -> None: ...
@_f
def glProgramSubroutineParametersuivNV(target, count, params) -> None: ...
