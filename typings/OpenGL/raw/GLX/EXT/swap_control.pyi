from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_MAX_SWAP_INTERVAL_EXT: Incomplete
GLX_SWAP_INTERVAL_EXT: Incomplete

@_f
def glXSwapIntervalEXT(dpy, drawable, interval) -> None: ...
