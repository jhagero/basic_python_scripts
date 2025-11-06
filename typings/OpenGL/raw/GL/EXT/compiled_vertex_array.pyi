from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ARRAY_ELEMENT_LOCK_COUNT_EXT: Incomplete
GL_ARRAY_ELEMENT_LOCK_FIRST_EXT: Incomplete

@_f
def glLockArraysEXT(first, count) -> None: ...
@_f
def glUnlockArraysEXT() -> None: ...
