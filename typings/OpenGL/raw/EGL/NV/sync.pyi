from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_ALREADY_SIGNALED_NV: Incomplete
EGL_CONDITION_SATISFIED_NV: Incomplete
EGL_FOREVER_NV: Incomplete
EGL_SIGNALED_NV: Incomplete
EGL_SYNC_CONDITION_NV: Incomplete
EGL_SYNC_FENCE_NV: Incomplete
EGL_SYNC_FLUSH_COMMANDS_BIT_NV: Incomplete
EGL_SYNC_PRIOR_COMMANDS_COMPLETE_NV: Incomplete
EGL_SYNC_STATUS_NV: Incomplete
EGL_SYNC_TYPE_NV: Incomplete
EGL_TIMEOUT_EXPIRED_NV: Incomplete
EGL_UNSIGNALED_NV: Incomplete

@_f
def eglClientWaitSyncNV(sync, flags, timeout) -> None: ...
@_f
def eglCreateFenceSyncNV(dpy, condition, attrib_list) -> None: ...
@_f
def eglDestroySyncNV(sync) -> None: ...
@_f
def eglFenceNV(sync) -> None: ...
@_f
def eglGetSyncAttribNV(sync, attribute, value) -> None: ...
@_f
def eglSignalSyncNV(sync, mode) -> None: ...
