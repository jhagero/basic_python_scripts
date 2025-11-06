from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_QUERY_RESOURCE_BUFFEROBJECT_NV: Incomplete
GL_QUERY_RESOURCE_MEMTYPE_VIDMEM_NV: Incomplete
GL_QUERY_RESOURCE_RENDERBUFFER_NV: Incomplete
GL_QUERY_RESOURCE_SYS_RESERVED_NV: Incomplete
GL_QUERY_RESOURCE_TEXTURE_NV: Incomplete
GL_QUERY_RESOURCE_TYPE_VIDMEM_ALLOC_NV: Incomplete

@_f
def glQueryResourceNV(queryType, tagId, count, buffer) -> None: ...
