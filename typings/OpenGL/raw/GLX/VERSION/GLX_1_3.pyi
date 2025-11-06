from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_ACCUM_BUFFER_BIT: Incomplete
GLX_AUX_BUFFERS_BIT: Incomplete
GLX_BACK_LEFT_BUFFER_BIT: Incomplete
GLX_BACK_RIGHT_BUFFER_BIT: Incomplete
GLX_COLOR_INDEX_BIT: Incomplete
GLX_COLOR_INDEX_TYPE: Incomplete
GLX_CONFIG_CAVEAT: Incomplete
GLX_DAMAGED: Incomplete
GLX_DEPTH_BUFFER_BIT: Incomplete
GLX_DIRECT_COLOR: Incomplete
GLX_DONT_CARE: Incomplete
GLX_DRAWABLE_TYPE: Incomplete
GLX_EVENT_MASK: Incomplete
GLX_FBCONFIG_ID: Incomplete
GLX_FRONT_LEFT_BUFFER_BIT: Incomplete
GLX_FRONT_RIGHT_BUFFER_BIT: Incomplete
GLX_GRAY_SCALE: Incomplete
GLX_HEIGHT: Incomplete
GLX_LARGEST_PBUFFER: Incomplete
GLX_MAX_PBUFFER_HEIGHT: Incomplete
GLX_MAX_PBUFFER_PIXELS: Incomplete
GLX_MAX_PBUFFER_WIDTH: Incomplete
GLX_NONE: Incomplete
GLX_NON_CONFORMANT_CONFIG: Incomplete
GLX_PBUFFER: Incomplete
GLX_PBUFFER_BIT: Incomplete
GLX_PBUFFER_CLOBBER_MASK: Incomplete
GLX_PBUFFER_HEIGHT: Incomplete
GLX_PBUFFER_WIDTH: Incomplete
GLX_PIXMAP_BIT: Incomplete
GLX_PRESERVED_CONTENTS: Incomplete
GLX_PSEUDO_COLOR: Incomplete
GLX_RENDER_TYPE: Incomplete
GLX_RGBA_BIT: Incomplete
GLX_RGBA_TYPE: Incomplete
GLX_SAVED: Incomplete
GLX_SCREEN: Incomplete
GLX_SLOW_CONFIG: Incomplete
GLX_STATIC_COLOR: Incomplete
GLX_STATIC_GRAY: Incomplete
GLX_STENCIL_BUFFER_BIT: Incomplete
GLX_TRANSPARENT_ALPHA_VALUE: Incomplete
GLX_TRANSPARENT_BLUE_VALUE: Incomplete
GLX_TRANSPARENT_GREEN_VALUE: Incomplete
GLX_TRANSPARENT_INDEX: Incomplete
GLX_TRANSPARENT_INDEX_VALUE: Incomplete
GLX_TRANSPARENT_RED_VALUE: Incomplete
GLX_TRANSPARENT_RGB: Incomplete
GLX_TRANSPARENT_TYPE: Incomplete
GLX_TRUE_COLOR: Incomplete
GLX_VISUAL_ID: Incomplete
GLX_WIDTH: Incomplete
GLX_WINDOW: Incomplete
GLX_WINDOW_BIT: Incomplete
GLX_X_RENDERABLE: Incomplete
GLX_X_VISUAL_TYPE: Incomplete

@_f
def glXChooseFBConfig(dpy, screen, attrib_list, nelements) -> None: ...
@_f
def glXCreateNewContext(dpy, config, render_type, share_list, direct) -> None: ...
@_f
def glXCreatePbuffer(dpy, config, attrib_list) -> None: ...
@_f
def glXCreatePixmap(dpy, config, pixmap, attrib_list) -> None: ...
@_f
def glXCreateWindow(dpy, config, win, attrib_list) -> None: ...
@_f
def glXDestroyPbuffer(dpy, pbuf) -> None: ...
@_f
def glXDestroyPixmap(dpy, pixmap) -> None: ...
@_f
def glXDestroyWindow(dpy, win) -> None: ...
@_f
def glXGetCurrentReadDrawable() -> None: ...
@_f
def glXGetFBConfigAttrib(dpy, config, attribute, value) -> None: ...
@_f
def glXGetFBConfigs(dpy, screen, nelements) -> None: ...
@_f
def glXGetSelectedEvent(dpy, draw, event_mask) -> None: ...
@_f
def glXGetVisualFromFBConfig(dpy, config) -> None: ...
@_f
def glXMakeContextCurrent(dpy, draw, read, ctx) -> None: ...
@_f
def glXQueryContext(dpy, ctx, attribute, value) -> None: ...
@_f
def glXQueryDrawable(dpy, draw, attribute, value) -> None: ...
@_f
def glXSelectEvent(dpy, draw, event_mask) -> None: ...
