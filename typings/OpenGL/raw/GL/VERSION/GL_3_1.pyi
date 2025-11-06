from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_UNIFORM_BLOCKS: Incomplete
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: Incomplete
GL_COPY_READ_BUFFER: Incomplete
GL_COPY_WRITE_BUFFER: Incomplete
GL_INT_SAMPLER_2D_RECT: Incomplete
GL_INT_SAMPLER_BUFFER: Incomplete
GL_INVALID_INDEX: Incomplete
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: Incomplete
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: Incomplete
GL_MAX_COMBINED_UNIFORM_BLOCKS: Incomplete
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: Incomplete
GL_MAX_FRAGMENT_UNIFORM_BLOCKS: Incomplete
GL_MAX_GEOMETRY_UNIFORM_BLOCKS: Incomplete
GL_MAX_RECTANGLE_TEXTURE_SIZE: Incomplete
GL_MAX_TEXTURE_BUFFER_SIZE: Incomplete
GL_MAX_UNIFORM_BLOCK_SIZE: Incomplete
GL_MAX_UNIFORM_BUFFER_BINDINGS: Incomplete
GL_MAX_VERTEX_UNIFORM_BLOCKS: Incomplete
GL_PRIMITIVE_RESTART: Incomplete
GL_PRIMITIVE_RESTART_INDEX: Incomplete
GL_PROXY_TEXTURE_RECTANGLE: Incomplete
GL_R16_SNORM: Incomplete
GL_R8_SNORM: Incomplete
GL_RG16_SNORM: Incomplete
GL_RG8_SNORM: Incomplete
GL_RGB16_SNORM: Incomplete
GL_RGB8_SNORM: Incomplete
GL_RGBA16_SNORM: Incomplete
GL_RGBA8_SNORM: Incomplete
GL_SAMPLER_2D_RECT: Incomplete
GL_SAMPLER_2D_RECT_SHADOW: Incomplete
GL_SAMPLER_BUFFER: Incomplete
GL_SIGNED_NORMALIZED: Incomplete
GL_TEXTURE_BINDING_BUFFER: Incomplete
GL_TEXTURE_BINDING_RECTANGLE: Incomplete
GL_TEXTURE_BUFFER: Incomplete
GL_TEXTURE_BUFFER_DATA_STORE_BINDING: Incomplete
GL_TEXTURE_RECTANGLE: Incomplete
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
GL_UNSIGNED_INT_SAMPLER_2D_RECT: Incomplete
GL_UNSIGNED_INT_SAMPLER_BUFFER: Incomplete

@_f
def glBindBufferBase(target, index, buffer) -> None: ...
@_f
def glBindBufferRange(target, index, buffer, offset, size) -> None: ...
@_f
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size) -> None: ...
@_f
def glDrawArraysInstanced(mode, first, count, instancecount) -> None: ...
@_f
def glDrawElementsInstanced(mode, count, type, indices, instancecount) -> None: ...
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
def glPrimitiveRestartIndex(index) -> None: ...
@_f
def glTexBuffer(target, internalformat, buffer) -> None: ...
@_f
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding) -> None: ...
