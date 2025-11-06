from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_READ_PIXEL_DATA_RANGE_LENGTH_NV: Incomplete
GL_READ_PIXEL_DATA_RANGE_NV: Incomplete
GL_READ_PIXEL_DATA_RANGE_POINTER_NV: Incomplete
GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV: Incomplete
GL_WRITE_PIXEL_DATA_RANGE_NV: Incomplete
GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV: Incomplete

@_f
def glFlushPixelDataRangeNV(target) -> None: ...
@_f
def glPixelDataRangeNV(target, length, pointer) -> None: ...
