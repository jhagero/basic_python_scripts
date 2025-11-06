from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT: Incomplete
GL_MAX_ARRAY_TEXTURE_LAYERS_EXT: Incomplete
GL_PROXY_TEXTURE_1D_ARRAY_EXT: Incomplete
GL_PROXY_TEXTURE_2D_ARRAY_EXT: Incomplete
GL_TEXTURE_1D_ARRAY_EXT: Incomplete
GL_TEXTURE_2D_ARRAY_EXT: Incomplete
GL_TEXTURE_BINDING_1D_ARRAY_EXT: Incomplete
GL_TEXTURE_BINDING_2D_ARRAY_EXT: Incomplete

@_f
def glFramebufferTextureLayerEXT(target, attachment, texture, level, layer) -> None: ...
