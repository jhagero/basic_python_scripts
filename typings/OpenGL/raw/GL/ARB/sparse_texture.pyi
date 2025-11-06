from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB: Incomplete
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB: Incomplete
GL_MAX_SPARSE_TEXTURE_SIZE_ARB: Incomplete
GL_NUM_SPARSE_LEVELS_ARB: Incomplete
GL_NUM_VIRTUAL_PAGE_SIZES_ARB: Incomplete
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB: Incomplete
GL_TEXTURE_SPARSE_ARB: Incomplete
GL_VIRTUAL_PAGE_SIZE_INDEX_ARB: Incomplete
GL_VIRTUAL_PAGE_SIZE_X_ARB: Incomplete
GL_VIRTUAL_PAGE_SIZE_Y_ARB: Incomplete
GL_VIRTUAL_PAGE_SIZE_Z_ARB: Incomplete

@_f
def glTexPageCommitmentARB(target, level, xoffset, yoffset, zoffset, width, height, depth, commit) -> None: ...
