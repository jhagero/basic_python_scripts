from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUMP_ENVMAP_ATI: Incomplete
GL_BUMP_NUM_TEX_UNITS_ATI: Incomplete
GL_BUMP_ROT_MATRIX_ATI: Incomplete
GL_BUMP_ROT_MATRIX_SIZE_ATI: Incomplete
GL_BUMP_TARGET_ATI: Incomplete
GL_BUMP_TEX_UNITS_ATI: Incomplete
GL_DU8DV8_ATI: Incomplete
GL_DUDV_ATI: Incomplete

@_f
def glGetTexBumpParameterfvATI(pname, param) -> None: ...
@_f
def glGetTexBumpParameterivATI(pname, param) -> None: ...
@_f
def glTexBumpParameterfvATI(pname, param) -> None: ...
@_f
def glTexBumpParameterivATI(pname, param) -> None: ...
