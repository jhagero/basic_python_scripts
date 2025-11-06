from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_LINEAR_SHARPEN_ALPHA_SGIS: Incomplete
GL_LINEAR_SHARPEN_COLOR_SGIS: Incomplete
GL_LINEAR_SHARPEN_SGIS: Incomplete
GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS: Incomplete

@_f
def glGetSharpenTexFuncSGIS(target, points) -> None: ...
@_f
def glSharpenTexFuncSGIS(target, n, points) -> None: ...
