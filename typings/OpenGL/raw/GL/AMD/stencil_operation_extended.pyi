from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_REPLACE_VALUE_AMD: Incomplete
GL_SET_AMD: Incomplete
GL_STENCIL_BACK_OP_VALUE_AMD: Incomplete
GL_STENCIL_OP_VALUE_AMD: Incomplete

@_f
def glStencilOpValueAMD(face, value) -> None: ...
