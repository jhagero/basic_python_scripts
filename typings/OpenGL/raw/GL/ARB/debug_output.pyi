from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEBUG_CALLBACK_FUNCTION_ARB: Incomplete
GL_DEBUG_CALLBACK_USER_PARAM_ARB: Incomplete
GL_DEBUG_LOGGED_MESSAGES_ARB: Incomplete
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB: Incomplete
GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB: Incomplete
GL_DEBUG_SEVERITY_HIGH_ARB: Incomplete
GL_DEBUG_SEVERITY_LOW_ARB: Incomplete
GL_DEBUG_SEVERITY_MEDIUM_ARB: Incomplete
GL_DEBUG_SOURCE_API_ARB: Incomplete
GL_DEBUG_SOURCE_APPLICATION_ARB: Incomplete
GL_DEBUG_SOURCE_OTHER_ARB: Incomplete
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB: Incomplete
GL_DEBUG_SOURCE_THIRD_PARTY_ARB: Incomplete
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB: Incomplete
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB: Incomplete
GL_DEBUG_TYPE_ERROR_ARB: Incomplete
GL_DEBUG_TYPE_OTHER_ARB: Incomplete
GL_DEBUG_TYPE_PERFORMANCE_ARB: Incomplete
GL_DEBUG_TYPE_PORTABILITY_ARB: Incomplete
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB: Incomplete
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB: Incomplete
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB: Incomplete

@_f
def glDebugMessageCallbackARB(callback, userParam) -> None: ...
@_f
def glDebugMessageControlARB(source, type, severity, count, ids, enabled) -> None: ...
@_f
def glDebugMessageInsertARB(source, type, id, severity, length, buf) -> None: ...
@_f
def glGetDebugMessageLogARB(count, bufSize, sources, types, ids, severities, lengths, messageLog) -> None: ...
