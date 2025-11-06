from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_QUERY_BY_REGION_NO_WAIT_NV: Incomplete
GL_QUERY_BY_REGION_WAIT_NV: Incomplete
GL_QUERY_NO_WAIT_NV: Incomplete
GL_QUERY_WAIT_NV: Incomplete

@_f
def glBeginConditionalRenderNV(id, mode) -> None: ...
@_f
def glEndConditionalRenderNV() -> None: ...
