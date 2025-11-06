from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_TABLE_ALPHA_SIZE_SGI: Incomplete
GL_COLOR_TABLE_BIAS_SGI: Incomplete
GL_COLOR_TABLE_BLUE_SIZE_SGI: Incomplete
GL_COLOR_TABLE_FORMAT_SGI: Incomplete
GL_COLOR_TABLE_GREEN_SIZE_SGI: Incomplete
GL_COLOR_TABLE_INTENSITY_SIZE_SGI: Incomplete
GL_COLOR_TABLE_LUMINANCE_SIZE_SGI: Incomplete
GL_COLOR_TABLE_RED_SIZE_SGI: Incomplete
GL_COLOR_TABLE_SCALE_SGI: Incomplete
GL_COLOR_TABLE_SGI: Incomplete
GL_COLOR_TABLE_WIDTH_SGI: Incomplete
GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI: Incomplete
GL_POST_CONVOLUTION_COLOR_TABLE_SGI: Incomplete
GL_PROXY_COLOR_TABLE_SGI: Incomplete
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI: Incomplete
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI: Incomplete

@_f
def glColorTableParameterfvSGI(target, pname, params) -> None: ...
@_f
def glColorTableParameterivSGI(target, pname, params) -> None: ...
@_f
def glColorTableSGI(target, internalformat, width, format, type, table) -> None: ...
@_f
def glCopyColorTableSGI(target, internalformat, x, y, width) -> None: ...
@_f
def glGetColorTableParameterfvSGI(target, pname, params) -> None: ...
@_f
def glGetColorTableParameterivSGI(target, pname, params) -> None: ...
@_f
def glGetColorTableSGI(target, format, type, table) -> None: ...
