from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT: Incomplete
GL_GEOMETRY_INPUT_TYPE_EXT: Incomplete
GL_GEOMETRY_OUTPUT_TYPE_EXT: Incomplete
GL_GEOMETRY_PROGRAM_NV: Incomplete
GL_GEOMETRY_VERTICES_OUT_EXT: Incomplete
GL_LINES_ADJACENCY_EXT: Incomplete
GL_LINE_STRIP_ADJACENCY_EXT: Incomplete
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT: Incomplete
GL_MAX_PROGRAM_OUTPUT_VERTICES_NV: Incomplete
GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV: Incomplete
GL_PROGRAM_POINT_SIZE_EXT: Incomplete
GL_TRIANGLES_ADJACENCY_EXT: Incomplete
GL_TRIANGLE_STRIP_ADJACENCY_EXT: Incomplete

@_f
def glFramebufferTextureEXT(target, attachment, texture, level) -> None: ...
@_f
def glFramebufferTextureFaceEXT(target, attachment, texture, level, face) -> None: ...
@_f
def glFramebufferTextureLayerEXT(target, attachment, texture, level, layer) -> None: ...
@_f
def glProgramVertexLimitNV(target, limit) -> None: ...
