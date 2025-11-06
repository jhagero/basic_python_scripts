from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS: Incomplete
GL_FRAMEBUFFER_DEFAULT_HEIGHT: Incomplete
GL_FRAMEBUFFER_DEFAULT_LAYERS: Incomplete
GL_FRAMEBUFFER_DEFAULT_SAMPLES: Incomplete
GL_FRAMEBUFFER_DEFAULT_WIDTH: Incomplete
GL_MAX_FRAMEBUFFER_HEIGHT: Incomplete
GL_MAX_FRAMEBUFFER_LAYERS: Incomplete
GL_MAX_FRAMEBUFFER_SAMPLES: Incomplete
GL_MAX_FRAMEBUFFER_WIDTH: Incomplete

@_f
def glFramebufferParameteri(target, pname, param) -> None: ...
@_f
def glGetFramebufferParameteriv(target, pname, params) -> None: ...
