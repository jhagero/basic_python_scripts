from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_LAYOUT_DEFAULT_INTEL: Incomplete
GL_LAYOUT_LINEAR_CPU_CACHED_INTEL: Incomplete
GL_LAYOUT_LINEAR_INTEL: Incomplete
GL_TEXTURE_MEMORY_LAYOUT_INTEL: Incomplete

@_f
def glMapTexture2DINTEL(texture, level, access, stride, layout) -> None: ...
@_f
def glSyncTextureINTEL(texture) -> None: ...
@_f
def glUnmapTexture2DINTEL(texture, level) -> None: ...
