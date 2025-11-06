from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_OCCLUSION_QUERY_EVENT_MASK_AMD: Incomplete
GL_QUERY_ALL_EVENT_BITS_AMD: Incomplete
GL_QUERY_DEPTH_BOUNDS_FAIL_EVENT_BIT_AMD: Incomplete
GL_QUERY_DEPTH_FAIL_EVENT_BIT_AMD: Incomplete
GL_QUERY_DEPTH_PASS_EVENT_BIT_AMD: Incomplete
GL_QUERY_STENCIL_FAIL_EVENT_BIT_AMD: Incomplete

@_f
def glQueryObjectParameteruiAMD(target, id, pname, param) -> None: ...
