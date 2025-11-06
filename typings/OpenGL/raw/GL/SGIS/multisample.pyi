from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_1PASS_SGIS: Incomplete
GL_2PASS_0_SGIS: Incomplete
GL_2PASS_1_SGIS: Incomplete
GL_4PASS_0_SGIS: Incomplete
GL_4PASS_1_SGIS: Incomplete
GL_4PASS_2_SGIS: Incomplete
GL_4PASS_3_SGIS: Incomplete
GL_MULTISAMPLE_SGIS: Incomplete
GL_SAMPLES_SGIS: Incomplete
GL_SAMPLE_ALPHA_TO_MASK_SGIS: Incomplete
GL_SAMPLE_ALPHA_TO_ONE_SGIS: Incomplete
GL_SAMPLE_BUFFERS_SGIS: Incomplete
GL_SAMPLE_MASK_INVERT_SGIS: Incomplete
GL_SAMPLE_MASK_SGIS: Incomplete
GL_SAMPLE_MASK_VALUE_SGIS: Incomplete
GL_SAMPLE_PATTERN_SGIS: Incomplete

@_f
def glSampleMaskSGIS(value, invert) -> None: ...
@_f
def glSamplePatternSGIS(pattern) -> None: ...
