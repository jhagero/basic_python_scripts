from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DRAW_FRAMEBUFFER_BINDING_EXT: Incomplete
GL_DRAW_FRAMEBUFFER_EXT: Incomplete
GL_READ_FRAMEBUFFER_BINDING_EXT: Incomplete
GL_READ_FRAMEBUFFER_EXT: Incomplete

@_f
def glBlitFramebufferEXT(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
