from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays

@_f
def glBlitFramebufferLayerEXT(srcX0, srcY0, srcX1, srcY1, srcLayer, dstX0, dstY0, dstX1, dstY1, dstLayer, mask, filter) -> None: ...
@_f
def glBlitFramebufferLayersEXT(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
