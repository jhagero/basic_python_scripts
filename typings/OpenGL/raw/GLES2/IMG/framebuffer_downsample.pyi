from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DOWNSAMPLE_SCALES_IMG: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SCALE_IMG: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_AND_DOWNSAMPLE_IMG: Incomplete
GL_NUM_DOWNSAMPLE_SCALES_IMG: Incomplete

@_f
def glFramebufferTexture2DDownsampleIMG(target, attachment, textarget, texture, level, xscale, yscale) -> None: ...
@_f
def glFramebufferTextureLayerDownsampleIMG(target, attachment, texture, level, layer, xscale, yscale) -> None: ...
