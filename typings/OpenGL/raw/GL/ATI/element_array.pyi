from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ELEMENT_ARRAY_ATI: Incomplete
GL_ELEMENT_ARRAY_POINTER_ATI: Incomplete
GL_ELEMENT_ARRAY_TYPE_ATI: Incomplete

@_f
def glDrawElementArrayATI(mode, count) -> None: ...
@_f
def glDrawRangeElementArrayATI(mode, start, end, count) -> None: ...
@_f
def glElementPointerATI(type, pointer) -> None: ...
