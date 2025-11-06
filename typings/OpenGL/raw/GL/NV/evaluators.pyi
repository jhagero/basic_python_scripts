from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_EVAL_2D_NV: Incomplete
GL_EVAL_FRACTIONAL_TESSELLATION_NV: Incomplete
GL_EVAL_TRIANGULAR_2D_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB0_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB10_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB11_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB12_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB13_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB14_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB15_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB1_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB2_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB3_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB4_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB5_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB6_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB7_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB8_NV: Incomplete
GL_EVAL_VERTEX_ATTRIB9_NV: Incomplete
GL_MAP_ATTRIB_U_ORDER_NV: Incomplete
GL_MAP_ATTRIB_V_ORDER_NV: Incomplete
GL_MAP_TESSELLATION_NV: Incomplete
GL_MAX_MAP_TESSELLATION_NV: Incomplete
GL_MAX_RATIONAL_EVAL_ORDER_NV: Incomplete

@_f
def glEvalMapsNV(target, mode) -> None: ...
@_f
def glGetMapAttribParameterfvNV(target, index, pname, params) -> None: ...
@_f
def glGetMapAttribParameterivNV(target, index, pname, params) -> None: ...
@_f
def glGetMapControlPointsNV(target, index, type, ustride, vstride, packed, points) -> None: ...
@_f
def glGetMapParameterfvNV(target, pname, params) -> None: ...
@_f
def glGetMapParameterivNV(target, pname, params) -> None: ...
@_f
def glMapControlPointsNV(target, index, type, ustride, vstride, uorder, vorder, packed, points) -> None: ...
@_f
def glMapParameterfvNV(target, pname, params) -> None: ...
@_f
def glMapParameterivNV(target, pname, params) -> None: ...
