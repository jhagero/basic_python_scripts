from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glDrawTransformFeedbackInstanced(mode, id, instancecount) -> None: ...
@_f
def glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount) -> None: ...
