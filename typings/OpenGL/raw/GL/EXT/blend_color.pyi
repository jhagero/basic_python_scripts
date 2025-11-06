from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BLEND_COLOR_EXT: Incomplete
GL_CONSTANT_ALPHA_EXT: Incomplete
GL_CONSTANT_COLOR_EXT: Incomplete
GL_ONE_MINUS_CONSTANT_ALPHA_EXT: Incomplete
GL_ONE_MINUS_CONSTANT_COLOR_EXT: Incomplete

@_f
def glBlendColorEXT(red, green, blue, alpha) -> None: ...
