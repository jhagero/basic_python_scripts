from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_INCOMPLETE_INSUFFICIENT_SHADER_COMBINED_LOCAL_STORAGE_EXT: Incomplete
GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_FAST_SIZE_EXT: Incomplete
GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_SIZE_EXT: Incomplete

@_f
def glClearPixelLocalStorageuiEXT(offset, n, values) -> None: ...
@_f
def glFramebufferPixelLocalStorageSizeEXT(target, size) -> None: ...
@_f
def glGetFramebufferPixelLocalStorageSizeEXT(target) -> None: ...
