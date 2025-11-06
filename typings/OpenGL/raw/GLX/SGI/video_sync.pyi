from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays

@_f
def glXGetVideoSyncSGI(count) -> None: ...
@_f
def glXWaitVideoSyncSGI(divisor, remainder, count) -> None: ...
