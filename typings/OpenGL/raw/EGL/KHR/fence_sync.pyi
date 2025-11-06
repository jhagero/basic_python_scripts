from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_SYNC_CONDITION_KHR: Incomplete
EGL_SYNC_FENCE_KHR: Incomplete
EGL_SYNC_PRIOR_COMMANDS_COMPLETE_KHR: Incomplete

@_f
def eglClientWaitSyncKHR(dpy, sync, flags, timeout) -> None: ...
@_f
def eglCreateSyncKHR(dpy, type, attrib_list) -> None: ...
@_f
def eglDestroySyncKHR(dpy, sync) -> None: ...
@_f
def eglGetSyncAttribKHR(dpy, sync, attribute, value) -> None: ...
