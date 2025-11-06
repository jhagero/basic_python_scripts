from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_COARSE_FRAGMENT_SAMPLES_NV: Incomplete
GL_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV: Incomplete
GL_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV: Incomplete
GL_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV: Incomplete
GL_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV: Incomplete
GL_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV: Incomplete
GL_SHADING_RATE_IMAGE_BINDING_NV: Incomplete
GL_SHADING_RATE_IMAGE_NV: Incomplete
GL_SHADING_RATE_IMAGE_PALETTE_SIZE_NV: Incomplete
GL_SHADING_RATE_IMAGE_TEXEL_HEIGHT_NV: Incomplete
GL_SHADING_RATE_IMAGE_TEXEL_WIDTH_NV: Incomplete
GL_SHADING_RATE_NO_INVOCATIONS_NV: Incomplete
GL_SHADING_RATE_SAMPLE_ORDER_DEFAULT_NV: Incomplete
GL_SHADING_RATE_SAMPLE_ORDER_PIXEL_MAJOR_NV: Incomplete
GL_SHADING_RATE_SAMPLE_ORDER_SAMPLE_MAJOR_NV: Incomplete

@_f
def glBindShadingRateImageNV(texture) -> None: ...
@_f
def glGetShadingRateImagePaletteNV(viewport, entry, rate) -> None: ...
@_f
def glGetShadingRateSampleLocationivNV(rate, samples, index, location) -> None: ...
@_f
def glShadingRateImageBarrierNV(synchronize) -> None: ...
@_f
def glShadingRateImagePaletteNV(viewport, first, count, rates) -> None: ...
@_f
def glShadingRateSampleOrderCustomNV(rate, samples, locations) -> None: ...
@_f
def glShadingRateSampleOrderNV(order) -> None: ...
