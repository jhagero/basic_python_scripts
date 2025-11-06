from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_POINT_DISTANCE_ATTENUATION_ARB: Incomplete
GL_POINT_FADE_THRESHOLD_SIZE_ARB: Incomplete
GL_POINT_SIZE_MAX_ARB: Incomplete
GL_POINT_SIZE_MIN_ARB: Incomplete

@_f
def glPointParameterfARB(pname, param) -> None: ...
@_f
def glPointParameterfvARB(pname, params) -> None: ...
