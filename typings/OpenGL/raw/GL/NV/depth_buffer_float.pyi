from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEPTH32F_STENCIL8_NV: Incomplete
GL_DEPTH_BUFFER_FLOAT_MODE_NV: Incomplete
GL_DEPTH_COMPONENT32F_NV: Incomplete
GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV: Incomplete

@_f
def glClearDepthdNV(depth) -> None: ...
@_f
def glDepthBoundsdNV(zmin, zmax) -> None: ...
@_f
def glDepthRangedNV(zNear, zFar) -> None: ...
