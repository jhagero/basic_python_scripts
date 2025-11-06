from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glBufferStorageExternalEXT(target, offset, size, clientBuffer, flags) -> None: ...
@_f
def glNamedBufferStorageExternalEXT(buffer, offset, size, clientBuffer, flags) -> None: ...
