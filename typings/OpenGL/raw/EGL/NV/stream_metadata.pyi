from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_CONSUMER_METADATA_NV: Incomplete
EGL_MAX_STREAM_METADATA_BLOCKS_NV: Incomplete
EGL_MAX_STREAM_METADATA_BLOCK_SIZE_NV: Incomplete
EGL_MAX_STREAM_METADATA_TOTAL_SIZE_NV: Incomplete
EGL_METADATA0_SIZE_NV: Incomplete
EGL_METADATA0_TYPE_NV: Incomplete
EGL_METADATA1_SIZE_NV: Incomplete
EGL_METADATA1_TYPE_NV: Incomplete
EGL_METADATA2_SIZE_NV: Incomplete
EGL_METADATA2_TYPE_NV: Incomplete
EGL_METADATA3_SIZE_NV: Incomplete
EGL_METADATA3_TYPE_NV: Incomplete
EGL_PENDING_METADATA_NV: Incomplete
EGL_PRODUCER_METADATA_NV: Incomplete

@_f
def eglQueryDisplayAttribNV(dpy, attribute, value) -> None: ...
@_f
def eglQueryStreamMetadataNV(dpy, stream, name, n, offset, size, data) -> None: ...
@_f
def eglSetStreamMetadataNV(dpy, stream, n, offset, size, data) -> None: ...
