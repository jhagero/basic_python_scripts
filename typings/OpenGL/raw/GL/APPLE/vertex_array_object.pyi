from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_VERTEX_ARRAY_BINDING_APPLE: Incomplete

@_f
def glBindVertexArrayAPPLE(array) -> None: ...
@_f
def glDeleteVertexArraysAPPLE(n, arrays) -> None: ...
@_f
def glGenVertexArraysAPPLE(n, arrays) -> None: ...
@_f
def glIsVertexArrayAPPLE(array) -> None: ...
