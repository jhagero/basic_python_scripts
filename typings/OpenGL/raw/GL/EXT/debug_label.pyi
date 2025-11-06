from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_OBJECT_EXT: Incomplete
GL_PROGRAM_OBJECT_EXT: Incomplete
GL_PROGRAM_PIPELINE_OBJECT_EXT: Incomplete
GL_QUERY_OBJECT_EXT: Incomplete
GL_SAMPLER: Incomplete
GL_SHADER_OBJECT_EXT: Incomplete
GL_TRANSFORM_FEEDBACK: Incomplete
GL_VERTEX_ARRAY_OBJECT_EXT: Incomplete

@_f
def glGetObjectLabelEXT(type, object, bufSize, length, label) -> None: ...
@_f
def glLabelObjectEXT(type, object, length, label) -> None: ...
