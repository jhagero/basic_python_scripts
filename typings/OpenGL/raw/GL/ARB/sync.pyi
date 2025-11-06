from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALREADY_SIGNALED: Incomplete
GL_CONDITION_SATISFIED: Incomplete
GL_MAX_SERVER_WAIT_TIMEOUT: Incomplete
GL_OBJECT_TYPE: Incomplete
GL_SIGNALED: Incomplete
GL_SYNC_CONDITION: Incomplete
GL_SYNC_FENCE: Incomplete
GL_SYNC_FLAGS: Incomplete
GL_SYNC_FLUSH_COMMANDS_BIT: Incomplete
GL_SYNC_GPU_COMMANDS_COMPLETE: Incomplete
GL_SYNC_STATUS: Incomplete
GL_TIMEOUT_EXPIRED: Incomplete
GL_TIMEOUT_IGNORED: Incomplete
GL_UNSIGNALED: Incomplete
GL_WAIT_FAILED: Incomplete

@_f
def glClientWaitSync(sync, flags, timeout) -> None: ...
@_f
def glDeleteSync(sync) -> None: ...
@_f
def glFenceSync(condition, flags) -> None: ...
@_f
def glGetInteger64v(pname, data) -> None: ...
@_f
def glGetSynciv(sync, pname, count, length, values) -> None: ...
@_f
def glIsSync(sync) -> None: ...
@_f
def glWaitSync(sync, flags, timeout) -> None: ...
