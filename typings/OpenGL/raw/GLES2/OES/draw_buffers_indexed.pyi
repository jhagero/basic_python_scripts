from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BLEND: Incomplete
GL_BLEND_DST_ALPHA: Incomplete
GL_BLEND_DST_RGB: Incomplete
GL_BLEND_EQUATION_ALPHA: Incomplete
GL_BLEND_EQUATION_RGB: Incomplete
GL_BLEND_SRC_ALPHA: Incomplete
GL_BLEND_SRC_RGB: Incomplete
GL_COLOR_WRITEMASK: Incomplete
GL_CONSTANT_ALPHA: Incomplete
GL_CONSTANT_COLOR: Incomplete
GL_DST_ALPHA: Incomplete
GL_DST_COLOR: Incomplete
GL_FUNC_ADD: Incomplete
GL_FUNC_REVERSE_SUBTRACT: Incomplete
GL_FUNC_SUBTRACT: Incomplete
GL_MAX: Incomplete
GL_MIN: Incomplete
GL_ONE: Incomplete
GL_ONE_MINUS_CONSTANT_ALPHA: Incomplete
GL_ONE_MINUS_CONSTANT_COLOR: Incomplete
GL_ONE_MINUS_DST_ALPHA: Incomplete
GL_ONE_MINUS_DST_COLOR: Incomplete
GL_ONE_MINUS_SRC_ALPHA: Incomplete
GL_ONE_MINUS_SRC_COLOR: Incomplete
GL_SRC_ALPHA: Incomplete
GL_SRC_ALPHA_SATURATE: Incomplete
GL_SRC_COLOR: Incomplete
GL_ZERO: Incomplete

@_f
def glBlendEquationSeparateiOES(buf, modeRGB, modeAlpha) -> None: ...
@_f
def glBlendEquationiOES(buf, mode) -> None: ...
@_f
def glBlendFuncSeparateiOES(buf, srcRGB, dstRGB, srcAlpha, dstAlpha) -> None: ...
@_f
def glBlendFunciOES(buf, src, dst) -> None: ...
@_f
def glColorMaskiOES(index, r, g, b, a) -> None: ...
@_f
def glDisableiOES(target, index) -> None: ...
@_f
def glEnableiOES(target, index) -> None: ...
@_f
def glIsEnablediOES(target, index) -> None: ...
