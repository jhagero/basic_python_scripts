from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TEXTURE_IMMUTABLE_LEVELS: Incomplete
GL_TEXTURE_VIEW_MIN_LAYER: Incomplete
GL_TEXTURE_VIEW_MIN_LEVEL: Incomplete
GL_TEXTURE_VIEW_NUM_LAYERS: Incomplete
GL_TEXTURE_VIEW_NUM_LEVELS: Incomplete

@_f
def glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers) -> None: ...
