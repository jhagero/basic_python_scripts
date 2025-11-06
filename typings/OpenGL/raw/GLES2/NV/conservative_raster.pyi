from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONSERVATIVE_RASTERIZATION_NV: Incomplete
GL_MAX_SUBPIXEL_PRECISION_BIAS_BITS_NV: Incomplete
GL_SUBPIXEL_PRECISION_BIAS_X_BITS_NV: Incomplete
GL_SUBPIXEL_PRECISION_BIAS_Y_BITS_NV: Incomplete

@_f
def glSubpixelPrecisionBiasNV(xbits, ybits) -> None: ...
