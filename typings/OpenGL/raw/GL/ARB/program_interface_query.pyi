from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_RESOURCES: Incomplete
GL_ACTIVE_VARIABLES: Incomplete
GL_ARRAY_SIZE: Incomplete
GL_ARRAY_STRIDE: Incomplete
GL_ATOMIC_COUNTER_BUFFER: Incomplete
GL_ATOMIC_COUNTER_BUFFER_INDEX: Incomplete
GL_BLOCK_INDEX: Incomplete
GL_BUFFER_BINDING: Incomplete
GL_BUFFER_DATA_SIZE: Incomplete
GL_BUFFER_VARIABLE: Incomplete
GL_COMPATIBLE_SUBROUTINES: Incomplete
GL_COMPUTE_SUBROUTINE: Incomplete
GL_COMPUTE_SUBROUTINE_UNIFORM: Incomplete
GL_FRAGMENT_SUBROUTINE: Incomplete
GL_FRAGMENT_SUBROUTINE_UNIFORM: Incomplete
GL_GEOMETRY_SUBROUTINE: Incomplete
GL_GEOMETRY_SUBROUTINE_UNIFORM: Incomplete
GL_IS_PER_PATCH: Incomplete
GL_IS_ROW_MAJOR: Incomplete
GL_LOCATION: Incomplete
GL_LOCATION_INDEX: Incomplete
GL_MATRIX_STRIDE: Incomplete
GL_MAX_NAME_LENGTH: Incomplete
GL_MAX_NUM_ACTIVE_VARIABLES: Incomplete
GL_MAX_NUM_COMPATIBLE_SUBROUTINES: Incomplete
GL_NAME_LENGTH: Incomplete
GL_NUM_ACTIVE_VARIABLES: Incomplete
GL_NUM_COMPATIBLE_SUBROUTINES: Incomplete
GL_OFFSET: Incomplete
GL_PROGRAM_INPUT: Incomplete
GL_PROGRAM_OUTPUT: Incomplete
GL_REFERENCED_BY_COMPUTE_SHADER: Incomplete
GL_REFERENCED_BY_FRAGMENT_SHADER: Incomplete
GL_REFERENCED_BY_GEOMETRY_SHADER: Incomplete
GL_REFERENCED_BY_TESS_CONTROL_SHADER: Incomplete
GL_REFERENCED_BY_TESS_EVALUATION_SHADER: Incomplete
GL_REFERENCED_BY_VERTEX_SHADER: Incomplete
GL_SHADER_STORAGE_BLOCK: Incomplete
GL_TESS_CONTROL_SUBROUTINE: Incomplete
GL_TESS_CONTROL_SUBROUTINE_UNIFORM: Incomplete
GL_TESS_EVALUATION_SUBROUTINE: Incomplete
GL_TESS_EVALUATION_SUBROUTINE_UNIFORM: Incomplete
GL_TOP_LEVEL_ARRAY_SIZE: Incomplete
GL_TOP_LEVEL_ARRAY_STRIDE: Incomplete
GL_TRANSFORM_FEEDBACK_VARYING: Incomplete
GL_TYPE: Incomplete
GL_UNIFORM: Incomplete
GL_UNIFORM_BLOCK: Incomplete
GL_VERTEX_SUBROUTINE: Incomplete
GL_VERTEX_SUBROUTINE_UNIFORM: Incomplete

@_f
def glGetProgramInterfaceiv(program, programInterface, pname, params) -> None: ...
@_f
def glGetProgramResourceIndex(program, programInterface, name) -> None: ...
@_f
def glGetProgramResourceLocation(program, programInterface, name) -> None: ...
@_f
def glGetProgramResourceLocationIndex(program, programInterface, name) -> None: ...
@_f
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name) -> None: ...
@_f
def glGetProgramResourceiv(program, programInterface, index, propCount, props, count, length, params) -> None: ...
