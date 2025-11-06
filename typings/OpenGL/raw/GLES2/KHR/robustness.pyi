from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONTEXT_LOST: Incomplete
GL_CONTEXT_LOST_KHR: Incomplete
GL_CONTEXT_ROBUST_ACCESS: Incomplete
GL_CONTEXT_ROBUST_ACCESS_KHR: Incomplete
GL_GUILTY_CONTEXT_RESET: Incomplete
GL_GUILTY_CONTEXT_RESET_KHR: Incomplete
GL_INNOCENT_CONTEXT_RESET: Incomplete
GL_INNOCENT_CONTEXT_RESET_KHR: Incomplete
GL_LOSE_CONTEXT_ON_RESET: Incomplete
GL_LOSE_CONTEXT_ON_RESET_KHR: Incomplete
GL_NO_ERROR: Incomplete
GL_NO_RESET_NOTIFICATION: Incomplete
GL_NO_RESET_NOTIFICATION_KHR: Incomplete
GL_RESET_NOTIFICATION_STRATEGY: Incomplete
GL_RESET_NOTIFICATION_STRATEGY_KHR: Incomplete
GL_UNKNOWN_CONTEXT_RESET: Incomplete
GL_UNKNOWN_CONTEXT_RESET_KHR: Incomplete

@_f
def glGetGraphicsResetStatus() -> None: ...
@_f
def glGetGraphicsResetStatusKHR() -> None: ...
@_f
def glGetnUniformfv(program, location, bufSize, params) -> None: ...
@_f
def glGetnUniformfvKHR(program, location, bufSize, params) -> None: ...
@_f
def glGetnUniformiv(program, location, bufSize, params) -> None: ...
@_f
def glGetnUniformivKHR(program, location, bufSize, params) -> None: ...
@_f
def glGetnUniformuiv(program, location, bufSize, params) -> None: ...
@_f
def glGetnUniformuivKHR(program, location, bufSize, params) -> None: ...
@_f
def glReadnPixels(x, y, width, height, format, type, bufSize, data) -> None: ...
@_f
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data) -> None: ...
