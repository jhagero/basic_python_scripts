from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_NV: Incomplete
GL_MAX_SAMPLES_NV: Incomplete
GL_RENDERBUFFER_SAMPLES_NV: Incomplete

@_f
def glRenderbufferStorageMultisampleNV(target, samples, internalformat, width, height) -> None: ...
