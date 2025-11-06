from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_ALPHA_SIZE: Incomplete
EGL_BAD_ACCESS: Incomplete
EGL_BAD_ALLOC: Incomplete
EGL_BAD_ATTRIBUTE: Incomplete
EGL_BAD_CONFIG: Incomplete
EGL_BAD_CONTEXT: Incomplete
EGL_BAD_CURRENT_SURFACE: Incomplete
EGL_BAD_DISPLAY: Incomplete
EGL_BAD_MATCH: Incomplete
EGL_BAD_NATIVE_PIXMAP: Incomplete
EGL_BAD_NATIVE_WINDOW: Incomplete
EGL_BAD_PARAMETER: Incomplete
EGL_BAD_SURFACE: Incomplete
EGL_BLUE_SIZE: Incomplete
EGL_BUFFER_SIZE: Incomplete
EGL_CONFIG_CAVEAT: Incomplete
EGL_CONFIG_ID: Incomplete
EGL_CORE_NATIVE_ENGINE: Incomplete
EGL_DEPTH_SIZE: Incomplete
EGL_DRAW: Incomplete
EGL_EXTENSIONS: Incomplete
EGL_FALSE: Incomplete
EGL_GREEN_SIZE: Incomplete
EGL_HEIGHT: Incomplete
EGL_LARGEST_PBUFFER: Incomplete
EGL_LEVEL: Incomplete
EGL_MAX_PBUFFER_HEIGHT: Incomplete
EGL_MAX_PBUFFER_PIXELS: Incomplete
EGL_MAX_PBUFFER_WIDTH: Incomplete
EGL_NATIVE_RENDERABLE: Incomplete
EGL_NATIVE_VISUAL_ID: Incomplete
EGL_NATIVE_VISUAL_TYPE: Incomplete
EGL_NONE: Incomplete
EGL_NON_CONFORMANT_CONFIG: Incomplete
EGL_NOT_INITIALIZED: Incomplete
EGL_PBUFFER_BIT: Incomplete
EGL_PIXMAP_BIT: Incomplete
EGL_READ: Incomplete
EGL_RED_SIZE: Incomplete
EGL_SAMPLES: Incomplete
EGL_SAMPLE_BUFFERS: Incomplete
EGL_SLOW_CONFIG: Incomplete
EGL_STENCIL_SIZE: Incomplete
EGL_SUCCESS: Incomplete
EGL_SURFACE_TYPE: Incomplete
EGL_TRANSPARENT_BLUE_VALUE: Incomplete
EGL_TRANSPARENT_GREEN_VALUE: Incomplete
EGL_TRANSPARENT_RED_VALUE: Incomplete
EGL_TRANSPARENT_RGB: Incomplete
EGL_TRANSPARENT_TYPE: Incomplete
EGL_TRUE: Incomplete
EGL_VENDOR: Incomplete
EGL_VERSION: Incomplete
EGL_WIDTH: Incomplete
EGL_WINDOW_BIT: Incomplete

@_f
def eglChooseConfig(dpy, attrib_list, configs, config_size, num_config) -> None: ...
@_f
def eglCopyBuffers(dpy, surface, target) -> None: ...
@_f
def eglCreateContext(dpy, config, share_context, attrib_list) -> None: ...
@_f
def eglCreatePbufferSurface(dpy, config, attrib_list) -> None: ...
@_f
def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list) -> None: ...
@_f
def eglCreateWindowSurface(dpy, config, win, attrib_list) -> None: ...
@_f
def eglDestroyContext(dpy, ctx) -> None: ...
@_f
def eglDestroySurface(dpy, surface) -> None: ...
@_f
def eglGetConfigAttrib(dpy, config, attribute, value) -> None: ...
@_f
def eglGetConfigs(dpy, configs, config_size, num_config) -> None: ...
@_f
def eglGetCurrentDisplay() -> None: ...
@_f
def eglGetCurrentSurface(readdraw) -> None: ...
@_f
def eglGetDisplay(display_id) -> None: ...
@_f
def eglGetError() -> None: ...
@_f
def eglGetProcAddress(procname) -> None: ...
@_f
def eglInitialize(dpy, major, minor) -> None: ...
@_f
def eglMakeCurrent(dpy, draw, read, ctx) -> None: ...
@_f
def eglQueryContext(dpy, ctx, attribute, value) -> None: ...
@_f
def eglQueryString(dpy, name) -> None: ...
@_f
def eglQuerySurface(dpy, surface, attribute, value) -> None: ...
@_f
def eglSwapBuffers(dpy, surface) -> None: ...
@_f
def eglTerminate(dpy) -> None: ...
@_f
def eglWaitGL() -> None: ...
@_f
def eglWaitNative(engine) -> None: ...
