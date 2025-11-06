from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ARRAY_LIST_IBM: Incomplete
GL_COLOR_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_EDGE_FLAG_ARRAY_LIST_IBM: Incomplete
GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_FOG_COORDINATE_ARRAY_LIST_IBM: Incomplete
GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_INDEX_ARRAY_LIST_IBM: Incomplete
GL_INDEX_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_NORMAL_ARRAY_LIST_IBM: Incomplete
GL_NORMAL_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_SECONDARY_COLOR_ARRAY_LIST_IBM: Incomplete
GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_TEXTURE_COORD_ARRAY_LIST_IBM: Incomplete
GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM: Incomplete
GL_VERTEX_ARRAY_LIST_IBM: Incomplete
GL_VERTEX_ARRAY_LIST_STRIDE_IBM: Incomplete

@_f
def glColorPointerListIBM(size, type, stride, pointer, ptrstride) -> None: ...
@_f
def glEdgeFlagPointerListIBM(stride, pointer, ptrstride) -> None: ...
@_f
def glFogCoordPointerListIBM(type, stride, pointer, ptrstride) -> None: ...
@_f
def glIndexPointerListIBM(type, stride, pointer, ptrstride) -> None: ...
@_f
def glNormalPointerListIBM(type, stride, pointer, ptrstride) -> None: ...
@_f
def glSecondaryColorPointerListIBM(size, type, stride, pointer, ptrstride) -> None: ...
@_f
def glTexCoordPointerListIBM(size, type, stride, pointer, ptrstride) -> None: ...
@_f
def glVertexPointerListIBM(size, type, stride, pointer, ptrstride) -> None: ...
