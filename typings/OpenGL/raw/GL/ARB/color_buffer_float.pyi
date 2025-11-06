from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CLAMP_FRAGMENT_COLOR_ARB: Incomplete
GL_CLAMP_READ_COLOR_ARB: Incomplete
GL_CLAMP_VERTEX_COLOR_ARB: Incomplete
GL_FIXED_ONLY_ARB: Incomplete
GL_RGBA_FLOAT_MODE_ARB: Incomplete

@_f
def glClampColorARB(target, clamp) -> None: ...
