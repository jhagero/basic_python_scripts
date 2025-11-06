from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_NO_NATIVE_FENCE_FD_ANDROID: Incomplete
EGL_SYNC_NATIVE_FENCE_ANDROID: Incomplete
EGL_SYNC_NATIVE_FENCE_FD_ANDROID: Incomplete
EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID: Incomplete

@_f
def eglDupNativeFenceFDANDROID(dpy, sync) -> None: ...
