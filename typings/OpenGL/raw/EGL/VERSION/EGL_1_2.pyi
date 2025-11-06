from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_ALPHA_FORMAT: Incomplete
EGL_ALPHA_FORMAT_NONPRE: Incomplete
EGL_ALPHA_FORMAT_PRE: Incomplete
EGL_ALPHA_MASK_SIZE: Incomplete
EGL_BUFFER_DESTROYED: Incomplete
EGL_BUFFER_PRESERVED: Incomplete
EGL_CLIENT_APIS: Incomplete
EGL_COLORSPACE: Incomplete
EGL_COLORSPACE_LINEAR: Incomplete
EGL_COLORSPACE_sRGB: Incomplete
EGL_COLOR_BUFFER_TYPE: Incomplete
EGL_CONTEXT_CLIENT_TYPE: Incomplete
EGL_DISPLAY_SCALING: Incomplete
EGL_HORIZONTAL_RESOLUTION: Incomplete
EGL_LUMINANCE_BUFFER: Incomplete
EGL_LUMINANCE_SIZE: Incomplete
EGL_OPENGL_ES_API: Incomplete
EGL_OPENGL_ES_BIT: Incomplete
EGL_OPENVG_API: Incomplete
EGL_OPENVG_BIT: Incomplete
EGL_OPENVG_IMAGE: Incomplete
EGL_PIXEL_ASPECT_RATIO: Incomplete
EGL_RENDERABLE_TYPE: Incomplete
EGL_RENDER_BUFFER: Incomplete
EGL_RGB_BUFFER: Incomplete
EGL_SINGLE_BUFFER: Incomplete
EGL_SWAP_BEHAVIOR: Incomplete
EGL_VERTICAL_RESOLUTION: Incomplete

@_f
def eglBindAPI(api) -> None: ...
@_f
def eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attrib_list) -> None: ...
@_f
def eglQueryAPI() -> None: ...
@_f
def eglReleaseThread() -> None: ...
@_f
def eglWaitClient() -> None: ...
