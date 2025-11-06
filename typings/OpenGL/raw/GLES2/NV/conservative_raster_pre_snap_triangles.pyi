from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONSERVATIVE_RASTER_MODE_NV: Incomplete
GL_CONSERVATIVE_RASTER_MODE_POST_SNAP_NV: Incomplete
GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_TRIANGLES_NV: Incomplete

@_f
def glConservativeRasterParameteriNV(pname, param) -> None: ...
