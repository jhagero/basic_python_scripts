from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_CONDITION_SATISFIED_KHR: Incomplete
EGL_FOREVER_KHR: Incomplete
EGL_SIGNALED_KHR: Incomplete
EGL_SYNC_FLUSH_COMMANDS_BIT_KHR: Incomplete
EGL_SYNC_REUSABLE_KHR: Incomplete
EGL_SYNC_STATUS_KHR: Incomplete
EGL_SYNC_TYPE_KHR: Incomplete
EGL_TIMEOUT_EXPIRED_KHR: Incomplete
EGL_UNSIGNALED_KHR: Incomplete

@_f
def eglClientWaitSyncKHR(dpy, sync, flags, timeout) -> None: ...
@_f
def eglCreateSyncKHR(dpy, type, attrib_list) -> None: ...
@_f
def eglDestroySyncKHR(dpy, sync) -> None: ...
@_f
def eglGetSyncAttribKHR(dpy, sync, attribute, value) -> None: ...
@_f
def eglSignalSyncKHR(dpy, sync, mode) -> None: ...
