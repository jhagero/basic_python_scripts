from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE: Incomplete

@_f
def glDrawArraysInstancedANGLE(mode, first, count, primcount) -> None: ...
@_f
def glDrawElementsInstancedANGLE(mode, count, type, indices, primcount) -> None: ...
@_f
def glVertexAttribDivisorANGLE(index, divisor) -> None: ...
