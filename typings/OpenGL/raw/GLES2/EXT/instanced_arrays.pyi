from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_VERTEX_ATTRIB_ARRAY_DIVISOR_EXT: Incomplete

@_f
def glDrawArraysInstancedEXT(mode, start, count, primcount) -> None: ...
@_f
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount) -> None: ...
@_f
def glVertexAttribDivisorEXT(index, divisor) -> None: ...
