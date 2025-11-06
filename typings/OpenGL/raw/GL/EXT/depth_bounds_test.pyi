from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEPTH_BOUNDS_EXT: Incomplete
GL_DEPTH_BOUNDS_TEST_EXT: Incomplete

@_f
def glDepthBoundsEXT(zmin, zmax) -> None: ...
