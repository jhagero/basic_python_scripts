from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALREADY_SIGNALED_APPLE: Incomplete
GL_CONDITION_SATISFIED_APPLE: Incomplete
GL_MAX_SERVER_WAIT_TIMEOUT_APPLE: Incomplete
GL_OBJECT_TYPE_APPLE: Incomplete
GL_SIGNALED_APPLE: Incomplete
GL_SYNC_CONDITION_APPLE: Incomplete
GL_SYNC_FENCE_APPLE: Incomplete
GL_SYNC_FLAGS_APPLE: Incomplete
GL_SYNC_FLUSH_COMMANDS_BIT_APPLE: Incomplete
GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE: Incomplete
GL_SYNC_OBJECT_APPLE: Incomplete
GL_SYNC_STATUS_APPLE: Incomplete
GL_TIMEOUT_EXPIRED_APPLE: Incomplete
GL_TIMEOUT_IGNORED_APPLE: Incomplete
GL_UNSIGNALED_APPLE: Incomplete
GL_WAIT_FAILED_APPLE: Incomplete

@_f
def glClientWaitSyncAPPLE(sync, flags, timeout) -> None: ...
@_f
def glDeleteSyncAPPLE(sync) -> None: ...
@_f
def glFenceSyncAPPLE(condition, flags) -> None: ...
@_f
def glGetInteger64vAPPLE(pname, params) -> None: ...
@_f
def glGetSyncivAPPLE(sync, pname, count, length, values) -> None: ...
@_f
def glIsSyncAPPLE(sync) -> None: ...
@_f
def glWaitSyncAPPLE(sync, flags, timeout) -> None: ...
