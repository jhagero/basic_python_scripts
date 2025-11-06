from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL: Incomplete
GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL: Incomplete
GL_PARALLEL_ARRAYS_INTEL: Incomplete
GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL: Incomplete
GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL: Incomplete

@_f
def glColorPointervINTEL(size, type, pointer) -> None: ...
@_f
def glNormalPointervINTEL(type, pointer) -> None: ...
@_f
def glTexCoordPointervINTEL(size, type, pointer) -> None: ...
@_f
def glVertexPointervINTEL(size, type, pointer) -> None: ...
