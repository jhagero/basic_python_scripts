from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays

@_f
def glXCreateGLXVideoSourceSGIX(display, screen, server, path, nodeClass, drainNode) -> None: ...
@_f
def glXDestroyGLXVideoSourceSGIX(dpy, glxvideosource) -> None: ...
