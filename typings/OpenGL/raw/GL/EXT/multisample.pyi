from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_1PASS_EXT: Incomplete
GL_2PASS_0_EXT: Incomplete
GL_2PASS_1_EXT: Incomplete
GL_4PASS_0_EXT: Incomplete
GL_4PASS_1_EXT: Incomplete
GL_4PASS_2_EXT: Incomplete
GL_4PASS_3_EXT: Incomplete
GL_MULTISAMPLE_BIT_EXT: Incomplete
GL_MULTISAMPLE_EXT: Incomplete
GL_SAMPLES_EXT: Incomplete
GL_SAMPLE_ALPHA_TO_MASK_EXT: Incomplete
GL_SAMPLE_ALPHA_TO_ONE_EXT: Incomplete
GL_SAMPLE_BUFFERS_EXT: Incomplete
GL_SAMPLE_MASK_EXT: Incomplete
GL_SAMPLE_MASK_INVERT_EXT: Incomplete
GL_SAMPLE_MASK_VALUE_EXT: Incomplete
GL_SAMPLE_PATTERN_EXT: Incomplete

@_f
def glSampleMaskEXT(value, invert) -> None: ...
@_f
def glSamplePatternEXT(pattern) -> None: ...
