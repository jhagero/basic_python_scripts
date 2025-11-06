from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TEXTURE_1D_BINDING_EXT: Incomplete
GL_TEXTURE_2D_BINDING_EXT: Incomplete
GL_TEXTURE_3D_BINDING_EXT: Incomplete
GL_TEXTURE_PRIORITY_EXT: Incomplete
GL_TEXTURE_RESIDENT_EXT: Incomplete

@_f
def glAreTexturesResidentEXT(n, textures, residences) -> None: ...
@_f
def glBindTextureEXT(target, texture) -> None: ...
@_f
def glDeleteTexturesEXT(n, textures) -> None: ...
@_f
def glGenTexturesEXT(n, textures) -> None: ...
@_f
def glIsTextureEXT(texture) -> None: ...
@_f
def glPrioritizeTexturesEXT(n, textures, priorities) -> None: ...
