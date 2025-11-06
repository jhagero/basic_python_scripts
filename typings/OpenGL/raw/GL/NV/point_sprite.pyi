from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COORD_REPLACE_NV: Incomplete
GL_POINT_SPRITE_NV: Incomplete
GL_POINT_SPRITE_R_MODE_NV: Incomplete

@_f
def glPointParameteriNV(pname, param) -> None: ...
@_f
def glPointParameterivNV(pname, params) -> None: ...
