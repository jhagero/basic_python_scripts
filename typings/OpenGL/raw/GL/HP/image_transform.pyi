from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_AVERAGE_HP: Incomplete
GL_CUBIC_HP: Incomplete
GL_IMAGE_CUBIC_WEIGHT_HP: Incomplete
GL_IMAGE_MAG_FILTER_HP: Incomplete
GL_IMAGE_MIN_FILTER_HP: Incomplete
GL_IMAGE_ROTATE_ANGLE_HP: Incomplete
GL_IMAGE_ROTATE_ORIGIN_X_HP: Incomplete
GL_IMAGE_ROTATE_ORIGIN_Y_HP: Incomplete
GL_IMAGE_SCALE_X_HP: Incomplete
GL_IMAGE_SCALE_Y_HP: Incomplete
GL_IMAGE_TRANSFORM_2D_HP: Incomplete
GL_IMAGE_TRANSLATE_X_HP: Incomplete
GL_IMAGE_TRANSLATE_Y_HP: Incomplete
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP: Incomplete
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP: Incomplete

@_f
def glGetImageTransformParameterfvHP(target, pname, params) -> None: ...
@_f
def glGetImageTransformParameterivHP(target, pname, params) -> None: ...
@_f
def glImageTransformParameterfHP(target, pname, param) -> None: ...
@_f
def glImageTransformParameterfvHP(target, pname, params) -> None: ...
@_f
def glImageTransformParameteriHP(target, pname, param) -> None: ...
@_f
def glImageTransformParameterivHP(target, pname, params) -> None: ...
