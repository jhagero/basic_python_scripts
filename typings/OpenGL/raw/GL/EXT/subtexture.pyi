from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glTexSubImage1DEXT(target, level, xoffset, width, format, type, pixels) -> None: ...
@_f
def glTexSubImage2DEXT(target, level, xoffset, yoffset, width, height, format, type, pixels) -> None: ...
