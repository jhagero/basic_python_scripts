from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_NATIVE_PIXMAP_KHR: Incomplete

@_f
def eglCreateImageKHR(dpy, ctx, target, buffer, attrib_list) -> None: ...
@_f
def eglDestroyImageKHR(dpy, image) -> None: ...
