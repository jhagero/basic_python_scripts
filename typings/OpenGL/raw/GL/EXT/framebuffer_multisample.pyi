from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT: Incomplete
GL_MAX_SAMPLES_EXT: Incomplete
GL_RENDERBUFFER_SAMPLES_EXT: Incomplete

@_f
def glRenderbufferStorageMultisampleEXT(target, samples, internalformat, width, height) -> None: ...
