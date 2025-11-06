from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_IMMUTABLE_STORAGE: Incomplete
GL_BUFFER_STORAGE_FLAGS: Incomplete
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT: Incomplete
GL_CLIENT_STORAGE_BIT: Incomplete
GL_DYNAMIC_STORAGE_BIT: Incomplete
GL_MAP_COHERENT_BIT: Incomplete
GL_MAP_PERSISTENT_BIT: Incomplete
GL_MAP_READ_BIT: Incomplete
GL_MAP_WRITE_BIT: Incomplete

@_f
def glBufferStorage(target, size, data, flags) -> None: ...
