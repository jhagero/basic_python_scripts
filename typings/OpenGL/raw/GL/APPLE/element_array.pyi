from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ELEMENT_ARRAY_APPLE: Incomplete
GL_ELEMENT_ARRAY_POINTER_APPLE: Incomplete
GL_ELEMENT_ARRAY_TYPE_APPLE: Incomplete

@_f
def glDrawElementArrayAPPLE(mode, first, count) -> None: ...
@_f
def glDrawRangeElementArrayAPPLE(mode, start, end, first, count) -> None: ...
@_f
def glElementPointerAPPLE(type, pointer) -> None: ...
@_f
def glMultiDrawElementArrayAPPLE(mode, first, count, primcount) -> None: ...
@_f
def glMultiDrawRangeElementArrayAPPLE(mode, start, end, first, count, primcount) -> None: ...
