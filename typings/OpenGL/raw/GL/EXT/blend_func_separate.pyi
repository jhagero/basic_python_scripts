from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BLEND_DST_ALPHA_EXT: Incomplete
GL_BLEND_DST_RGB_EXT: Incomplete
GL_BLEND_SRC_ALPHA_EXT: Incomplete
GL_BLEND_SRC_RGB_EXT: Incomplete

@_f
def glBlendFuncSeparateEXT(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha) -> None: ...
