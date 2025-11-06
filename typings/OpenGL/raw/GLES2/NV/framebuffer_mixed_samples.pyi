from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_SAMPLES_NV: Incomplete
GL_COVERAGE_MODULATION_NV: Incomplete
GL_COVERAGE_MODULATION_TABLE_NV: Incomplete
GL_COVERAGE_MODULATION_TABLE_SIZE_NV: Incomplete
GL_DEPTH_SAMPLES_NV: Incomplete
GL_EFFECTIVE_RASTER_SAMPLES_EXT: Incomplete
GL_MAX_RASTER_SAMPLES_EXT: Incomplete
GL_MIXED_DEPTH_SAMPLES_SUPPORTED_NV: Incomplete
GL_MIXED_STENCIL_SAMPLES_SUPPORTED_NV: Incomplete
GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT: Incomplete
GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT: Incomplete
GL_RASTER_MULTISAMPLE_EXT: Incomplete
GL_RASTER_SAMPLES_EXT: Incomplete
GL_STENCIL_SAMPLES_NV: Incomplete

@_f
def glCoverageModulationNV(components) -> None: ...
@_f
def glCoverageModulationTableNV(n, v) -> None: ...
@_f
def glGetCoverageModulationTableNV(bufSize, v) -> None: ...
@_f
def glRasterSamplesEXT(samples, fixedsamplelocations) -> None: ...
