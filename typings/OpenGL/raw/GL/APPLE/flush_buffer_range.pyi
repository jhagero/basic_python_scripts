from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_FLUSHING_UNMAP_APPLE: Incomplete
GL_BUFFER_SERIALIZED_MODIFY_APPLE: Incomplete

@_f
def glBufferParameteriAPPLE(target, pname, param) -> None: ...
@_f
def glFlushMappedBufferRangeAPPLE(target, offset, size) -> None: ...
