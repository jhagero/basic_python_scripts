from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glClearTexImageEXT(texture, level, format, type, data) -> None: ...
@_f
def glClearTexSubImageEXT(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data) -> None: ...
