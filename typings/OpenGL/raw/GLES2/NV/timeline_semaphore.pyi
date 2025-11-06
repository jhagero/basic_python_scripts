from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_TIMELINE_SEMAPHORE_VALUE_DIFFERENCE_NV: Incomplete
GL_SEMAPHORE_TYPE_BINARY_NV: Incomplete
GL_SEMAPHORE_TYPE_NV: Incomplete
GL_SEMAPHORE_TYPE_TIMELINE_NV: Incomplete
GL_TIMELINE_SEMAPHORE_VALUE_NV: Incomplete

@_f
def glCreateSemaphoresNV(n, semaphores) -> None: ...
@_f
def glGetSemaphoreParameterivNV(semaphore, pname, params) -> None: ...
@_f
def glSemaphoreParameterivNV(semaphore, pname, params) -> None: ...
