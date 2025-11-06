from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_EXT: Incomplete
GL_DEPTH_EXT: Incomplete
GL_STENCIL_EXT: Incomplete

@_f
def glDiscardFramebufferEXT(target, numAttachments, attachments) -> None: ...
