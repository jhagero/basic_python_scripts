from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_ACCESS_OES: Incomplete
GL_BUFFER_MAPPED_OES: Incomplete
GL_BUFFER_MAP_POINTER_OES: Incomplete
GL_WRITE_ONLY_OES: Incomplete

@_f
def glGetBufferPointervOES(target, pname, params) -> None: ...
@_f
def glMapBufferOES(target, access) -> None: ...
@_f
def glUnmapBufferOES(target) -> None: ...
