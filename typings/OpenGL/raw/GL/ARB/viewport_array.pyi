from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEPTH_RANGE: Incomplete
GL_FIRST_VERTEX_CONVENTION: Incomplete
GL_LAST_VERTEX_CONVENTION: Incomplete
GL_LAYER_PROVOKING_VERTEX: Incomplete
GL_MAX_VIEWPORTS: Incomplete
GL_PROVOKING_VERTEX: Incomplete
GL_SCISSOR_BOX: Incomplete
GL_SCISSOR_TEST: Incomplete
GL_UNDEFINED_VERTEX: Incomplete
GL_VIEWPORT: Incomplete
GL_VIEWPORT_BOUNDS_RANGE: Incomplete
GL_VIEWPORT_INDEX_PROVOKING_VERTEX: Incomplete
GL_VIEWPORT_SUBPIXEL_BITS: Incomplete

@_f
def glDepthRangeArraydvNV(first, count, v) -> None: ...
@_f
def glDepthRangeArrayv(first, count, v) -> None: ...
@_f
def glDepthRangeIndexed(index, n, f) -> None: ...
@_f
def glDepthRangeIndexeddNV(index, n, f) -> None: ...
@_f
def glGetDoublei_v(target, index, data) -> None: ...
@_f
def glGetFloati_v(target, index, data) -> None: ...
@_f
def glScissorArrayv(first, count, v) -> None: ...
@_f
def glScissorIndexed(index, left, bottom, width, height) -> None: ...
@_f
def glScissorIndexedv(index, v) -> None: ...
@_f
def glViewportArrayv(first, count, v) -> None: ...
@_f
def glViewportIndexedf(index, x, y, w, h) -> None: ...
@_f
def glViewportIndexedfv(index, v) -> None: ...
