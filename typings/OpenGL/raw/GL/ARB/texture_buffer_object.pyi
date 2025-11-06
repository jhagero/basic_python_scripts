from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_TEXTURE_BUFFER_SIZE_ARB: Incomplete
GL_TEXTURE_BINDING_BUFFER_ARB: Incomplete
GL_TEXTURE_BUFFER_ARB: Incomplete
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB: Incomplete
GL_TEXTURE_BUFFER_FORMAT_ARB: Incomplete

@_f
def glTexBufferARB(target, internalformat, buffer) -> None: ...
