from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_BACK_BUFFER: Incomplete
EGL_BIND_TO_TEXTURE_RGB: Incomplete
EGL_BIND_TO_TEXTURE_RGBA: Incomplete
EGL_CONTEXT_LOST: Incomplete
EGL_MAX_SWAP_INTERVAL: Incomplete
EGL_MIN_SWAP_INTERVAL: Incomplete
EGL_MIPMAP_LEVEL: Incomplete
EGL_MIPMAP_TEXTURE: Incomplete
EGL_NO_TEXTURE: Incomplete
EGL_TEXTURE_2D: Incomplete
EGL_TEXTURE_FORMAT: Incomplete
EGL_TEXTURE_RGB: Incomplete
EGL_TEXTURE_RGBA: Incomplete
EGL_TEXTURE_TARGET: Incomplete

@_f
def eglBindTexImage(dpy, surface, buffer) -> None: ...
@_f
def eglReleaseTexImage(dpy, surface, buffer) -> None: ...
@_f
def eglSurfaceAttrib(dpy, surface, attribute, value) -> None: ...
@_f
def eglSwapInterval(dpy, interval) -> None: ...
