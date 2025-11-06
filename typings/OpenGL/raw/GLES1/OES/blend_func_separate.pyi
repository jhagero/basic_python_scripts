from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BLEND_DST_ALPHA_OES: Incomplete
GL_BLEND_DST_RGB_OES: Incomplete
GL_BLEND_SRC_ALPHA_OES: Incomplete
GL_BLEND_SRC_RGB_OES: Incomplete

@_f
def glBlendFuncSeparateOES(srcRGB, dstRGB, srcAlpha, dstAlpha) -> None: ...
