from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_NV: Incomplete
GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_NV: Incomplete
GL_PROGRAMMABLE_SAMPLE_LOCATION_NV: Incomplete
GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_NV: Incomplete
GL_SAMPLE_LOCATION_NV: Incomplete
GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_NV: Incomplete
GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_NV: Incomplete
GL_SAMPLE_LOCATION_SUBPIXEL_BITS_NV: Incomplete

@_f
def glFramebufferSampleLocationsfvNV(target, start, count, v) -> None: ...
@_f
def glNamedFramebufferSampleLocationsfvNV(framebuffer, start, count, v) -> None: ...
@_f
def glResolveDepthValuesNV() -> None: ...
