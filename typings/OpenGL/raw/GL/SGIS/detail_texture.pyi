from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DETAIL_TEXTURE_2D_BINDING_SGIS: Incomplete
GL_DETAIL_TEXTURE_2D_SGIS: Incomplete
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS: Incomplete
GL_DETAIL_TEXTURE_LEVEL_SGIS: Incomplete
GL_DETAIL_TEXTURE_MODE_SGIS: Incomplete
GL_LINEAR_DETAIL_ALPHA_SGIS: Incomplete
GL_LINEAR_DETAIL_COLOR_SGIS: Incomplete
GL_LINEAR_DETAIL_SGIS: Incomplete

@_f
def glDetailTexFuncSGIS(target, n, points) -> None: ...
@_f
def glGetDetailTexFuncSGIS(target, points) -> None: ...
