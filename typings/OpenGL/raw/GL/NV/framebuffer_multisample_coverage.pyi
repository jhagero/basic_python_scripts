from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV: Incomplete
GL_MULTISAMPLE_COVERAGE_MODES_NV: Incomplete
GL_RENDERBUFFER_COLOR_SAMPLES_NV: Incomplete
GL_RENDERBUFFER_COVERAGE_SAMPLES_NV: Incomplete

@_f
def glRenderbufferStorageMultisampleCoverageNV(target, coverageSamples, colorSamples, internalformat, width, height) -> None: ...
