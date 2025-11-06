from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_VERTEX_ARRAY_BINDING_OES: Incomplete

@_f
def glBindVertexArrayOES(array) -> None: ...
@_f
def glDeleteVertexArraysOES(n, arrays) -> None: ...
@_f
def glGenVertexArraysOES(n, arrays) -> None: ...
@_f
def glIsVertexArrayOES(array) -> None: ...
