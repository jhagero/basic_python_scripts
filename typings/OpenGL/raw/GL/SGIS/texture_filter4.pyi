from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FILTER4_SGIS: Incomplete
GL_TEXTURE_FILTER4_SIZE_SGIS: Incomplete

@_f
def glGetTexFilterFuncSGIS(target, filter, weights) -> None: ...
@_f
def glTexFilterFuncSGIS(target, filter, n, weights) -> None: ...
