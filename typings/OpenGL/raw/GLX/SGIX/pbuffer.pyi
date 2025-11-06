from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_ACCUM_BUFFER_BIT_SGIX: Incomplete
GLX_AUX_BUFFERS_BIT_SGIX: Incomplete
GLX_BACK_LEFT_BUFFER_BIT_SGIX: Incomplete
GLX_BACK_RIGHT_BUFFER_BIT_SGIX: Incomplete
GLX_BUFFER_CLOBBER_MASK_SGIX: Incomplete
GLX_DAMAGED_SGIX: Incomplete
GLX_DEPTH_BUFFER_BIT_SGIX: Incomplete
GLX_EVENT_MASK_SGIX: Incomplete
GLX_FRONT_LEFT_BUFFER_BIT_SGIX: Incomplete
GLX_FRONT_RIGHT_BUFFER_BIT_SGIX: Incomplete
GLX_HEIGHT_SGIX: Incomplete
GLX_LARGEST_PBUFFER_SGIX: Incomplete
GLX_MAX_PBUFFER_HEIGHT_SGIX: Incomplete
GLX_MAX_PBUFFER_PIXELS_SGIX: Incomplete
GLX_MAX_PBUFFER_WIDTH_SGIX: Incomplete
GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX: Incomplete
GLX_OPTIMAL_PBUFFER_WIDTH_SGIX: Incomplete
GLX_PBUFFER_BIT_SGIX: Incomplete
GLX_PBUFFER_SGIX: Incomplete
GLX_PRESERVED_CONTENTS_SGIX: Incomplete
GLX_SAMPLE_BUFFERS_BIT_SGIX: Incomplete
GLX_SAVED_SGIX: Incomplete
GLX_STENCIL_BUFFER_BIT_SGIX: Incomplete
GLX_WIDTH_SGIX: Incomplete
GLX_WINDOW_SGIX: Incomplete

@_f
def glXCreateGLXPbufferSGIX(dpy, config, width, height, attrib_list) -> None: ...
@_f
def glXDestroyGLXPbufferSGIX(dpy, pbuf) -> None: ...
@_f
def glXGetSelectedEventSGIX(dpy, drawable, mask) -> None: ...
@_f
def glXQueryGLXPbufferSGIX(dpy, pbuf, attribute, value) -> None: ...
@_f
def glXSelectEventSGIX(dpy, drawable, mask) -> None: ...
