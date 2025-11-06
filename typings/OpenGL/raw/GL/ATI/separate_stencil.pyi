from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_STENCIL_BACK_FAIL_ATI: Incomplete
GL_STENCIL_BACK_FUNC_ATI: Incomplete
GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI: Incomplete
GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI: Incomplete

@_f
def glStencilFuncSeparateATI(frontfunc, backfunc, ref, mask) -> None: ...
@_f
def glStencilOpSeparateATI(face, sfail, dpfail, dppass) -> None: ...
