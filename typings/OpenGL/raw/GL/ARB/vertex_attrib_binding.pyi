from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_VERTEX_ATTRIB_BINDINGS: Incomplete
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET: Incomplete
GL_VERTEX_ATTRIB_BINDING: Incomplete
GL_VERTEX_ATTRIB_RELATIVE_OFFSET: Incomplete
GL_VERTEX_BINDING_DIVISOR: Incomplete
GL_VERTEX_BINDING_OFFSET: Incomplete
GL_VERTEX_BINDING_STRIDE: Incomplete

@_f
def glBindVertexBuffer(bindingindex, buffer, offset, stride) -> None: ...
@_f
def glVertexAttribBinding(attribindex, bindingindex) -> None: ...
@_f
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset) -> None: ...
@_f
def glVertexAttribIFormat(attribindex, size, type, relativeoffset) -> None: ...
@_f
def glVertexAttribLFormat(attribindex, size, type, relativeoffset) -> None: ...
@_f
def glVertexBindingDivisor(bindingindex, divisor) -> None: ...
