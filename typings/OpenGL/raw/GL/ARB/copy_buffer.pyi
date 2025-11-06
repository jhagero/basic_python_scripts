from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COPY_READ_BUFFER: Incomplete
GL_COPY_WRITE_BUFFER: Incomplete

@_f
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size) -> None: ...
