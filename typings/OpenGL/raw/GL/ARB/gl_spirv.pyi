from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_SHADER_BINARY_FORMAT_SPIR_V_ARB: Incomplete
GL_SPIR_V_BINARY_ARB: Incomplete

@_f
def glSpecializeShaderARB(shader, pEntryPoint, numSpecializationConstants, pConstantIndex, pConstantValue) -> None: ...
