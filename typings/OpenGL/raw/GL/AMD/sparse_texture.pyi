from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_SPARSE_3D_TEXTURE_SIZE_AMD: Incomplete
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS: Incomplete
GL_MAX_SPARSE_TEXTURE_SIZE_AMD: Incomplete
GL_MIN_LOD_WARNING_AMD: Incomplete
GL_MIN_SPARSE_LEVEL_AMD: Incomplete
GL_TEXTURE_STORAGE_SPARSE_BIT_AMD: Incomplete
GL_VIRTUAL_PAGE_SIZE_X_AMD: Incomplete
GL_VIRTUAL_PAGE_SIZE_Y_AMD: Incomplete
GL_VIRTUAL_PAGE_SIZE_Z_AMD: Incomplete

@_f
def glTexStorageSparseAMD(target, internalFormat, width, height, depth, layers, flags) -> None: ...
@_f
def glTextureStorageSparseAMD(texture, target, internalFormat, width, height, depth, layers, flags) -> None: ...
