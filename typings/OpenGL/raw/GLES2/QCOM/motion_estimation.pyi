from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FOVEATION_SCALED_BIN_METHOD_BIT_QCOM: Incomplete
GL_MOTION_ESTIMATION_SEARCH_BLOCK_X_QCOM: Incomplete
GL_MOTION_ESTIMATION_SEARCH_BLOCK_Y_QCOM: Incomplete

@_f
def glTexEstimateMotionQCOM(ref, target, output) -> None: ...
@_f
def glTexEstimateMotionRegionsQCOM(ref, target, output, mask) -> None: ...
