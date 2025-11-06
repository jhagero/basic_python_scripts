from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALPHA16F_EXT: Incomplete
GL_ALPHA32F_EXT: Incomplete
GL_ALPHA8_EXT: Incomplete
GL_BGRA8_EXT: Incomplete
GL_LUMINANCE16F_EXT: Incomplete
GL_LUMINANCE32F_EXT: Incomplete
GL_LUMINANCE8_ALPHA8_EXT: Incomplete
GL_LUMINANCE8_EXT: Incomplete
GL_LUMINANCE_ALPHA16F_EXT: Incomplete
GL_LUMINANCE_ALPHA32F_EXT: Incomplete
GL_R16F_EXT: Incomplete
GL_R32F_EXT: Incomplete
GL_R8_EXT: Incomplete
GL_RG16F_EXT: Incomplete
GL_RG32F_EXT: Incomplete
GL_RG8_EXT: Incomplete
GL_RGB10_A2_EXT: Incomplete
GL_RGB10_EXT: Incomplete
GL_RGB16F_EXT: Incomplete
GL_RGB32F_EXT: Incomplete
GL_RGBA16F_EXT: Incomplete
GL_RGBA32F_EXT: Incomplete
GL_TEXTURE_IMMUTABLE_FORMAT_EXT: Incomplete

@_f
def glTexStorage1DEXT(target, levels, internalformat, width) -> None: ...
@_f
def glTexStorage2DEXT(target, levels, internalformat, width, height) -> None: ...
@_f
def glTexStorage3DEXT(target, levels, internalformat, width, height, depth) -> None: ...
@_f
def glTextureStorage1DEXT(texture, target, levels, internalformat, width) -> None: ...
@_f
def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height) -> None: ...
@_f
def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth) -> None: ...
