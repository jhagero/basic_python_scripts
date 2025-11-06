from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ATTENUATION_EXT: Incomplete
GL_FRAGMENT_COLOR_EXT: Incomplete
GL_FRAGMENT_DEPTH_EXT: Incomplete
GL_FRAGMENT_MATERIAL_EXT: Incomplete
GL_FRAGMENT_NORMAL_EXT: Incomplete
GL_SHADOW_ATTENUATION_EXT: Incomplete
GL_TEXTURE_APPLICATION_MODE_EXT: Incomplete
GL_TEXTURE_LIGHT_EXT: Incomplete
GL_TEXTURE_MATERIAL_FACE_EXT: Incomplete
GL_TEXTURE_MATERIAL_PARAMETER_EXT: Incomplete

@_f
def glApplyTextureEXT(mode) -> None: ...
@_f
def glTextureLightEXT(pname) -> None: ...
@_f
def glTextureMaterialEXT(face, mode) -> None: ...
