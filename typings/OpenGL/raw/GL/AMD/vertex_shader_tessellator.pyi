from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONTINUOUS_AMD: Incomplete
GL_DISCRETE_AMD: Incomplete
GL_INT_SAMPLER_BUFFER_AMD: Incomplete
GL_SAMPLER_BUFFER_AMD: Incomplete
GL_TESSELLATION_FACTOR_AMD: Incomplete
GL_TESSELLATION_MODE_AMD: Incomplete
GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD: Incomplete

@_f
def glTessellationFactorAMD(factor) -> None: ...
@_f
def glTessellationModeAMD(mode) -> None: ...
