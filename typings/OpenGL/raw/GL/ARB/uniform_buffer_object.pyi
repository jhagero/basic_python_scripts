from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_UNIFORM_BLOCKS: Incomplete
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: Incomplete
GL_INVALID_INDEX: Incomplete
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: Incomplete
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: Incomplete
GL_MAX_COMBINED_UNIFORM_BLOCKS: Incomplete
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: Incomplete
GL_MAX_FRAGMENT_UNIFORM_BLOCKS: Incomplete
GL_MAX_GEOMETRY_UNIFORM_BLOCKS: Incomplete
GL_MAX_UNIFORM_BLOCK_SIZE: Incomplete
GL_MAX_UNIFORM_BUFFER_BINDINGS: Incomplete
GL_MAX_VERTEX_UNIFORM_BLOCKS: Incomplete
GL_UNIFORM_ARRAY_STRIDE: Incomplete
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: Incomplete
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: Incomplete
GL_UNIFORM_BLOCK_BINDING: Incomplete
GL_UNIFORM_BLOCK_DATA_SIZE: Incomplete
GL_UNIFORM_BLOCK_INDEX: Incomplete
GL_UNIFORM_BLOCK_NAME_LENGTH: Incomplete
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: Incomplete
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER: Incomplete
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: Incomplete
GL_UNIFORM_BUFFER: Incomplete
GL_UNIFORM_BUFFER_BINDING: Incomplete
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: Incomplete
GL_UNIFORM_BUFFER_SIZE: Incomplete
GL_UNIFORM_BUFFER_START: Incomplete
GL_UNIFORM_IS_ROW_MAJOR: Incomplete
GL_UNIFORM_MATRIX_STRIDE: Incomplete
GL_UNIFORM_NAME_LENGTH: Incomplete
GL_UNIFORM_OFFSET: Incomplete
GL_UNIFORM_SIZE: Incomplete
GL_UNIFORM_TYPE: Incomplete

@_f
def glBindBufferBase(target, index, buffer) -> None: ...
@_f
def glBindBufferRange(target, index, buffer, offset, size) -> None: ...
@_f
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName) -> None: ...
@_f
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params) -> None: ...
@_f
def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName) -> None: ...
@_f
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params) -> None: ...
@_f
def glGetIntegeri_v(target, index, data) -> None: ...
@_f
def glGetUniformBlockIndex(program, uniformBlockName) -> None: ...
@_f
def glGetUniformIndices(program, uniformCount, uniformNames, uniformIndices) -> None: ...
@_f
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding) -> None: ...
