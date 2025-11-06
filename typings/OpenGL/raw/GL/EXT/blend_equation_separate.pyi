from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BLEND_EQUATION_ALPHA_EXT: Incomplete
GL_BLEND_EQUATION_RGB_EXT: Incomplete

@_f
def glBlendEquationSeparateEXT(modeRGB, modeAlpha) -> None: ...
