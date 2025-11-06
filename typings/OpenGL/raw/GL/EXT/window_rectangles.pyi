from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_EXCLUSIVE_EXT: Incomplete
GL_INCLUSIVE_EXT: Incomplete
GL_MAX_WINDOW_RECTANGLES_EXT: Incomplete
GL_NUM_WINDOW_RECTANGLES_EXT: Incomplete
GL_WINDOW_RECTANGLE_EXT: Incomplete
GL_WINDOW_RECTANGLE_MODE_EXT: Incomplete

@_f
def glWindowRectanglesEXT(mode, count, box) -> None: ...
