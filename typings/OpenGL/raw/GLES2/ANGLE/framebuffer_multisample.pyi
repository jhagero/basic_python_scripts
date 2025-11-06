from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_ANGLE: Incomplete
GL_MAX_SAMPLES_ANGLE: Incomplete
GL_RENDERBUFFER_SAMPLES_ANGLE: Incomplete

@_f
def glRenderbufferStorageMultisampleANGLE(target, samples, internalformat, width, height) -> None: ...
