from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FOVEATION_ENABLE_BIT_QCOM: Incomplete
GL_FOVEATION_SCALED_BIN_METHOD_BIT_QCOM: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_FOVEATION_QCOM: Incomplete
GL_TEXTURE_FOVEATED_FEATURE_BITS_QCOM: Incomplete
GL_TEXTURE_FOVEATED_FEATURE_QUERY_QCOM: Incomplete
GL_TEXTURE_FOVEATED_MIN_PIXEL_DENSITY_QCOM: Incomplete
GL_TEXTURE_FOVEATED_NUM_FOCAL_POINTS_QUERY_QCOM: Incomplete

@_f
def glTextureFoveationParametersQCOM(texture, layer, focalPoint, focalX, focalY, gainX, gainY, foveaArea) -> None: ...
