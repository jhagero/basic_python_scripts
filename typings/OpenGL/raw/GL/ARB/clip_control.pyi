from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CLIP_DEPTH_MODE: Incomplete
GL_CLIP_ORIGIN: Incomplete
GL_LOWER_LEFT: Incomplete
GL_NEGATIVE_ONE_TO_ONE: Incomplete
GL_UPPER_LEFT: Incomplete
GL_ZERO_TO_ONE: Incomplete

@_f
def glClipControl(origin, depth) -> None: ...
