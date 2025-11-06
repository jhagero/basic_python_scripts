from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEBUG_CATEGORY_API_ERROR_AMD: Incomplete
GL_DEBUG_CATEGORY_APPLICATION_AMD: Incomplete
GL_DEBUG_CATEGORY_DEPRECATION_AMD: Incomplete
GL_DEBUG_CATEGORY_OTHER_AMD: Incomplete
GL_DEBUG_CATEGORY_PERFORMANCE_AMD: Incomplete
GL_DEBUG_CATEGORY_SHADER_COMPILER_AMD: Incomplete
GL_DEBUG_CATEGORY_UNDEFINED_BEHAVIOR_AMD: Incomplete
GL_DEBUG_CATEGORY_WINDOW_SYSTEM_AMD: Incomplete
GL_DEBUG_LOGGED_MESSAGES_AMD: Incomplete
GL_DEBUG_SEVERITY_HIGH_AMD: Incomplete
GL_DEBUG_SEVERITY_LOW_AMD: Incomplete
GL_DEBUG_SEVERITY_MEDIUM_AMD: Incomplete
GL_MAX_DEBUG_LOGGED_MESSAGES_AMD: Incomplete
GL_MAX_DEBUG_MESSAGE_LENGTH_AMD: Incomplete

@_f
def glDebugMessageCallbackAMD(callback, userParam) -> None: ...
@_f
def glDebugMessageEnableAMD(category, severity, count, ids, enabled) -> None: ...
@_f
def glDebugMessageInsertAMD(category, severity, id, length, buf) -> None: ...
@_f
def glGetDebugMessageLogAMD(count, bufSize, categories, severities, ids, lengths, message) -> None: ...
