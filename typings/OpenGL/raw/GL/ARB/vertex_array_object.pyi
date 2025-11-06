from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_VERTEX_ARRAY_BINDING: Incomplete

@_f
def glBindVertexArray(array) -> None: ...
@_f
def glDeleteVertexArrays(n, arrays) -> None: ...
@_f
def glGenVertexArrays(n, arrays) -> None: ...
@_f
def glIsVertexArray(array) -> None: ...
