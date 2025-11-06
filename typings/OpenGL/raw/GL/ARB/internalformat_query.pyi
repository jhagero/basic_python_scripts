from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_NUM_SAMPLE_COUNTS: Incomplete

@_f
def glGetInternalformativ(target, internalformat, pname, count, params) -> None: ...
