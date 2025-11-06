from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_4D_TEXTURE_SIZE_SGIS: Incomplete
GL_PACK_IMAGE_DEPTH_SGIS: Incomplete
GL_PACK_SKIP_VOLUMES_SGIS: Incomplete
GL_PROXY_TEXTURE_4D_SGIS: Incomplete
GL_TEXTURE_4DSIZE_SGIS: Incomplete
GL_TEXTURE_4D_BINDING_SGIS: Incomplete
GL_TEXTURE_4D_SGIS: Incomplete
GL_TEXTURE_WRAP_Q_SGIS: Incomplete
GL_UNPACK_IMAGE_DEPTH_SGIS: Incomplete
GL_UNPACK_SKIP_VOLUMES_SGIS: Incomplete

@_f
def glTexImage4DSGIS(target, level, internalformat, width, height, depth, size4d, border, format, type, pixels) -> None: ...
@_f
def glTexSubImage4DSGIS(target, level, xoffset, yoffset, zoffset, woffset, width, height, depth, size4d, format, type, pixels) -> None: ...
