from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALL_PIXELS_AMD: Incomplete
GL_PIXELS_PER_SAMPLE_PATTERN_X_AMD: Incomplete
GL_PIXELS_PER_SAMPLE_PATTERN_Y_AMD: Incomplete
GL_SUBSAMPLE_DISTANCE_AMD: Incomplete

@_f
def glFramebufferSamplePositionsfvAMD(target, numsamples, pixelindex, values) -> None: ...
@_f
def glGetFramebufferParameterfvAMD(target, pname, numsamples, pixelindex, size, values) -> None: ...
@_f
def glGetNamedFramebufferParameterfvAMD(framebuffer, pname, numsamples, pixelindex, size, values) -> None: ...
@_f
def glNamedFramebufferSamplePositionsfvAMD(framebuffer, numsamples, pixelindex, values) -> None: ...
