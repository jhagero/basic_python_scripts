from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DISTANCE_ATTENUATION_SGIS: Incomplete
GL_POINT_FADE_THRESHOLD_SIZE_SGIS: Incomplete
GL_POINT_SIZE_MAX_SGIS: Incomplete
GL_POINT_SIZE_MIN_SGIS: Incomplete

@_f
def glPointParameterfSGIS(pname, param) -> None: ...
@_f
def glPointParameterfvSGIS(pname, params) -> None: ...
