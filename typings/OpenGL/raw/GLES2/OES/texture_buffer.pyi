from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_IMAGE_BUFFER_OES: Incomplete
GL_INT_IMAGE_BUFFER_OES: Incomplete
GL_INT_SAMPLER_BUFFER_OES: Incomplete
GL_MAX_TEXTURE_BUFFER_SIZE_OES: Incomplete
GL_SAMPLER_BUFFER_OES: Incomplete
GL_TEXTURE_BINDING_BUFFER_OES: Incomplete
GL_TEXTURE_BUFFER_BINDING_OES: Incomplete
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_OES: Incomplete
GL_TEXTURE_BUFFER_OES: Incomplete
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_OES: Incomplete
GL_TEXTURE_BUFFER_OFFSET_OES: Incomplete
GL_TEXTURE_BUFFER_SIZE_OES: Incomplete
GL_UNSIGNED_INT_IMAGE_BUFFER_OES: Incomplete
GL_UNSIGNED_INT_SAMPLER_BUFFER_OES: Incomplete

@_f
def glTexBufferOES(target, internalformat, buffer) -> None: ...
@_f
def glTexBufferRangeOES(target, internalformat, buffer, offset, size) -> None: ...
