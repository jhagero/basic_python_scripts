from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_BAD_HYPERPIPE_CONFIG_SGIX: Incomplete
GLX_BAD_HYPERPIPE_SGIX: Incomplete
GLX_HYPERPIPE_DISPLAY_PIPE_SGIX: Incomplete
GLX_HYPERPIPE_ID_SGIX: Incomplete
GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX: Incomplete
GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX: Incomplete
GLX_HYPERPIPE_RENDER_PIPE_SGIX: Incomplete
GLX_HYPERPIPE_STEREO_SGIX: Incomplete
GLX_PIPE_RECT_LIMITS_SGIX: Incomplete
GLX_PIPE_RECT_SGIX: Incomplete

@_f
def glXBindHyperpipeSGIX(dpy, hpId) -> None: ...
@_f
def glXDestroyHyperpipeConfigSGIX(dpy, hpId) -> None: ...
@_f
def glXHyperpipeAttribSGIX(dpy, timeSlice, attrib, size, attribList) -> None: ...
@_f
def glXHyperpipeConfigSGIX(dpy, networkId, npipes, cfg, hpId) -> None: ...
@_f
def glXQueryHyperpipeAttribSGIX(dpy, timeSlice, attrib, size, returnAttribList) -> None: ...
@_f
def glXQueryHyperpipeBestAttribSGIX(dpy, timeSlice, attrib, size, attribList, returnAttribList) -> None: ...
@_f
def glXQueryHyperpipeConfigSGIX(dpy, hpId, npipes) -> None: ...
@_f
def glXQueryHyperpipeNetworkSGIX(dpy, npipes) -> None: ...
