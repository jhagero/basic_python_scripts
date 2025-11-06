from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_LOCATION_INDEX_EXT: Incomplete
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS_EXT: Incomplete
GL_ONE_MINUS_SRC1_ALPHA_EXT: Incomplete
GL_ONE_MINUS_SRC1_COLOR_EXT: Incomplete
GL_SRC1_ALPHA_EXT: Incomplete
GL_SRC1_COLOR_EXT: Incomplete
GL_SRC_ALPHA_SATURATE_EXT: Incomplete

@_f
def glBindFragDataLocationEXT(program, color, name) -> None: ...
@_f
def glBindFragDataLocationIndexedEXT(program, colorNumber, index, name) -> None: ...
@_f
def glGetFragDataIndexEXT(program, name) -> None: ...
@_f
def glGetProgramResourceLocationIndexEXT(program, programInterface, name) -> None: ...
