from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_TEXTURE_IMMUTABLE_FORMAT: Incomplete

@_f
def glTexStorage1D(target, levels, internalformat, width) -> None: ...
@_f
def glTexStorage2D(target, levels, internalformat, width, height) -> None: ...
@_f
def glTexStorage3D(target, levels, internalformat, width, height, depth) -> None: ...
