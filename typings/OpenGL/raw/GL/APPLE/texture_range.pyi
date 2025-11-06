from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_STORAGE_CACHED_APPLE: Incomplete
GL_STORAGE_PRIVATE_APPLE: Incomplete
GL_STORAGE_SHARED_APPLE: Incomplete
GL_TEXTURE_RANGE_LENGTH_APPLE: Incomplete
GL_TEXTURE_RANGE_POINTER_APPLE: Incomplete
GL_TEXTURE_STORAGE_HINT_APPLE: Incomplete

@_f
def glGetTexParameterPointervAPPLE(target, pname, params) -> None: ...
@_f
def glTextureRangeAPPLE(target, length, pointer) -> None: ...
