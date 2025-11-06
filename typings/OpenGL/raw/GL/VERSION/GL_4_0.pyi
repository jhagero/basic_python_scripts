from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_SUBROUTINES: Incomplete
GL_ACTIVE_SUBROUTINE_MAX_LENGTH: Incomplete
GL_ACTIVE_SUBROUTINE_UNIFORMS: Incomplete
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS: Incomplete
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH: Incomplete
GL_COMPATIBLE_SUBROUTINES: Incomplete
GL_DOUBLE_MAT2: Incomplete
GL_DOUBLE_MAT2x3: Incomplete
GL_DOUBLE_MAT2x4: Incomplete
GL_DOUBLE_MAT3: Incomplete
GL_DOUBLE_MAT3x2: Incomplete
GL_DOUBLE_MAT3x4: Incomplete
GL_DOUBLE_MAT4: Incomplete
GL_DOUBLE_MAT4x2: Incomplete
GL_DOUBLE_MAT4x3: Incomplete
GL_DOUBLE_VEC2: Incomplete
GL_DOUBLE_VEC3: Incomplete
GL_DOUBLE_VEC4: Incomplete
GL_DRAW_INDIRECT_BUFFER: Incomplete
GL_DRAW_INDIRECT_BUFFER_BINDING: Incomplete
GL_FRACTIONAL_EVEN: Incomplete
GL_FRACTIONAL_ODD: Incomplete
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS: Incomplete
GL_GEOMETRY_SHADER_INVOCATIONS: Incomplete
GL_INT_SAMPLER_CUBE_MAP_ARRAY: Incomplete
GL_ISOLINES: Incomplete
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS: Incomplete
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS: Incomplete
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET: Incomplete
GL_MAX_GEOMETRY_SHADER_INVOCATIONS: Incomplete
GL_MAX_PATCH_VERTICES: Incomplete
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET: Incomplete
GL_MAX_SUBROUTINES: Incomplete
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS: Incomplete
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS: Incomplete
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS: Incomplete
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS: Incomplete
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS: Incomplete
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS: Incomplete
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS: Incomplete
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS: Incomplete
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS: Incomplete
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS: Incomplete
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS: Incomplete
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS: Incomplete
GL_MAX_TESS_GEN_LEVEL: Incomplete
GL_MAX_TESS_PATCH_COMPONENTS: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS: Incomplete
GL_MAX_VERTEX_STREAMS: Incomplete
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET: Incomplete
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET: Incomplete
GL_MIN_SAMPLE_SHADING_VALUE: Incomplete
GL_NUM_COMPATIBLE_SUBROUTINES: Incomplete
GL_PATCHES: Incomplete
GL_PATCH_DEFAULT_INNER_LEVEL: Incomplete
GL_PATCH_DEFAULT_OUTER_LEVEL: Incomplete
GL_PATCH_VERTICES: Incomplete
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY: Incomplete
GL_QUADS: Incomplete
GL_SAMPLER_CUBE_MAP_ARRAY: Incomplete
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW: Incomplete
GL_SAMPLE_SHADING: Incomplete
GL_TESS_CONTROL_OUTPUT_VERTICES: Incomplete
GL_TESS_CONTROL_SHADER: Incomplete
GL_TESS_EVALUATION_SHADER: Incomplete
GL_TESS_GEN_MODE: Incomplete
GL_TESS_GEN_POINT_MODE: Incomplete
GL_TESS_GEN_SPACING: Incomplete
GL_TESS_GEN_VERTEX_ORDER: Incomplete
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY: Incomplete
GL_TEXTURE_CUBE_MAP_ARRAY: Incomplete
GL_TRANSFORM_FEEDBACK: Incomplete
GL_TRANSFORM_FEEDBACK_BINDING: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED: Incomplete
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER: Incomplete
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER: Incomplete
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY: Incomplete

@_f
def glBeginQueryIndexed(target, index, id) -> None: ...
@_f
def glBindTransformFeedback(target, id) -> None: ...
@_f
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha) -> None: ...
@_f
def glBlendEquationi(buf, mode) -> None: ...
@_f
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha) -> None: ...
@_f
def glBlendFunci(buf, src, dst) -> None: ...
@_f
def glDeleteTransformFeedbacks(n, ids) -> None: ...
@_f
def glDrawArraysIndirect(mode, indirect) -> None: ...
@_f
def glDrawElementsIndirect(mode, type, indirect) -> None: ...
@_f
def glDrawTransformFeedback(mode, id) -> None: ...
@_f
def glDrawTransformFeedbackStream(mode, id, stream) -> None: ...
@_f
def glEndQueryIndexed(target, index) -> None: ...
@_f
def glGenTransformFeedbacks(n, ids) -> None: ...
@_f
def glGetActiveSubroutineName(program, shadertype, index, bufSize, length, name) -> None: ...
@_f
def glGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name) -> None: ...
@_f
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values) -> None: ...
@_f
def glGetProgramStageiv(program, shadertype, pname, values) -> None: ...
@_f
def glGetQueryIndexediv(target, index, pname, params) -> None: ...
@_f
def glGetSubroutineIndex(program, shadertype, name) -> None: ...
@_f
def glGetSubroutineUniformLocation(program, shadertype, name) -> None: ...
@_f
def glGetUniformSubroutineuiv(shadertype, location, params) -> None: ...
@_f
def glGetUniformdv(program, location, params) -> None: ...
@_f
def glIsTransformFeedback(id) -> None: ...
@_f
def glMinSampleShading(value) -> None: ...
@_f
def glPatchParameterfv(pname, values) -> None: ...
@_f
def glPatchParameteri(pname, value) -> None: ...
@_f
def glPauseTransformFeedback() -> None: ...
@_f
def glResumeTransformFeedback() -> None: ...
@_f
def glUniform1d(location, x) -> None: ...
@_f
def glUniform1dv(location, count, value) -> None: ...
@_f
def glUniform2d(location, x, y) -> None: ...
@_f
def glUniform2dv(location, count, value) -> None: ...
@_f
def glUniform3d(location, x, y, z) -> None: ...
@_f
def glUniform3dv(location, count, value) -> None: ...
@_f
def glUniform4d(location, x, y, z, w) -> None: ...
@_f
def glUniform4dv(location, count, value) -> None: ...
@_f
def glUniformMatrix2dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix2x3dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix2x4dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3x2dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3x4dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4x2dv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4x3dv(location, count, transpose, value) -> None: ...
@_f
def glUniformSubroutinesuiv(shadertype, count, indices) -> None: ...
