from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TRANSPOSE_COLOR_MATRIX_ARB: Incomplete
GL_TRANSPOSE_MODELVIEW_MATRIX_ARB: Incomplete
GL_TRANSPOSE_PROJECTION_MATRIX_ARB: Incomplete
GL_TRANSPOSE_TEXTURE_MATRIX_ARB: Incomplete

@_f
def glLoadTransposeMatrixdARB(m) -> None: ...
@_f
def glLoadTransposeMatrixfARB(m) -> None: ...
@_f
def glMultTransposeMatrixdARB(m) -> None: ...
@_f
def glMultTransposeMatrixfARB(m) -> None: ...
