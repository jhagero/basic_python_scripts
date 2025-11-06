from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ARRAY_ADDRESS_NV: Incomplete
GL_COLOR_ARRAY_LENGTH_NV: Incomplete
GL_DRAW_INDIRECT_ADDRESS_NV: Incomplete
GL_DRAW_INDIRECT_LENGTH_NV: Incomplete
GL_DRAW_INDIRECT_UNIFIED_NV: Incomplete
GL_EDGE_FLAG_ARRAY_ADDRESS_NV: Incomplete
GL_EDGE_FLAG_ARRAY_LENGTH_NV: Incomplete
GL_ELEMENT_ARRAY_ADDRESS_NV: Incomplete
GL_ELEMENT_ARRAY_LENGTH_NV: Incomplete
GL_ELEMENT_ARRAY_UNIFIED_NV: Incomplete
GL_FOG_COORD_ARRAY_ADDRESS_NV: Incomplete
GL_FOG_COORD_ARRAY_LENGTH_NV: Incomplete
GL_INDEX_ARRAY_ADDRESS_NV: Incomplete
GL_INDEX_ARRAY_LENGTH_NV: Incomplete
GL_NORMAL_ARRAY_ADDRESS_NV: Incomplete
GL_NORMAL_ARRAY_LENGTH_NV: Incomplete
GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV: Incomplete
GL_SECONDARY_COLOR_ARRAY_LENGTH_NV: Incomplete
GL_TEXTURE_COORD_ARRAY_ADDRESS_NV: Incomplete
GL_TEXTURE_COORD_ARRAY_LENGTH_NV: Incomplete
GL_VERTEX_ARRAY_ADDRESS_NV: Incomplete
GL_VERTEX_ARRAY_LENGTH_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV: Incomplete

@_f
def glBufferAddressRangeNV(pname, index, address, length) -> None: ...
@_f
def glColorFormatNV(size, type, stride) -> None: ...
@_f
def glEdgeFlagFormatNV(stride) -> None: ...
@_f
def glFogCoordFormatNV(type, stride) -> None: ...
@_f
def glGetIntegerui64i_vNV(value, index, result) -> None: ...
@_f
def glIndexFormatNV(type, stride) -> None: ...
@_f
def glNormalFormatNV(type, stride) -> None: ...
@_f
def glSecondaryColorFormatNV(size, type, stride) -> None: ...
@_f
def glTexCoordFormatNV(size, type, stride) -> None: ...
@_f
def glVertexAttribFormatNV(index, size, type, normalized, stride) -> None: ...
@_f
def glVertexAttribIFormatNV(index, size, type, stride) -> None: ...
@_f
def glVertexFormatNV(size, type, stride) -> None: ...
