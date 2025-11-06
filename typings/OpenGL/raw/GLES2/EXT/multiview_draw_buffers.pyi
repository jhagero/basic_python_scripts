from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ATTACHMENT_EXT: Incomplete
GL_DRAW_BUFFER_EXT: Incomplete
GL_MAX_MULTIVIEW_BUFFERS_EXT: Incomplete
GL_MULTIVIEW_EXT: Incomplete
GL_READ_BUFFER_EXT: Incomplete

@_f
def glDrawBuffersIndexedEXT(n, location, indices) -> None: ...
@_f
def glGetIntegeri_vEXT(target, index, data) -> None: ...
@_f
def glReadBufferIndexedEXT(src, index) -> None: ...
