from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_COLOR_FRAMEBUFFER_SAMPLES_AMD: Incomplete
GL_MAX_COLOR_FRAMEBUFFER_STORAGE_SAMPLES_AMD: Incomplete
GL_MAX_DEPTH_STENCIL_FRAMEBUFFER_SAMPLES_AMD: Incomplete
GL_NUM_SUPPORTED_MULTISAMPLE_MODES_AMD: Incomplete
GL_RENDERBUFFER_STORAGE_SAMPLES_AMD: Incomplete
GL_SUPPORTED_MULTISAMPLE_MODES_AMD: Incomplete

@_f
def glNamedRenderbufferStorageMultisampleAdvancedAMD(renderbuffer, samples, storageSamples, internalformat, width, height) -> None: ...
@_f
def glRenderbufferStorageMultisampleAdvancedAMD(target, samples, storageSamples, internalformat, width, height) -> None: ...
