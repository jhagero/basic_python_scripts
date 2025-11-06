from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FIXED: Incomplete
GL_HIGH_FLOAT: Incomplete
GL_HIGH_INT: Incomplete
GL_IMPLEMENTATION_COLOR_READ_FORMAT: Incomplete
GL_IMPLEMENTATION_COLOR_READ_TYPE: Incomplete
GL_LOW_FLOAT: Incomplete
GL_LOW_INT: Incomplete
GL_MAX_FRAGMENT_UNIFORM_VECTORS: Incomplete
GL_MAX_VARYING_VECTORS: Incomplete
GL_MAX_VERTEX_UNIFORM_VECTORS: Incomplete
GL_MEDIUM_FLOAT: Incomplete
GL_MEDIUM_INT: Incomplete
GL_NUM_SHADER_BINARY_FORMATS: Incomplete
GL_RGB565: Incomplete
GL_SHADER_BINARY_FORMATS: Incomplete
GL_SHADER_COMPILER: Incomplete

@_f
def glClearDepthf(d) -> None: ...
@_f
def glDepthRangef(n, f) -> None: ...
@_f
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision) -> None: ...
@_f
def glReleaseShaderCompiler() -> None: ...
@_f
def glShaderBinary(count, shaders, binaryFormat, binary, length) -> None: ...
