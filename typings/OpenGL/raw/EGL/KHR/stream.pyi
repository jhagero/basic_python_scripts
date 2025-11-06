from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_BAD_STATE_KHR: Incomplete
EGL_BAD_STREAM_KHR: Incomplete
EGL_CONSUMER_FRAME_KHR: Incomplete
EGL_CONSUMER_LATENCY_USEC_KHR: Incomplete
EGL_PRODUCER_FRAME_KHR: Incomplete
EGL_STREAM_STATE_CONNECTING_KHR: Incomplete
EGL_STREAM_STATE_CREATED_KHR: Incomplete
EGL_STREAM_STATE_DISCONNECTED_KHR: Incomplete
EGL_STREAM_STATE_EMPTY_KHR: Incomplete
EGL_STREAM_STATE_KHR: Incomplete
EGL_STREAM_STATE_NEW_FRAME_AVAILABLE_KHR: Incomplete
EGL_STREAM_STATE_OLD_FRAME_AVAILABLE_KHR: Incomplete

@_f
def eglCreateStreamKHR(dpy, attrib_list) -> None: ...
@_f
def eglDestroyStreamKHR(dpy, stream) -> None: ...
@_f
def eglQueryStreamKHR(dpy, stream, attribute, value) -> None: ...
@_f
def eglQueryStreamu64KHR(dpy, stream, attribute, value) -> None: ...
@_f
def eglStreamAttribKHR(dpy, stream, attribute, value) -> None: ...
