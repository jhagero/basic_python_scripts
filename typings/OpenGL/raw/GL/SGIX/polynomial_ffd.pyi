from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEFORMATIONS_MASK_SGIX: Incomplete
GL_GEOMETRY_DEFORMATION_BIT_SGIX: Incomplete
GL_GEOMETRY_DEFORMATION_SGIX: Incomplete
GL_MAX_DEFORMATION_ORDER_SGIX: Incomplete
GL_TEXTURE_DEFORMATION_BIT_SGIX: Incomplete
GL_TEXTURE_DEFORMATION_SGIX: Incomplete

@_f
def glDeformSGIX(mask) -> None: ...
@_f
def glDeformationMap3dSGIX(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, w1, w2, wstride, worder, points) -> None: ...
@_f
def glDeformationMap3fSGIX(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, w1, w2, wstride, worder, points) -> None: ...
@_f
def glLoadIdentityDeformationMapSGIX(mask) -> None: ...
