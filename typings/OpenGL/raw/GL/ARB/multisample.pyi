from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MULTISAMPLE_ARB: Incomplete
GL_MULTISAMPLE_BIT_ARB: Incomplete
GL_SAMPLES_ARB: Incomplete
GL_SAMPLE_ALPHA_TO_COVERAGE_ARB: Incomplete
GL_SAMPLE_ALPHA_TO_ONE_ARB: Incomplete
GL_SAMPLE_BUFFERS_ARB: Incomplete
GL_SAMPLE_COVERAGE_ARB: Incomplete
GL_SAMPLE_COVERAGE_INVERT_ARB: Incomplete
GL_SAMPLE_COVERAGE_VALUE_ARB: Incomplete

@_f
def glSampleCoverageARB(value, invert) -> None: ...
