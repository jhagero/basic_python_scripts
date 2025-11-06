from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_POLYGON_OFFSET_BIAS_EXT: Incomplete
GL_POLYGON_OFFSET_EXT: Incomplete
GL_POLYGON_OFFSET_FACTOR_EXT: Incomplete

@_f
def glPolygonOffsetEXT(factor, bias) -> None: ...
