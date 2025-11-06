from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONVOLUTION_1D_EXT: Incomplete
GL_CONVOLUTION_2D_EXT: Incomplete
GL_CONVOLUTION_BORDER_MODE_EXT: Incomplete
GL_CONVOLUTION_FILTER_BIAS_EXT: Incomplete
GL_CONVOLUTION_FILTER_SCALE_EXT: Incomplete
GL_CONVOLUTION_FORMAT_EXT: Incomplete
GL_CONVOLUTION_HEIGHT_EXT: Incomplete
GL_CONVOLUTION_WIDTH_EXT: Incomplete
GL_MAX_CONVOLUTION_HEIGHT_EXT: Incomplete
GL_MAX_CONVOLUTION_WIDTH_EXT: Incomplete
GL_POST_CONVOLUTION_ALPHA_BIAS_EXT: Incomplete
GL_POST_CONVOLUTION_ALPHA_SCALE_EXT: Incomplete
GL_POST_CONVOLUTION_BLUE_BIAS_EXT: Incomplete
GL_POST_CONVOLUTION_BLUE_SCALE_EXT: Incomplete
GL_POST_CONVOLUTION_GREEN_BIAS_EXT: Incomplete
GL_POST_CONVOLUTION_GREEN_SCALE_EXT: Incomplete
GL_POST_CONVOLUTION_RED_BIAS_EXT: Incomplete
GL_POST_CONVOLUTION_RED_SCALE_EXT: Incomplete
GL_REDUCE_EXT: Incomplete
GL_SEPARABLE_2D_EXT: Incomplete

@_f
def glConvolutionFilter1DEXT(target, internalformat, width, format, type, image) -> None: ...
@_f
def glConvolutionFilter2DEXT(target, internalformat, width, height, format, type, image) -> None: ...
@_f
def glConvolutionParameterfEXT(target, pname, params) -> None: ...
@_f
def glConvolutionParameterfvEXT(target, pname, params) -> None: ...
@_f
def glConvolutionParameteriEXT(target, pname, params) -> None: ...
@_f
def glConvolutionParameterivEXT(target, pname, params) -> None: ...
@_f
def glCopyConvolutionFilter1DEXT(target, internalformat, x, y, width) -> None: ...
@_f
def glCopyConvolutionFilter2DEXT(target, internalformat, x, y, width, height) -> None: ...
@_f
def glGetConvolutionFilterEXT(target, format, type, image) -> None: ...
@_f
def glGetConvolutionParameterfvEXT(target, pname, params) -> None: ...
@_f
def glGetConvolutionParameterivEXT(target, pname, params) -> None: ...
@_f
def glGetSeparableFilterEXT(target, format, type, row, column, span) -> None: ...
@_f
def glSeparableFilter2DEXT(target, internalformat, width, height, format, type, row, column) -> None: ...
