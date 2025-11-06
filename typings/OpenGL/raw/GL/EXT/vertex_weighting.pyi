from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_VERTEX_WEIGHT_EXT: Incomplete
GL_MODELVIEW0_EXT: Incomplete
GL_MODELVIEW0_MATRIX_EXT: Incomplete
GL_MODELVIEW0_STACK_DEPTH_EXT: Incomplete
GL_MODELVIEW1_EXT: Incomplete
GL_MODELVIEW1_MATRIX_EXT: Incomplete
GL_MODELVIEW1_STACK_DEPTH_EXT: Incomplete
GL_VERTEX_WEIGHTING_EXT: Incomplete
GL_VERTEX_WEIGHT_ARRAY_EXT: Incomplete
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT: Incomplete
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT: Incomplete
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT: Incomplete
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT: Incomplete

@_f
def glVertexWeightPointerEXT(size, type, stride, pointer) -> None: ...
@_f
def glVertexWeightfEXT(weight) -> None: ...
@_f
def glVertexWeightfvEXT(weight) -> None: ...
