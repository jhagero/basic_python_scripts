from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COPY_READ_BUFFER_NV: Incomplete
GL_COPY_WRITE_BUFFER_NV: Incomplete

@_f
def glCopyBufferSubDataNV(readTarget, writeTarget, readOffset, writeOffset, size) -> None: ...
