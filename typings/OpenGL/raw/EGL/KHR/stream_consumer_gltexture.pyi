from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_CONSUMER_ACQUIRE_TIMEOUT_USEC_KHR: Incomplete

@_f
def eglStreamConsumerAcquireKHR(dpy, stream) -> None: ...
@_f
def eglStreamConsumerGLTextureExternalKHR(dpy, stream) -> None: ...
@_f
def eglStreamConsumerReleaseKHR(dpy, stream) -> None: ...
