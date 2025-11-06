from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_IMMUTABLE_STORAGE: Incomplete
GL_BUFFER_STORAGE_FLAGS: Incomplete
GL_CLEAR_TEXTURE: Incomplete
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT: Incomplete
GL_CLIENT_STORAGE_BIT: Incomplete
GL_DYNAMIC_STORAGE_BIT: Incomplete
GL_LOCATION_COMPONENT: Incomplete
GL_MAP_COHERENT_BIT: Incomplete
GL_MAP_PERSISTENT_BIT: Incomplete
GL_MAP_READ_BIT: Incomplete
GL_MAP_WRITE_BIT: Incomplete
GL_MAX_VERTEX_ATTRIB_STRIDE: Incomplete
GL_MIRROR_CLAMP_TO_EDGE: Incomplete
GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED: Incomplete
GL_QUERY_BUFFER: Incomplete
GL_QUERY_BUFFER_BARRIER_BIT: Incomplete
GL_QUERY_BUFFER_BINDING: Incomplete
GL_QUERY_RESULT_NO_WAIT: Incomplete
GL_STENCIL_INDEX: Incomplete
GL_STENCIL_INDEX8: Incomplete
GL_TEXTURE_BUFFER_BINDING: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_INDEX: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE: Incomplete
GL_UNSIGNED_INT_10F_11F_11F_REV: Incomplete

@_f
def glBindBuffersBase(target, first, count, buffers) -> None: ...
@_f
def glBindBuffersRange(target, first, count, buffers, offsets, sizes) -> None: ...
@_f
def glBindImageTextures(first, count, textures) -> None: ...
@_f
def glBindSamplers(first, count, samplers) -> None: ...
@_f
def glBindTextures(first, count, textures) -> None: ...
@_f
def glBindVertexBuffers(first, count, buffers, offsets, strides) -> None: ...
@_f
def glBufferStorage(target, size, data, flags) -> None: ...
@_f
def glClearTexImage(texture, level, format, type, data) -> None: ...
@_f
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data) -> None: ...
