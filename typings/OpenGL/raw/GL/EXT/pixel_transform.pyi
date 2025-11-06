from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_AVERAGE_EXT: Incomplete
GL_CUBIC_EXT: Incomplete
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT: Incomplete
GL_PIXEL_CUBIC_WEIGHT_EXT: Incomplete
GL_PIXEL_MAG_FILTER_EXT: Incomplete
GL_PIXEL_MIN_FILTER_EXT: Incomplete
GL_PIXEL_TRANSFORM_2D_EXT: Incomplete
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT: Incomplete
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT: Incomplete

@_f
def glGetPixelTransformParameterfvEXT(target, pname, params) -> None: ...
@_f
def glGetPixelTransformParameterivEXT(target, pname, params) -> None: ...
@_f
def glPixelTransformParameterfEXT(target, pname, param) -> None: ...
@_f
def glPixelTransformParameterfvEXT(target, pname, params) -> None: ...
@_f
def glPixelTransformParameteriEXT(target, pname, param) -> None: ...
@_f
def glPixelTransformParameterivEXT(target, pname, params) -> None: ...
