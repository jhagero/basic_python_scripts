from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_HISTOGRAM_ALPHA_SIZE_EXT: Incomplete
GL_HISTOGRAM_BLUE_SIZE_EXT: Incomplete
GL_HISTOGRAM_EXT: Incomplete
GL_HISTOGRAM_FORMAT_EXT: Incomplete
GL_HISTOGRAM_GREEN_SIZE_EXT: Incomplete
GL_HISTOGRAM_LUMINANCE_SIZE_EXT: Incomplete
GL_HISTOGRAM_RED_SIZE_EXT: Incomplete
GL_HISTOGRAM_SINK_EXT: Incomplete
GL_HISTOGRAM_WIDTH_EXT: Incomplete
GL_MINMAX_EXT: Incomplete
GL_MINMAX_FORMAT_EXT: Incomplete
GL_MINMAX_SINK_EXT: Incomplete
GL_PROXY_HISTOGRAM_EXT: Incomplete
GL_TABLE_TOO_LARGE_EXT: Incomplete

@_f
def glGetHistogramEXT(target, reset, format, type, values) -> None: ...
@_f
def glGetHistogramParameterfvEXT(target, pname, params) -> None: ...
@_f
def glGetHistogramParameterivEXT(target, pname, params) -> None: ...
@_f
def glGetMinmaxEXT(target, reset, format, type, values) -> None: ...
@_f
def glGetMinmaxParameterfvEXT(target, pname, params) -> None: ...
@_f
def glGetMinmaxParameterivEXT(target, pname, params) -> None: ...
@_f
def glHistogramEXT(target, width, internalformat, sink) -> None: ...
@_f
def glMinmaxEXT(target, internalformat, sink) -> None: ...
@_f
def glResetHistogramEXT(target) -> None: ...
@_f
def glResetMinmaxEXT(target) -> None: ...
