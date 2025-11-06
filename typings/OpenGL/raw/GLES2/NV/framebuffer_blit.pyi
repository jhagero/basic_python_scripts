from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DRAW_FRAMEBUFFER_BINDING_NV: Incomplete
GL_DRAW_FRAMEBUFFER_NV: Incomplete
GL_READ_FRAMEBUFFER_BINDING_NV: Incomplete
GL_READ_FRAMEBUFFER_NV: Incomplete

@_f
def glBlitFramebufferNV(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
