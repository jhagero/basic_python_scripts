from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DRAW_FRAMEBUFFER_APPLE: Incomplete
GL_DRAW_FRAMEBUFFER_BINDING_APPLE: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_APPLE: Incomplete
GL_MAX_SAMPLES_APPLE: Incomplete
GL_READ_FRAMEBUFFER_APPLE: Incomplete
GL_READ_FRAMEBUFFER_BINDING_APPLE: Incomplete
GL_RENDERBUFFER_SAMPLES_APPLE: Incomplete

@_f
def glRenderbufferStorageMultisampleAPPLE(target, samples, internalformat, width, height) -> None: ...
@_f
def glResolveMultisampleFramebufferAPPLE() -> None: ...
