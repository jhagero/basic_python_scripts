from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glBufferStorageExternalEXT(target, offset, size, clientBuffer, flags) -> None: ...
@_f
def glNamedBufferStorageExternalEXT(buffer, offset, size, clientBuffer, flags) -> None: ...
