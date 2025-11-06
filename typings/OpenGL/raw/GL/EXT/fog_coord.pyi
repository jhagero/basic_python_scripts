from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_FOG_COORDINATE_EXT: Incomplete
GL_FOG_COORDINATE_ARRAY_EXT: Incomplete
GL_FOG_COORDINATE_ARRAY_POINTER_EXT: Incomplete
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT: Incomplete
GL_FOG_COORDINATE_ARRAY_TYPE_EXT: Incomplete
GL_FOG_COORDINATE_EXT: Incomplete
GL_FOG_COORDINATE_SOURCE_EXT: Incomplete
GL_FRAGMENT_DEPTH_EXT: Incomplete

@_f
def glFogCoordPointerEXT(type, stride, pointer) -> None: ...
@_f
def glFogCoorddEXT(coord) -> None: ...
@_f
def glFogCoorddvEXT(coord) -> None: ...
@_f
def glFogCoordfEXT(coord) -> None: ...
@_f
def glFogCoordfvEXT(coord) -> None: ...
