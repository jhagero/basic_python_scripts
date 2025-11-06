from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_SUBROUTINES: Incomplete
GL_ACTIVE_SUBROUTINE_MAX_LENGTH: Incomplete
GL_ACTIVE_SUBROUTINE_UNIFORMS: Incomplete
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS: Incomplete
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH: Incomplete
GL_COMPATIBLE_SUBROUTINES: Incomplete
GL_MAX_SUBROUTINES: Incomplete
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS: Incomplete
GL_NUM_COMPATIBLE_SUBROUTINES: Incomplete
GL_UNIFORM_NAME_LENGTH: Incomplete
GL_UNIFORM_SIZE: Incomplete

@_f
def glGetActiveSubroutineName(program, shadertype, index, bufSize, length, name) -> None: ...
@_f
def glGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name) -> None: ...
@_f
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values) -> None: ...
@_f
def glGetProgramStageiv(program, shadertype, pname, values) -> None: ...
@_f
def glGetSubroutineIndex(program, shadertype, name) -> None: ...
@_f
def glGetSubroutineUniformLocation(program, shadertype, name) -> None: ...
@_f
def glGetUniformSubroutineuiv(shadertype, location, params) -> None: ...
@_f
def glUniformSubroutinesuiv(shadertype, count, indices) -> None: ...
