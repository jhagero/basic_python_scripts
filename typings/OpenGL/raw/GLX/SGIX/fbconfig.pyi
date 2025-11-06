from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_COLOR_INDEX_BIT_SGIX: Incomplete
GLX_COLOR_INDEX_TYPE_SGIX: Incomplete
GLX_DRAWABLE_TYPE_SGIX: Incomplete
GLX_FBCONFIG_ID_SGIX: Incomplete
GLX_PIXMAP_BIT_SGIX: Incomplete
GLX_RENDER_TYPE_SGIX: Incomplete
GLX_RGBA_BIT_SGIX: Incomplete
GLX_RGBA_TYPE_SGIX: Incomplete
GLX_SCREEN_EXT: Incomplete
GLX_WINDOW_BIT_SGIX: Incomplete
GLX_X_RENDERABLE_SGIX: Incomplete

@_f
def glXChooseFBConfigSGIX(dpy, screen, attrib_list, nelements) -> None: ...
@_f
def glXCreateContextWithConfigSGIX(dpy, config, render_type, share_list, direct) -> None: ...
@_f
def glXCreateGLXPixmapWithConfigSGIX(dpy, config, pixmap) -> None: ...
@_f
def glXGetFBConfigAttribSGIX(dpy, config, attribute, value) -> None: ...
@_f
def glXGetFBConfigFromVisualSGIX(dpy, vis) -> None: ...
@_f
def glXGetVisualFromFBConfigSGIX(dpy, config) -> None: ...
