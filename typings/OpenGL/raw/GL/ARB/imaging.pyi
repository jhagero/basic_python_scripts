from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BLEND_COLOR: Incomplete
GL_BLEND_EQUATION: Incomplete
GL_COLOR_MATRIX: Incomplete
GL_COLOR_MATRIX_STACK_DEPTH: Incomplete
GL_COLOR_TABLE: Incomplete
GL_COLOR_TABLE_ALPHA_SIZE: Incomplete
GL_COLOR_TABLE_BIAS: Incomplete
GL_COLOR_TABLE_BLUE_SIZE: Incomplete
GL_COLOR_TABLE_FORMAT: Incomplete
GL_COLOR_TABLE_GREEN_SIZE: Incomplete
GL_COLOR_TABLE_INTENSITY_SIZE: Incomplete
GL_COLOR_TABLE_LUMINANCE_SIZE: Incomplete
GL_COLOR_TABLE_RED_SIZE: Incomplete
GL_COLOR_TABLE_SCALE: Incomplete
GL_COLOR_TABLE_WIDTH: Incomplete
GL_CONSTANT_ALPHA: Incomplete
GL_CONSTANT_BORDER: Incomplete
GL_CONSTANT_COLOR: Incomplete
GL_CONVOLUTION_1D: Incomplete
GL_CONVOLUTION_2D: Incomplete
GL_CONVOLUTION_BORDER_COLOR: Incomplete
GL_CONVOLUTION_BORDER_MODE: Incomplete
GL_CONVOLUTION_FILTER_BIAS: Incomplete
GL_CONVOLUTION_FILTER_SCALE: Incomplete
GL_CONVOLUTION_FORMAT: Incomplete
GL_CONVOLUTION_HEIGHT: Incomplete
GL_CONVOLUTION_WIDTH: Incomplete
GL_FUNC_ADD: Incomplete
GL_FUNC_REVERSE_SUBTRACT: Incomplete
GL_FUNC_SUBTRACT: Incomplete
GL_HISTOGRAM: Incomplete
GL_HISTOGRAM_ALPHA_SIZE: Incomplete
GL_HISTOGRAM_BLUE_SIZE: Incomplete
GL_HISTOGRAM_FORMAT: Incomplete
GL_HISTOGRAM_GREEN_SIZE: Incomplete
GL_HISTOGRAM_LUMINANCE_SIZE: Incomplete
GL_HISTOGRAM_RED_SIZE: Incomplete
GL_HISTOGRAM_SINK: Incomplete
GL_HISTOGRAM_WIDTH: Incomplete
GL_MAX: Incomplete
GL_MAX_COLOR_MATRIX_STACK_DEPTH: Incomplete
GL_MAX_CONVOLUTION_HEIGHT: Incomplete
GL_MAX_CONVOLUTION_WIDTH: Incomplete
GL_MIN: Incomplete
GL_MINMAX: Incomplete
GL_MINMAX_FORMAT: Incomplete
GL_MINMAX_SINK: Incomplete
GL_ONE_MINUS_CONSTANT_ALPHA: Incomplete
GL_ONE_MINUS_CONSTANT_COLOR: Incomplete
GL_POST_COLOR_MATRIX_ALPHA_BIAS: Incomplete
GL_POST_COLOR_MATRIX_ALPHA_SCALE: Incomplete
GL_POST_COLOR_MATRIX_BLUE_BIAS: Incomplete
GL_POST_COLOR_MATRIX_BLUE_SCALE: Incomplete
GL_POST_COLOR_MATRIX_COLOR_TABLE: Incomplete
GL_POST_COLOR_MATRIX_GREEN_BIAS: Incomplete
GL_POST_COLOR_MATRIX_GREEN_SCALE: Incomplete
GL_POST_COLOR_MATRIX_RED_BIAS: Incomplete
GL_POST_COLOR_MATRIX_RED_SCALE: Incomplete
GL_POST_CONVOLUTION_ALPHA_BIAS: Incomplete
GL_POST_CONVOLUTION_ALPHA_SCALE: Incomplete
GL_POST_CONVOLUTION_BLUE_BIAS: Incomplete
GL_POST_CONVOLUTION_BLUE_SCALE: Incomplete
GL_POST_CONVOLUTION_COLOR_TABLE: Incomplete
GL_POST_CONVOLUTION_GREEN_BIAS: Incomplete
GL_POST_CONVOLUTION_GREEN_SCALE: Incomplete
GL_POST_CONVOLUTION_RED_BIAS: Incomplete
GL_POST_CONVOLUTION_RED_SCALE: Incomplete
GL_PROXY_COLOR_TABLE: Incomplete
GL_PROXY_HISTOGRAM: Incomplete
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE: Incomplete
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE: Incomplete
GL_REDUCE: Incomplete
GL_REPLICATE_BORDER: Incomplete
GL_SEPARABLE_2D: Incomplete
GL_TABLE_TOO_LARGE: Incomplete

@_f
def glBlendColor(red, green, blue, alpha) -> None: ...
@_f
def glBlendEquation(mode) -> None: ...
@_f
def glColorSubTable(target, start, count, format, type, data) -> None: ...
@_f
def glColorTable(target, internalformat, width, format, type, table) -> None: ...
@_f
def glColorTableParameterfv(target, pname, params) -> None: ...
@_f
def glColorTableParameteriv(target, pname, params) -> None: ...
@_f
def glConvolutionFilter1D(target, internalformat, width, format, type, image) -> None: ...
@_f
def glConvolutionFilter2D(target, internalformat, width, height, format, type, image) -> None: ...
@_f
def glConvolutionParameterf(target, pname, params) -> None: ...
@_f
def glConvolutionParameterfv(target, pname, params) -> None: ...
@_f
def glConvolutionParameteri(target, pname, params) -> None: ...
@_f
def glConvolutionParameteriv(target, pname, params) -> None: ...
@_f
def glCopyColorSubTable(target, start, x, y, width) -> None: ...
@_f
def glCopyColorTable(target, internalformat, x, y, width) -> None: ...
@_f
def glCopyConvolutionFilter1D(target, internalformat, x, y, width) -> None: ...
@_f
def glCopyConvolutionFilter2D(target, internalformat, x, y, width, height) -> None: ...
@_f
def glGetColorTable(target, format, type, table) -> None: ...
@_f
def glGetColorTableParameterfv(target, pname, params) -> None: ...
@_f
def glGetColorTableParameteriv(target, pname, params) -> None: ...
@_f
def glGetConvolutionFilter(target, format, type, image) -> None: ...
@_f
def glGetConvolutionParameterfv(target, pname, params) -> None: ...
@_f
def glGetConvolutionParameteriv(target, pname, params) -> None: ...
@_f
def glGetHistogram(target, reset, format, type, values) -> None: ...
@_f
def glGetHistogramParameterfv(target, pname, params) -> None: ...
@_f
def glGetHistogramParameteriv(target, pname, params) -> None: ...
@_f
def glGetMinmax(target, reset, format, type, values) -> None: ...
@_f
def glGetMinmaxParameterfv(target, pname, params) -> None: ...
@_f
def glGetMinmaxParameteriv(target, pname, params) -> None: ...
@_f
def glGetSeparableFilter(target, format, type, row, column, span) -> None: ...
@_f
def glHistogram(target, width, internalformat, sink) -> None: ...
@_f
def glMinmax(target, internalformat, sink) -> None: ...
@_f
def glResetHistogram(target) -> None: ...
@_f
def glResetMinmax(target) -> None: ...
@_f
def glSeparableFilter2D(target, internalformat, width, height, format, type, row, column) -> None: ...
