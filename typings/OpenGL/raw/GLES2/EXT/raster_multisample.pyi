from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_EFFECTIVE_RASTER_SAMPLES_EXT: Incomplete
GL_MAX_RASTER_SAMPLES_EXT: Incomplete
GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT: Incomplete
GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT: Incomplete
GL_RASTER_MULTISAMPLE_EXT: Incomplete
GL_RASTER_SAMPLES_EXT: Incomplete

@_f
def glRasterSamplesEXT(samples, fixedsamplelocations) -> None: ...
