from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_STREAM_BIT_KHR: Incomplete

@_f
def eglCreateStreamProducerSurfaceKHR(dpy, config, stream, attrib_list) -> None: ...
