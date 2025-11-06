from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COMPRESSED_ALPHA_ARB: Incomplete
GL_COMPRESSED_INTENSITY_ARB: Incomplete
GL_COMPRESSED_LUMINANCE_ALPHA_ARB: Incomplete
GL_COMPRESSED_LUMINANCE_ARB: Incomplete
GL_COMPRESSED_RGBA_ARB: Incomplete
GL_COMPRESSED_RGB_ARB: Incomplete
GL_COMPRESSED_TEXTURE_FORMATS_ARB: Incomplete
GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB: Incomplete
GL_TEXTURE_COMPRESSED_ARB: Incomplete
GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB: Incomplete
GL_TEXTURE_COMPRESSION_HINT_ARB: Incomplete

@_f
def glCompressedTexImage1DARB(target, level, internalformat, width, border, imageSize, data) -> None: ...
@_f
def glCompressedTexImage2DARB(target, level, internalformat, width, height, border, imageSize, data) -> None: ...
@_f
def glCompressedTexImage3DARB(target, level, internalformat, width, height, depth, border, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage1DARB(target, level, xoffset, width, format, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage2DARB(target, level, xoffset, yoffset, width, height, format, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage3DARB(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data) -> None: ...
@_f
def glGetCompressedTexImageARB(target, level, img) -> None: ...
