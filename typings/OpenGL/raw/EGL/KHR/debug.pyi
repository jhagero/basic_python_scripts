from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_DEBUG_CALLBACK_KHR: Incomplete
EGL_DEBUG_MSG_CRITICAL_KHR: Incomplete
EGL_DEBUG_MSG_ERROR_KHR: Incomplete
EGL_DEBUG_MSG_INFO_KHR: Incomplete
EGL_DEBUG_MSG_WARN_KHR: Incomplete
EGL_OBJECT_CONTEXT_KHR: Incomplete
EGL_OBJECT_DISPLAY_KHR: Incomplete
EGL_OBJECT_IMAGE_KHR: Incomplete
EGL_OBJECT_STREAM_KHR: Incomplete
EGL_OBJECT_SURFACE_KHR: Incomplete
EGL_OBJECT_SYNC_KHR: Incomplete
EGL_OBJECT_THREAD_KHR: Incomplete

@_f
def eglDebugMessageControlKHR(callback, attrib_list) -> None: ...
@_f
def eglLabelObjectKHR(display, objectType, object, label) -> None: ...
@_f
def eglQueryDebugKHR(attribute, value) -> None: ...
