from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DISTANCE_ATTENUATION_EXT: Incomplete
GL_POINT_FADE_THRESHOLD_SIZE_EXT: Incomplete
GL_POINT_SIZE_MAX_EXT: Incomplete
GL_POINT_SIZE_MIN_EXT: Incomplete

@_f
def glPointParameterfEXT(pname, param) -> None: ...
@_f
def glPointParameterfvEXT(pname, params) -> None: ...
