from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_TRANSFORM_FEEDBACK_BUFFERS: Incomplete
GL_MAX_VERTEX_STREAMS: Incomplete

@_f
def glBeginQueryIndexed(target, index, id) -> None: ...
@_f
def glDrawTransformFeedbackStream(mode, id, stream) -> None: ...
@_f
def glEndQueryIndexed(target, index) -> None: ...
@_f
def glGetQueryIndexediv(target, index, pname, params) -> None: ...
