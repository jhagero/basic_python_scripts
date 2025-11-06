from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_DEVICE_LUID_EXT: Incomplete
GL_DEVICE_NODE_MASK_EXT: Incomplete
GL_HANDLE_TYPE_D3D11_IMAGE_EXT: Incomplete
GL_HANDLE_TYPE_D3D11_IMAGE_KMT_EXT: Incomplete
GL_HANDLE_TYPE_D3D12_RESOURCE_EXT: Incomplete
GL_HANDLE_TYPE_D3D12_TILEPOOL_EXT: Incomplete
GL_HANDLE_TYPE_OPAQUE_WIN32_EXT: Incomplete
GL_HANDLE_TYPE_OPAQUE_WIN32_KMT_EXT: Incomplete
GL_LUID_SIZE_EXT: Incomplete

@_f
def glImportMemoryWin32HandleEXT(memory, size, handleType, handle) -> None: ...
@_f
def glImportMemoryWin32NameEXT(memory, size, handleType, name) -> None: ...
