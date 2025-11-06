from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_SCREEN_EXT: Incomplete
GLX_SHARE_CONTEXT_EXT: Incomplete
GLX_VISUAL_ID_EXT: Incomplete

@_f
def glXFreeContextEXT(dpy, context) -> None: ...
@_f
def glXGetContextIDEXT(context) -> None: ...
@_f
def glXGetCurrentDisplayEXT() -> None: ...
@_f
def glXImportContextEXT(dpy, contextID) -> None: ...
@_f
def glXQueryContextInfoEXT(dpy, context, attribute, value) -> None: ...
