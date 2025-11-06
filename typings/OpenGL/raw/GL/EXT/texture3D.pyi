from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_3D_TEXTURE_SIZE_EXT: Incomplete
GL_PACK_IMAGE_HEIGHT_EXT: Incomplete
GL_PACK_SKIP_IMAGES_EXT: Incomplete
GL_PROXY_TEXTURE_3D_EXT: Incomplete
GL_TEXTURE_3D_EXT: Incomplete
GL_TEXTURE_DEPTH_EXT: Incomplete
GL_TEXTURE_WRAP_R_EXT: Incomplete
GL_UNPACK_IMAGE_HEIGHT_EXT: Incomplete
GL_UNPACK_SKIP_IMAGES_EXT: Incomplete

@_f
def glTexImage3DEXT(target, level, internalformat, width, height, depth, border, format, type, pixels) -> None: ...
@_f
def glTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels) -> None: ...
