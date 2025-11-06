from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_SCISSOR_BOX_EXCLUSIVE_NV: Incomplete
GL_SCISSOR_TEST_EXCLUSIVE_NV: Incomplete

@_f
def glScissorExclusiveArrayvNV(first, count, v) -> None: ...
@_f
def glScissorExclusiveNV(x, y, width, height) -> None: ...
