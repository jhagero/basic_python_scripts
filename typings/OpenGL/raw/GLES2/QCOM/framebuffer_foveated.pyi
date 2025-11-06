from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FOVEATION_ENABLE_BIT_QCOM: Incomplete
GL_FOVEATION_SCALED_BIN_METHOD_BIT_QCOM: Incomplete

@_f
def glFramebufferFoveationConfigQCOM(framebuffer, numLayers, focalPointsPerLayer, requestedFeatures, providedFeatures) -> None: ...
@_f
def glFramebufferFoveationParametersQCOM(framebuffer, layer, focalPoint, focalX, focalY, gainX, gainY, foveaArea) -> None: ...
