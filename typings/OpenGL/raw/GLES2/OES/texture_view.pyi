from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TEXTURE_IMMUTABLE_LEVELS: Incomplete
GL_TEXTURE_VIEW_MIN_LAYER_OES: Incomplete
GL_TEXTURE_VIEW_MIN_LEVEL_OES: Incomplete
GL_TEXTURE_VIEW_NUM_LAYERS_OES: Incomplete
GL_TEXTURE_VIEW_NUM_LEVELS_OES: Incomplete

@_f
def glTextureViewOES(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers) -> None: ...
