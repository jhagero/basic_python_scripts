from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_STREAM_FIFO_LENGTH_KHR: Incomplete
EGL_STREAM_TIME_CONSUMER_KHR: Incomplete
EGL_STREAM_TIME_NOW_KHR: Incomplete
EGL_STREAM_TIME_PRODUCER_KHR: Incomplete

@_f
def eglQueryStreamTimeKHR(dpy, stream, attribute, value) -> None: ...
