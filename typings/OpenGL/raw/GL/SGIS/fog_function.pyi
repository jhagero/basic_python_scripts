from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FOG_FUNC_POINTS_SGIS: Incomplete
GL_FOG_FUNC_SGIS: Incomplete
GL_MAX_FOG_FUNC_POINTS_SGIS: Incomplete

@_f
def glFogFuncSGIS(n, points) -> None: ...
@_f
def glGetFogFuncSGIS(points) -> None: ...
