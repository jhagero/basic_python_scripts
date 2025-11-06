from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_VARYINGS_NV: Incomplete
GL_ACTIVE_VARYING_MAX_LENGTH_NV: Incomplete
GL_BACK_PRIMARY_COLOR_NV: Incomplete
GL_BACK_SECONDARY_COLOR_NV: Incomplete
GL_CLIP_DISTANCE_NV: Incomplete
GL_GENERIC_ATTRIB_NV: Incomplete
GL_INTERLEAVED_ATTRIBS_NV: Incomplete
GL_LAYER_NV: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_NV: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_NV: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_NV: Incomplete
GL_NEXT_BUFFER_NV: Incomplete
GL_PRIMITIVES_GENERATED_NV: Incomplete
GL_PRIMITIVE_ID_NV: Incomplete
GL_RASTERIZER_DISCARD_NV: Incomplete
GL_SEPARATE_ATTRIBS_NV: Incomplete
GL_SKIP_COMPONENTS1_NV: Incomplete
GL_SKIP_COMPONENTS2_NV: Incomplete
GL_SKIP_COMPONENTS3_NV: Incomplete
GL_SKIP_COMPONENTS4_NV: Incomplete
GL_TEXTURE_COORD_NV: Incomplete
GL_TRANSFORM_FEEDBACK_ATTRIBS_NV: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_NV: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_NV: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_NV: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_NV: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_START_NV: Incomplete
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_NV: Incomplete
GL_TRANSFORM_FEEDBACK_RECORD_NV: Incomplete
GL_TRANSFORM_FEEDBACK_VARYINGS_NV: Incomplete
GL_VERTEX_ID_NV: Incomplete

@_f
def glActiveVaryingNV(program, name) -> None: ...
@_f
def glBeginTransformFeedbackNV(primitiveMode) -> None: ...
@_f
def glBindBufferBaseNV(target, index, buffer) -> None: ...
@_f
def glBindBufferOffsetNV(target, index, buffer, offset) -> None: ...
@_f
def glBindBufferRangeNV(target, index, buffer, offset, size) -> None: ...
@_f
def glEndTransformFeedbackNV() -> None: ...
@_f
def glGetActiveVaryingNV(program, index, bufSize, length, size, type, name) -> None: ...
@_f
def glGetTransformFeedbackVaryingNV(program, index, location) -> None: ...
@_f
def glGetVaryingLocationNV(program, name) -> None: ...
@_f
def glTransformFeedbackAttribsNV(count, attribs, bufferMode) -> None: ...
@_f
def glTransformFeedbackStreamAttribsNV(count, attribs, nbuffers, bufstreams, bufferMode) -> None: ...
@_f
def glTransformFeedbackVaryingsNV(program, count, locations, bufferMode) -> None: ...
