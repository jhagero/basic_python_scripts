from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glMultiModeDrawArraysIBM(mode, first, count, primcount, modestride) -> None: ...
@_f
def glMultiModeDrawElementsIBM(mode, count, type, indices, primcount, modestride) -> None: ...
