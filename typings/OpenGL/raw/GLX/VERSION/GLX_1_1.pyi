from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_EXTENSIONS: Incomplete
GLX_VENDOR: Incomplete
GLX_VERSION: Incomplete

@_f
def glXGetClientString(dpy, name) -> None: ...
@_f
def glXQueryExtensionsString(dpy, screen) -> None: ...
@_f
def glXQueryServerString(dpy, screen, name) -> None: ...
