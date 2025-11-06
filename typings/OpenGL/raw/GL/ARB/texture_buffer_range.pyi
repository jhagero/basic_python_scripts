from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TEXTURE_BUFFER_OFFSET: Incomplete
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT: Incomplete
GL_TEXTURE_BUFFER_SIZE: Incomplete

@_f
def glTexBufferRange(target, internalformat, buffer, offset, size) -> None: ...
