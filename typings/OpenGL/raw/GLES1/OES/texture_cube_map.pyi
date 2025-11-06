from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES: Incomplete
GL_NORMAL_MAP_OES: Incomplete
GL_REFLECTION_MAP_OES: Incomplete
GL_TEXTURE_BINDING_CUBE_MAP_OES: Incomplete
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES: Incomplete
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES: Incomplete
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES: Incomplete
GL_TEXTURE_CUBE_MAP_OES: Incomplete
GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES: Incomplete
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES: Incomplete
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES: Incomplete
GL_TEXTURE_GEN_MODE_OES: Incomplete
GL_TEXTURE_GEN_STR_OES: Incomplete

@_f
def glGetTexGenfvOES(coord, pname, params) -> None: ...
@_f
def glGetTexGenivOES(coord, pname, params) -> None: ...
@_f
def glGetTexGenxvOES(coord, pname, params) -> None: ...
@_f
def glTexGenfOES(coord, pname, param) -> None: ...
@_f
def glTexGenfvOES(coord, pname, params) -> None: ...
@_f
def glTexGeniOES(coord, pname, param) -> None: ...
@_f
def glTexGenivOES(coord, pname, params) -> None: ...
@_f
def glTexGenxOES(coord, pname, param) -> None: ...
@_f
def glTexGenxvOES(coord, pname, params) -> None: ...
