from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV: Incomplete
GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV: Incomplete
GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV: Incomplete
GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV: Incomplete
GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV: Incomplete

@_f
def glProgramBufferParametersIivNV(target, bindingIndex, wordIndex, count, params) -> None: ...
@_f
def glProgramBufferParametersIuivNV(target, bindingIndex, wordIndex, count, params) -> None: ...
@_f
def glProgramBufferParametersfvNV(target, bindingIndex, wordIndex, count, params) -> None: ...
