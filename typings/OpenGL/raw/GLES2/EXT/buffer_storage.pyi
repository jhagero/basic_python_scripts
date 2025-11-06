from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_IMMUTABLE_STORAGE_EXT: Incomplete
GL_BUFFER_STORAGE_FLAGS_EXT: Incomplete
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT: Incomplete
GL_CLIENT_STORAGE_BIT_EXT: Incomplete
GL_DYNAMIC_STORAGE_BIT_EXT: Incomplete
GL_MAP_COHERENT_BIT_EXT: Incomplete
GL_MAP_PERSISTENT_BIT_EXT: Incomplete
GL_MAP_READ_BIT: Incomplete
GL_MAP_WRITE_BIT: Incomplete

@_f
def glBufferStorageEXT(target, size, data, flags) -> None: ...
