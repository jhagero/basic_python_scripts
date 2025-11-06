from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CLIPPING_INPUT_PRIMITIVES: Incomplete
GL_CLIPPING_OUTPUT_PRIMITIVES: Incomplete
GL_COMPUTE_SHADER_INVOCATIONS: Incomplete
GL_CONTEXT_FLAG_NO_ERROR_BIT: Incomplete
GL_CONTEXT_RELEASE_BEHAVIOR: Incomplete
GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH: Incomplete
GL_FRAGMENT_SHADER_INVOCATIONS: Incomplete
GL_GEOMETRY_SHADER_INVOCATIONS: Incomplete
GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED: Incomplete
GL_MAX_TEXTURE_MAX_ANISOTROPY: Incomplete
GL_NONE: Incomplete
GL_NUM_SPIR_V_EXTENSIONS: Incomplete
GL_PARAMETER_BUFFER: Incomplete
GL_PARAMETER_BUFFER_BINDING: Incomplete
GL_POLYGON_OFFSET_CLAMP: Incomplete
GL_PRIMITIVES_SUBMITTED: Incomplete
GL_SHADER_BINARY_FORMAT_SPIR_V: Incomplete
GL_SPIR_V_BINARY: Incomplete
GL_SPIR_V_EXTENSIONS: Incomplete
GL_TESS_CONTROL_SHADER_PATCHES: Incomplete
GL_TESS_EVALUATION_SHADER_INVOCATIONS: Incomplete
GL_TEXTURE_MAX_ANISOTROPY: Incomplete
GL_TRANSFORM_FEEDBACK_OVERFLOW: Incomplete
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW: Incomplete
GL_VERTEX_SHADER_INVOCATIONS: Incomplete
GL_VERTICES_SUBMITTED: Incomplete

@_f
def glMultiDrawArraysIndirectCount(mode, indirect, drawcount, maxdrawcount, stride) -> None: ...
@_f
def glMultiDrawElementsIndirectCount(mode, type, indirect, drawcount, maxdrawcount, stride) -> None: ...
@_f
def glPolygonOffsetClamp(factor, units, clamp) -> None: ...
@_f
def glSpecializeShader(shader, pEntryPoint, numSpecializationConstants, pConstantIndex, pConstantValue) -> None: ...
