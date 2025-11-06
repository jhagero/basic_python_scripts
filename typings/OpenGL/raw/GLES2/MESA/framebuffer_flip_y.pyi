from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_FLIP_Y_MESA: Incomplete

@_f
def glFramebufferParameteriMESA(target, pname, param) -> None: ...
@_f
def glGetFramebufferParameterivMESA(target, pname, params) -> None: ...
