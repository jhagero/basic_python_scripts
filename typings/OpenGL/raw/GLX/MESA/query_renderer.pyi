from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_RENDERER_ACCELERATED_MESA: Incomplete
GLX_RENDERER_DEVICE_ID_MESA: Incomplete
GLX_RENDERER_OPENGL_COMPATIBILITY_PROFILE_VERSION_MESA: Incomplete
GLX_RENDERER_OPENGL_CORE_PROFILE_VERSION_MESA: Incomplete
GLX_RENDERER_OPENGL_ES2_PROFILE_VERSION_MESA: Incomplete
GLX_RENDERER_OPENGL_ES_PROFILE_VERSION_MESA: Incomplete
GLX_RENDERER_PREFERRED_PROFILE_MESA: Incomplete
GLX_RENDERER_UNIFIED_MEMORY_ARCHITECTURE_MESA: Incomplete
GLX_RENDERER_VENDOR_ID_MESA: Incomplete
GLX_RENDERER_VERSION_MESA: Incomplete
GLX_RENDERER_VIDEO_MEMORY_MESA: Incomplete

@_f
def glXQueryCurrentRendererIntegerMESA(attribute, value) -> None: ...
@_f
def glXQueryCurrentRendererStringMESA(attribute) -> None: ...
@_f
def glXQueryRendererIntegerMESA(dpy, screen, renderer, attribute, value) -> None: ...
@_f
def glXQueryRendererStringMESA(dpy, screen, renderer, attribute) -> None: ...
