from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_INDEX12_EXT: Incomplete
GL_COLOR_INDEX16_EXT: Incomplete
GL_COLOR_INDEX1_EXT: Incomplete
GL_COLOR_INDEX2_EXT: Incomplete
GL_COLOR_INDEX4_EXT: Incomplete
GL_COLOR_INDEX8_EXT: Incomplete
GL_TEXTURE_INDEX_SIZE_EXT: Incomplete

@_f
def glColorTableEXT(target, internalFormat, width, format, type, table) -> None: ...
@_f
def glGetColorTableEXT(target, format, type, data) -> None: ...
@_f
def glGetColorTableParameterfvEXT(target, pname, params) -> None: ...
@_f
def glGetColorTableParameterivEXT(target, pname, params) -> None: ...
