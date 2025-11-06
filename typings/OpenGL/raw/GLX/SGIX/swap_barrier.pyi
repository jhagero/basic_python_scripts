from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays

@_f
def glXBindSwapBarrierSGIX(dpy, drawable, barrier) -> None: ...
@_f
def glXQueryMaxSwapBarriersSGIX(dpy, screen, max) -> None: ...
