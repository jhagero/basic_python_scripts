from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAGMENT_PROGRAM_BINDING_NV: Incomplete
GL_FRAGMENT_PROGRAM_NV: Incomplete
GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV: Incomplete
GL_MAX_TEXTURE_COORDS_NV: Incomplete
GL_MAX_TEXTURE_IMAGE_UNITS_NV: Incomplete
GL_PROGRAM_ERROR_STRING_NV: Incomplete

@_f
def glGetProgramNamedParameterdvNV(id, len, name, params) -> None: ...
@_f
def glGetProgramNamedParameterfvNV(id, len, name, params) -> None: ...
@_f
def glProgramNamedParameter4dNV(id, len, name, x, y, z, w) -> None: ...
@_f
def glProgramNamedParameter4dvNV(id, len, name, v) -> None: ...
@_f
def glProgramNamedParameter4fNV(id, len, name, x, y, z, w) -> None: ...
@_f
def glProgramNamedParameter4fvNV(id, len, name, v) -> None: ...
