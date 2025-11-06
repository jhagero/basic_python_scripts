from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_BINDABLE_UNIFORM_SIZE_EXT: Incomplete
GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT: Incomplete
GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT: Incomplete
GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT: Incomplete
GL_UNIFORM_BUFFER_BINDING_EXT: Incomplete
GL_UNIFORM_BUFFER_EXT: Incomplete

@_f
def glGetUniformBufferSizeEXT(program, location) -> None: ...
@_f
def glGetUniformOffsetEXT(program, location) -> None: ...
@_f
def glUniformBufferEXT(program, location, buffer) -> None: ...
