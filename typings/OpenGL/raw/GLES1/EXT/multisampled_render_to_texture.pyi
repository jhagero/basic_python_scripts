from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT: Incomplete
GL_MAX_SAMPLES_EXT: Incomplete
GL_RENDERBUFFER_SAMPLES_EXT: Incomplete

@_f
def glFramebufferTexture2DMultisampleEXT(target, attachment, textarget, texture, level, samples) -> None: ...
@_f
def glRenderbufferStorageMultisampleEXT(target, samples, internalformat, width, height) -> None: ...
