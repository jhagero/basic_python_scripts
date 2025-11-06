from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_INTERLEAVED_ATTRIBS_EXT: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT: Incomplete
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT: Incomplete
GL_PRIMITIVES_GENERATED_EXT: Incomplete
GL_RASTERIZER_DISCARD_EXT: Incomplete
GL_SEPARATE_ATTRIBS_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_VARYINGS_EXT: Incomplete
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT: Incomplete

@_f
def glBeginTransformFeedbackEXT(primitiveMode) -> None: ...
@_f
def glBindBufferBaseEXT(target, index, buffer) -> None: ...
@_f
def glBindBufferOffsetEXT(target, index, buffer, offset) -> None: ...
@_f
def glBindBufferRangeEXT(target, index, buffer, offset, size) -> None: ...
@_f
def glEndTransformFeedbackEXT() -> None: ...
@_f
def glGetTransformFeedbackVaryingEXT(program, index, bufSize, length, size, type, name) -> None: ...
@_f
def glTransformFeedbackVaryingsEXT(program, count, varyings, bufferMode) -> None: ...
