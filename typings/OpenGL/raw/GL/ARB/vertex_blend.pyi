from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_VERTEX_UNITS_ARB: Incomplete
GL_CURRENT_WEIGHT_ARB: Incomplete
GL_MAX_VERTEX_UNITS_ARB: Incomplete
GL_MODELVIEW0_ARB: Incomplete
GL_MODELVIEW10_ARB: Incomplete
GL_MODELVIEW11_ARB: Incomplete
GL_MODELVIEW12_ARB: Incomplete
GL_MODELVIEW13_ARB: Incomplete
GL_MODELVIEW14_ARB: Incomplete
GL_MODELVIEW15_ARB: Incomplete
GL_MODELVIEW16_ARB: Incomplete
GL_MODELVIEW17_ARB: Incomplete
GL_MODELVIEW18_ARB: Incomplete
GL_MODELVIEW19_ARB: Incomplete
GL_MODELVIEW1_ARB: Incomplete
GL_MODELVIEW20_ARB: Incomplete
GL_MODELVIEW21_ARB: Incomplete
GL_MODELVIEW22_ARB: Incomplete
GL_MODELVIEW23_ARB: Incomplete
GL_MODELVIEW24_ARB: Incomplete
GL_MODELVIEW25_ARB: Incomplete
GL_MODELVIEW26_ARB: Incomplete
GL_MODELVIEW27_ARB: Incomplete
GL_MODELVIEW28_ARB: Incomplete
GL_MODELVIEW29_ARB: Incomplete
GL_MODELVIEW2_ARB: Incomplete
GL_MODELVIEW30_ARB: Incomplete
GL_MODELVIEW31_ARB: Incomplete
GL_MODELVIEW3_ARB: Incomplete
GL_MODELVIEW4_ARB: Incomplete
GL_MODELVIEW5_ARB: Incomplete
GL_MODELVIEW6_ARB: Incomplete
GL_MODELVIEW7_ARB: Incomplete
GL_MODELVIEW8_ARB: Incomplete
GL_MODELVIEW9_ARB: Incomplete
GL_VERTEX_BLEND_ARB: Incomplete
GL_WEIGHT_ARRAY_ARB: Incomplete
GL_WEIGHT_ARRAY_POINTER_ARB: Incomplete
GL_WEIGHT_ARRAY_SIZE_ARB: Incomplete
GL_WEIGHT_ARRAY_STRIDE_ARB: Incomplete
GL_WEIGHT_ARRAY_TYPE_ARB: Incomplete
GL_WEIGHT_SUM_UNITY_ARB: Incomplete

@_f
def glVertexBlendARB(count) -> None: ...
@_f
def glWeightPointerARB(size, type, stride, pointer) -> None: ...
@_f
def glWeightbvARB(size, weights) -> None: ...
@_f
def glWeightdvARB(size, weights) -> None: ...
@_f
def glWeightfvARB(size, weights) -> None: ...
@_f
def glWeightivARB(size, weights) -> None: ...
@_f
def glWeightsvARB(size, weights) -> None: ...
@_f
def glWeightubvARB(size, weights) -> None: ...
@_f
def glWeightuivARB(size, weights) -> None: ...
@_f
def glWeightusvARB(size, weights) -> None: ...
