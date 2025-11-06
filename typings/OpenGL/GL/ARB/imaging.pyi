from OpenGL.raw.GL.ARB.imaging import *
from OpenGL import arrays as arrays, constant as constant, extensions as extensions, platform as platform, wrapper as wrapper
from OpenGL.GL import images as images
from _typeshed import Incomplete

def glInitImagingARB(): ...

glColorTable: Incomplete
glColorTableParameterfv: Incomplete
glColorTableParameteriv: Incomplete
glGetColorTableParameterfv: Incomplete
glGetColorTableParameteriv: Incomplete
glColorSubTable: Incomplete
glConvolutionFilter1D: Incomplete
glConvolutionFilter2D: Incomplete
glConvolutionParameterfv: Incomplete
glConvolutionParameteriv: Incomplete
glGetConvolutionParameterfv: Incomplete
glGetConvolutionParameteriv: Incomplete
glSeparableFilter2D: Incomplete
glGetHistogramParameterfv: Incomplete
glGetHistogramParameteriv: Incomplete
glGetMinmaxParameterfv: Incomplete
glGetMinmaxParameteriv: Incomplete

def glGetConvolutionFilter(baseFunction, target, format, type): ...
def glGetSeparableFilter(baseFunction, target, format, type): ...
def glGetColorTable(baseFunction, target, format, type): ...
def glGetHistogram(baseFunction, target, reset, format, type, values=None): ...
def glGetMinmax(baseFunction, target, reset, format, type, values=None): ...
