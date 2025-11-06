from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_VERTEX_ATTRIB_MAP1_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP1_COEFF_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP1_DOMAIN_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP1_ORDER_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP1_SIZE_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP2_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP2_COEFF_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP2_DOMAIN_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP2_ORDER_APPLE: Incomplete
GL_VERTEX_ATTRIB_MAP2_SIZE_APPLE: Incomplete

@_f
def glDisableVertexAttribAPPLE(index, pname) -> None: ...
@_f
def glEnableVertexAttribAPPLE(index, pname) -> None: ...
@_f
def glIsVertexAttribEnabledAPPLE(index, pname) -> None: ...
@_f
def glMapVertexAttrib1dAPPLE(index, size, u1, u2, stride, order, points) -> None: ...
@_f
def glMapVertexAttrib1fAPPLE(index, size, u1, u2, stride, order, points) -> None: ...
@_f
def glMapVertexAttrib2dAPPLE(index, size, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points) -> None: ...
@_f
def glMapVertexAttrib2fAPPLE(index, size, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points) -> None: ...
