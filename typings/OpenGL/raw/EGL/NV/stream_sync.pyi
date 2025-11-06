from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_SYNC_NEW_FRAME_NV: Incomplete
EGL_SYNC_TYPE_KHR: Incomplete

@_f
def eglCreateStreamSyncNV(dpy, stream, type, attrib_list) -> None: ...
