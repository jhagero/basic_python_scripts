from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glColorSubTableEXT(target, start, count, format, type, data) -> None: ...
@_f
def glCopyColorSubTableEXT(target, start, x, y, width) -> None: ...
