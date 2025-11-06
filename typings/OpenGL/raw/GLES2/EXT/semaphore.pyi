from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEVICE_UUID_EXT: Incomplete
GL_DRIVER_UUID_EXT: Incomplete
GL_LAYOUT_COLOR_ATTACHMENT_EXT: Incomplete
GL_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_EXT: Incomplete
GL_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_EXT: Incomplete
GL_LAYOUT_DEPTH_STENCIL_ATTACHMENT_EXT: Incomplete
GL_LAYOUT_DEPTH_STENCIL_READ_ONLY_EXT: Incomplete
GL_LAYOUT_GENERAL_EXT: Incomplete
GL_LAYOUT_SHADER_READ_ONLY_EXT: Incomplete
GL_LAYOUT_TRANSFER_DST_EXT: Incomplete
GL_LAYOUT_TRANSFER_SRC_EXT: Incomplete
GL_NUM_DEVICE_UUIDS_EXT: Incomplete
GL_UUID_SIZE_EXT: Incomplete

@_f
def glDeleteSemaphoresEXT(n, semaphores) -> None: ...
@_f
def glGenSemaphoresEXT(n, semaphores) -> None: ...
@_f
def glGetSemaphoreParameterui64vEXT(semaphore, pname, params) -> None: ...
@_f
def glGetUnsignedBytei_vEXT(target, index, data) -> None: ...
@_f
def glGetUnsignedBytevEXT(pname, data) -> None: ...
@_f
def glIsSemaphoreEXT(semaphore) -> None: ...
@_f
def glSemaphoreParameterui64vEXT(semaphore, pname, params) -> None: ...
@_f
def glSignalSemaphoreEXT(semaphore, numBufferBarriers, buffers, numTextureBarriers, textures, dstLayouts) -> None: ...
@_f
def glWaitSemaphoreEXT(semaphore, numBufferBarriers, buffers, numTextureBarriers, textures, srcLayouts) -> None: ...
