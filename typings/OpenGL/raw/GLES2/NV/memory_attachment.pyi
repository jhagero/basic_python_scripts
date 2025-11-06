from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ATTACHED_MEMORY_OBJECT_NV: Incomplete
GL_ATTACHED_MEMORY_OFFSET_NV: Incomplete
GL_DETACHED_BUFFERS_NV: Incomplete
GL_DETACHED_MEMORY_INCARNATION_NV: Incomplete
GL_DETACHED_TEXTURES_NV: Incomplete
GL_MAX_DETACHED_BUFFERS_NV: Incomplete
GL_MAX_DETACHED_TEXTURES_NV: Incomplete
GL_MEMORY_ATTACHABLE_ALIGNMENT_NV: Incomplete
GL_MEMORY_ATTACHABLE_NV: Incomplete
GL_MEMORY_ATTACHABLE_SIZE_NV: Incomplete

@_f
def glBufferAttachMemoryNV(target, memory, offset) -> None: ...
@_f
def glGetMemoryObjectDetachedResourcesuivNV(memory, pname, first, count, params) -> None: ...
@_f
def glNamedBufferAttachMemoryNV(buffer, memory, offset) -> None: ...
@_f
def glResetMemoryObjectParameterNV(memory, pname) -> None: ...
@_f
def glTexAttachMemoryNV(target, memory, offset) -> None: ...
@_f
def glTextureAttachMemoryNV(texture, memory, offset) -> None: ...
