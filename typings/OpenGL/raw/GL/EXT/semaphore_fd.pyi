from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_HANDLE_TYPE_OPAQUE_FD_EXT: Incomplete

@_f
def glImportSemaphoreFdEXT(semaphore, handleType, fd) -> None: ...
