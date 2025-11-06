from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_ELEMENTS_INDICES_EXT: Incomplete
GL_MAX_ELEMENTS_VERTICES_EXT: Incomplete

@_f
def glDrawRangeElementsEXT(mode, start, end, count, type, indices) -> None: ...
