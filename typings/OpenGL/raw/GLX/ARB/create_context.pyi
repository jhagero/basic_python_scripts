from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_CONTEXT_DEBUG_BIT_ARB: Incomplete
GLX_CONTEXT_FLAGS_ARB: Incomplete
GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB: Incomplete
GLX_CONTEXT_MAJOR_VERSION_ARB: Incomplete
GLX_CONTEXT_MINOR_VERSION_ARB: Incomplete

@_f
def glXCreateContextAttribsARB(dpy, config, share_context, direct, attrib_list) -> None: ...
