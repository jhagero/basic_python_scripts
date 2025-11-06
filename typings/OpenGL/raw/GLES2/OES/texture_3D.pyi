from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_OES: Incomplete
GL_MAX_3D_TEXTURE_SIZE_OES: Incomplete
GL_SAMPLER_3D_OES: Incomplete
GL_TEXTURE_3D_OES: Incomplete
GL_TEXTURE_BINDING_3D_OES: Incomplete
GL_TEXTURE_WRAP_R_OES: Incomplete

@_f
def glCompressedTexImage3DOES(target, level, internalformat, width, height, depth, border, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data) -> None: ...
@_f
def glCopyTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, x, y, width, height) -> None: ...
@_f
def glFramebufferTexture3DOES(target, attachment, textarget, texture, level, zoffset) -> None: ...
@_f
def glTexImage3DOES(target, level, internalformat, width, height, depth, border, format, type, pixels) -> None: ...
@_f
def glTexSubImage3DOES(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels) -> None: ...
