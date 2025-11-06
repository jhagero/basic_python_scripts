from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER: Incomplete
GL_BUFFER_KHR: Incomplete
GL_CONTEXT_FLAG_DEBUG_BIT: Incomplete
GL_CONTEXT_FLAG_DEBUG_BIT_KHR: Incomplete
GL_DEBUG_CALLBACK_FUNCTION: Incomplete
GL_DEBUG_CALLBACK_FUNCTION_KHR: Incomplete
GL_DEBUG_CALLBACK_USER_PARAM: Incomplete
GL_DEBUG_CALLBACK_USER_PARAM_KHR: Incomplete
GL_DEBUG_GROUP_STACK_DEPTH: Incomplete
GL_DEBUG_GROUP_STACK_DEPTH_KHR: Incomplete
GL_DEBUG_LOGGED_MESSAGES: Incomplete
GL_DEBUG_LOGGED_MESSAGES_KHR: Incomplete
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH: Incomplete
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_KHR: Incomplete
GL_DEBUG_OUTPUT: Incomplete
GL_DEBUG_OUTPUT_KHR: Incomplete
GL_DEBUG_OUTPUT_SYNCHRONOUS: Incomplete
GL_DEBUG_OUTPUT_SYNCHRONOUS_KHR: Incomplete
GL_DEBUG_SEVERITY_HIGH: Incomplete
GL_DEBUG_SEVERITY_HIGH_KHR: Incomplete
GL_DEBUG_SEVERITY_LOW: Incomplete
GL_DEBUG_SEVERITY_LOW_KHR: Incomplete
GL_DEBUG_SEVERITY_MEDIUM: Incomplete
GL_DEBUG_SEVERITY_MEDIUM_KHR: Incomplete
GL_DEBUG_SEVERITY_NOTIFICATION: Incomplete
GL_DEBUG_SEVERITY_NOTIFICATION_KHR: Incomplete
GL_DEBUG_SOURCE_API: Incomplete
GL_DEBUG_SOURCE_API_KHR: Incomplete
GL_DEBUG_SOURCE_APPLICATION: Incomplete
GL_DEBUG_SOURCE_APPLICATION_KHR: Incomplete
GL_DEBUG_SOURCE_OTHER: Incomplete
GL_DEBUG_SOURCE_OTHER_KHR: Incomplete
GL_DEBUG_SOURCE_SHADER_COMPILER: Incomplete
GL_DEBUG_SOURCE_SHADER_COMPILER_KHR: Incomplete
GL_DEBUG_SOURCE_THIRD_PARTY: Incomplete
GL_DEBUG_SOURCE_THIRD_PARTY_KHR: Incomplete
GL_DEBUG_SOURCE_WINDOW_SYSTEM: Incomplete
GL_DEBUG_SOURCE_WINDOW_SYSTEM_KHR: Incomplete
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR: Incomplete
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_KHR: Incomplete
GL_DEBUG_TYPE_ERROR: Incomplete
GL_DEBUG_TYPE_ERROR_KHR: Incomplete
GL_DEBUG_TYPE_MARKER: Incomplete
GL_DEBUG_TYPE_MARKER_KHR: Incomplete
GL_DEBUG_TYPE_OTHER: Incomplete
GL_DEBUG_TYPE_OTHER_KHR: Incomplete
GL_DEBUG_TYPE_PERFORMANCE: Incomplete
GL_DEBUG_TYPE_PERFORMANCE_KHR: Incomplete
GL_DEBUG_TYPE_POP_GROUP: Incomplete
GL_DEBUG_TYPE_POP_GROUP_KHR: Incomplete
GL_DEBUG_TYPE_PORTABILITY: Incomplete
GL_DEBUG_TYPE_PORTABILITY_KHR: Incomplete
GL_DEBUG_TYPE_PUSH_GROUP: Incomplete
GL_DEBUG_TYPE_PUSH_GROUP_KHR: Incomplete
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR: Incomplete
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_KHR: Incomplete
GL_DISPLAY_LIST: Incomplete
GL_MAX_DEBUG_GROUP_STACK_DEPTH: Incomplete
GL_MAX_DEBUG_GROUP_STACK_DEPTH_KHR: Incomplete
GL_MAX_DEBUG_LOGGED_MESSAGES: Incomplete
GL_MAX_DEBUG_LOGGED_MESSAGES_KHR: Incomplete
GL_MAX_DEBUG_MESSAGE_LENGTH: Incomplete
GL_MAX_DEBUG_MESSAGE_LENGTH_KHR: Incomplete
GL_MAX_LABEL_LENGTH: Incomplete
GL_MAX_LABEL_LENGTH_KHR: Incomplete
GL_PROGRAM: Incomplete
GL_PROGRAM_KHR: Incomplete
GL_PROGRAM_PIPELINE: Incomplete
GL_PROGRAM_PIPELINE_KHR: Incomplete
GL_QUERY: Incomplete
GL_QUERY_KHR: Incomplete
GL_SAMPLER: Incomplete
GL_SAMPLER_KHR: Incomplete
GL_SHADER: Incomplete
GL_SHADER_KHR: Incomplete
GL_STACK_OVERFLOW: Incomplete
GL_STACK_OVERFLOW_KHR: Incomplete
GL_STACK_UNDERFLOW: Incomplete
GL_STACK_UNDERFLOW_KHR: Incomplete
GL_VERTEX_ARRAY: Incomplete
GL_VERTEX_ARRAY_KHR: Incomplete

@_f
def glDebugMessageCallback(callback, userParam) -> None: ...
@_f
def glDebugMessageCallbackKHR(callback, userParam) -> None: ...
@_f
def glDebugMessageControl(source, type, severity, count, ids, enabled) -> None: ...
@_f
def glDebugMessageControlKHR(source, type, severity, count, ids, enabled) -> None: ...
@_f
def glDebugMessageInsert(source, type, id, severity, length, buf) -> None: ...
@_f
def glDebugMessageInsertKHR(source, type, id, severity, length, buf) -> None: ...
@_f
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog) -> None: ...
@_f
def glGetDebugMessageLogKHR(count, bufSize, sources, types, ids, severities, lengths, messageLog) -> None: ...
@_f
def glGetObjectLabel(identifier, name, bufSize, length, label) -> None: ...
@_f
def glGetObjectLabelKHR(identifier, name, bufSize, length, label) -> None: ...
@_f
def glGetObjectPtrLabel(ptr, bufSize, length, label) -> None: ...
@_f
def glGetObjectPtrLabelKHR(ptr, bufSize, length, label) -> None: ...
@_f
def glGetPointerv(pname, params) -> None: ...
@_f
def glGetPointervKHR(pname, params) -> None: ...
@_f
def glObjectLabel(identifier, name, length, label) -> None: ...
@_f
def glObjectLabelKHR(identifier, name, length, label) -> None: ...
@_f
def glObjectPtrLabel(ptr, length, label) -> None: ...
@_f
def glObjectPtrLabelKHR(ptr, length, label) -> None: ...
@_f
def glPopDebugGroup() -> None: ...
@_f
def glPopDebugGroupKHR() -> None: ...
@_f
def glPushDebugGroup(source, id, length, message) -> None: ...
@_f
def glPushDebugGroupKHR(source, id, length, message) -> None: ...
