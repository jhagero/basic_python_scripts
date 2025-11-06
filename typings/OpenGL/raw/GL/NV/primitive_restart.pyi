from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_PRIMITIVE_RESTART_INDEX_NV: Incomplete
GL_PRIMITIVE_RESTART_NV: Incomplete

@_f
def glPrimitiveRestartIndexNV(index) -> None: ...
@_f
def glPrimitiveRestartNV() -> None: ...
