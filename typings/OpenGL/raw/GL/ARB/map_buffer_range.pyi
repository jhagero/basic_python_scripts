from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAP_FLUSH_EXPLICIT_BIT: Incomplete
GL_MAP_INVALIDATE_BUFFER_BIT: Incomplete
GL_MAP_INVALIDATE_RANGE_BIT: Incomplete
GL_MAP_READ_BIT: Incomplete
GL_MAP_UNSYNCHRONIZED_BIT: Incomplete
GL_MAP_WRITE_BIT: Incomplete

@_f
def glFlushMappedBufferRange(target, offset, length) -> None: ...
@_f
def glMapBufferRange(target, offset, length, access) -> None: ...
