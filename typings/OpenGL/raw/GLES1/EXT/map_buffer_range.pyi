from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAP_FLUSH_EXPLICIT_BIT_EXT: Incomplete
GL_MAP_INVALIDATE_BUFFER_BIT_EXT: Incomplete
GL_MAP_INVALIDATE_RANGE_BIT_EXT: Incomplete
GL_MAP_READ_BIT_EXT: Incomplete
GL_MAP_UNSYNCHRONIZED_BIT_EXT: Incomplete
GL_MAP_WRITE_BIT_EXT: Incomplete

@_f
def glFlushMappedBufferRangeEXT(target, offset, length) -> None: ...
@_f
def glMapBufferRangeEXT(target, offset, length, access) -> None: ...
