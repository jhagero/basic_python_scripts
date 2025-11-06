from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glDrawArraysInstancedARB(mode, first, count, primcount) -> None: ...
@_f
def glDrawElementsInstancedARB(mode, count, type, indices, primcount) -> None: ...
