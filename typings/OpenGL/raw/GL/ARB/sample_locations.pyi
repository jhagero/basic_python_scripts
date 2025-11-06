from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_ARB: Incomplete
GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_ARB: Incomplete
GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB: Incomplete
GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_ARB: Incomplete
GL_SAMPLE_LOCATION_ARB: Incomplete
GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_ARB: Incomplete
GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_ARB: Incomplete
GL_SAMPLE_LOCATION_SUBPIXEL_BITS_ARB: Incomplete

@_f
def glEvaluateDepthValuesARB() -> None: ...
@_f
def glFramebufferSampleLocationsfvARB(target, start, count, v) -> None: ...
@_f
def glNamedFramebufferSampleLocationsfvARB(framebuffer, start, count, v) -> None: ...
