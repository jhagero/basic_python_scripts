from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_PER_STAGE_CONSTANTS_NV: Incomplete

@_f
def glCombinerStageParameterfvNV(stage, pname, params) -> None: ...
@_f
def glGetCombinerStageParameterfvNV(stage, pname, params) -> None: ...
