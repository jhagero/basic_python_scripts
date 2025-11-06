from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_PALETTE_MATRIX_OES: Incomplete
GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES: Incomplete
GL_MATRIX_INDEX_ARRAY_OES: Incomplete
GL_MATRIX_INDEX_ARRAY_POINTER_OES: Incomplete
GL_MATRIX_INDEX_ARRAY_SIZE_OES: Incomplete
GL_MATRIX_INDEX_ARRAY_STRIDE_OES: Incomplete
GL_MATRIX_INDEX_ARRAY_TYPE_OES: Incomplete
GL_MATRIX_PALETTE_OES: Incomplete
GL_MAX_PALETTE_MATRICES_OES: Incomplete
GL_MAX_VERTEX_UNITS_OES: Incomplete
GL_WEIGHT_ARRAY_BUFFER_BINDING_OES: Incomplete
GL_WEIGHT_ARRAY_OES: Incomplete
GL_WEIGHT_ARRAY_POINTER_OES: Incomplete
GL_WEIGHT_ARRAY_SIZE_OES: Incomplete
GL_WEIGHT_ARRAY_STRIDE_OES: Incomplete
GL_WEIGHT_ARRAY_TYPE_OES: Incomplete

@_f
def glCurrentPaletteMatrixOES(matrixpaletteindex) -> None: ...
@_f
def glLoadPaletteFromModelViewMatrixOES() -> None: ...
@_f
def glMatrixIndexPointerOES(size, type, stride, pointer) -> None: ...
@_f
def glWeightPointerOES(size, type, stride, pointer) -> None: ...
