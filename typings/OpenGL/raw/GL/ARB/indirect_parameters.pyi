from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_PARAMETER_BUFFER_ARB: Incomplete
GL_PARAMETER_BUFFER_BINDING_ARB: Incomplete

@_f
def glMultiDrawArraysIndirectCountARB(mode, indirect, drawcount, maxdrawcount, stride) -> None: ...
@_f
def glMultiDrawElementsIndirectCountARB(mode, type, indirect, drawcount, maxdrawcount, stride) -> None: ...
