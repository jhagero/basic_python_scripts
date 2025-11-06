from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_TEXTURE_BUFFER_SIZE_EXT: Incomplete
GL_TEXTURE_BINDING_BUFFER_EXT: Incomplete
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT: Incomplete
GL_TEXTURE_BUFFER_EXT: Incomplete
GL_TEXTURE_BUFFER_FORMAT_EXT: Incomplete

@_f
def glTexBufferEXT(target, internalformat, buffer) -> None: ...
