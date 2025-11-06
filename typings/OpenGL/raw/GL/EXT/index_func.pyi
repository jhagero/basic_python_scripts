from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_INDEX_TEST_EXT: Incomplete
GL_INDEX_TEST_FUNC_EXT: Incomplete
GL_INDEX_TEST_REF_EXT: Incomplete

@_f
def glIndexFuncEXT(func, ref) -> None: ...
