from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_IMAGE_BUFFER_EXT: Incomplete
GL_INT_IMAGE_BUFFER_EXT: Incomplete
GL_INT_SAMPLER_BUFFER_EXT: Incomplete
GL_MAX_TEXTURE_BUFFER_SIZE_EXT: Incomplete
GL_SAMPLER_BUFFER_EXT: Incomplete
GL_TEXTURE_BINDING_BUFFER_EXT: Incomplete
GL_TEXTURE_BUFFER_BINDING_EXT: Incomplete
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT: Incomplete
GL_TEXTURE_BUFFER_EXT: Incomplete
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT: Incomplete
GL_TEXTURE_BUFFER_OFFSET_EXT: Incomplete
GL_TEXTURE_BUFFER_SIZE_EXT: Incomplete
GL_UNSIGNED_INT_IMAGE_BUFFER_EXT: Incomplete
GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT: Incomplete

@_f
def glTexBufferEXT(target, internalformat, buffer) -> None: ...
@_f
def glTexBufferRangeEXT(target, internalformat, buffer, offset, size) -> None: ...
