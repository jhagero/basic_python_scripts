from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_BAD_DEVICE_EXT: Incomplete
EGL_DEVICE_EXT: Incomplete

@_f
def eglQueryDeviceAttribEXT(device, attribute, value) -> None: ...
@_f
def eglQueryDeviceStringEXT(device, name) -> None: ...
@_f
def eglQueryDisplayAttribEXT(dpy, attribute, value) -> None: ...
