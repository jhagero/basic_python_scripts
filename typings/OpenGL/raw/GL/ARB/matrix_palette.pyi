from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_MATRIX_INDEX_ARB: Incomplete
GL_CURRENT_PALETTE_MATRIX_ARB: Incomplete
GL_MATRIX_INDEX_ARRAY_ARB: Incomplete
GL_MATRIX_INDEX_ARRAY_POINTER_ARB: Incomplete
GL_MATRIX_INDEX_ARRAY_SIZE_ARB: Incomplete
GL_MATRIX_INDEX_ARRAY_STRIDE_ARB: Incomplete
GL_MATRIX_INDEX_ARRAY_TYPE_ARB: Incomplete
GL_MATRIX_PALETTE_ARB: Incomplete
GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB: Incomplete
GL_MAX_PALETTE_MATRICES_ARB: Incomplete

@_f
def glCurrentPaletteMatrixARB(index) -> None: ...
@_f
def glMatrixIndexPointerARB(size, type, stride, pointer) -> None: ...
@_f
def glMatrixIndexubvARB(size, indices) -> None: ...
@_f
def glMatrixIndexuivARB(size, indices) -> None: ...
@_f
def glMatrixIndexusvARB(size, indices) -> None: ...
