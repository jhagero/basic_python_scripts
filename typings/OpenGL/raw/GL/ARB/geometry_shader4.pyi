from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB: Incomplete
GL_GEOMETRY_INPUT_TYPE_ARB: Incomplete
GL_GEOMETRY_OUTPUT_TYPE_ARB: Incomplete
GL_GEOMETRY_SHADER_ARB: Incomplete
GL_GEOMETRY_VERTICES_OUT_ARB: Incomplete
GL_LINES_ADJACENCY_ARB: Incomplete
GL_LINE_STRIP_ADJACENCY_ARB: Incomplete
GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB: Incomplete
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB: Incomplete
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB: Incomplete
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB: Incomplete
GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB: Incomplete
GL_MAX_VARYING_COMPONENTS: Incomplete
GL_MAX_VERTEX_VARYING_COMPONENTS_ARB: Incomplete
GL_PROGRAM_POINT_SIZE_ARB: Incomplete
GL_TRIANGLES_ADJACENCY_ARB: Incomplete
GL_TRIANGLE_STRIP_ADJACENCY_ARB: Incomplete

@_f
def glFramebufferTextureARB(target, attachment, texture, level) -> None: ...
@_f
def glFramebufferTextureFaceARB(target, attachment, texture, level, face) -> None: ...
@_f
def glFramebufferTextureLayerARB(target, attachment, texture, level, layer) -> None: ...
@_f
def glProgramParameteriARB(program, pname, value) -> None: ...
