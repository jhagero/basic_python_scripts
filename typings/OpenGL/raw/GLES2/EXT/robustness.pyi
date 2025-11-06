from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONTEXT_ROBUST_ACCESS_EXT: Incomplete
GL_GUILTY_CONTEXT_RESET_EXT: Incomplete
GL_INNOCENT_CONTEXT_RESET_EXT: Incomplete
GL_LOSE_CONTEXT_ON_RESET_EXT: Incomplete
GL_NO_ERROR: Incomplete
GL_NO_RESET_NOTIFICATION_EXT: Incomplete
GL_RESET_NOTIFICATION_STRATEGY_EXT: Incomplete
GL_UNKNOWN_CONTEXT_RESET_EXT: Incomplete

@_f
def glGetGraphicsResetStatusEXT() -> None: ...
@_f
def glGetnUniformfvEXT(program, location, bufSize, params) -> None: ...
@_f
def glGetnUniformivEXT(program, location, bufSize, params) -> None: ...
@_f
def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, data) -> None: ...
