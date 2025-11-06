from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_SPARSE_3D_TEXTURE_SIZE_EXT: Incomplete
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_EXT: Incomplete
GL_MAX_SPARSE_TEXTURE_SIZE_EXT: Incomplete
GL_NUM_SPARSE_LEVELS_EXT: Incomplete
GL_NUM_VIRTUAL_PAGE_SIZES_EXT: Incomplete
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_EXT: Incomplete
GL_TEXTURE_2D: Incomplete
GL_TEXTURE_2D_ARRAY: Incomplete
GL_TEXTURE_3D: Incomplete
GL_TEXTURE_CUBE_MAP: Incomplete
GL_TEXTURE_CUBE_MAP_ARRAY_OES: Incomplete
GL_TEXTURE_SPARSE_EXT: Incomplete
GL_VIRTUAL_PAGE_SIZE_INDEX_EXT: Incomplete
GL_VIRTUAL_PAGE_SIZE_X_EXT: Incomplete
GL_VIRTUAL_PAGE_SIZE_Y_EXT: Incomplete
GL_VIRTUAL_PAGE_SIZE_Z_EXT: Incomplete

@_f
def glTexPageCommitmentEXT(target, level, xoffset, yoffset, zoffset, width, height, depth, commit) -> None: ...
