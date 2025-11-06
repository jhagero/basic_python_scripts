from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CLEAR_TEXTURE: Incomplete

@_f
def glClearTexImage(texture, level, format, type, data) -> None: ...
@_f
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data) -> None: ...
