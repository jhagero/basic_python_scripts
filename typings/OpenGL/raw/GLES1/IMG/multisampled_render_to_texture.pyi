from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG: Incomplete
GL_MAX_SAMPLES_IMG: Incomplete
GL_RENDERBUFFER_SAMPLES_IMG: Incomplete
GL_TEXTURE_SAMPLES_IMG: Incomplete

@_f
def glFramebufferTexture2DMultisampleIMG(target, attachment, textarget, texture, level, samples) -> None: ...
@_f
def glRenderbufferStorageMultisampleIMG(target, samples, internalformat, width, height) -> None: ...
