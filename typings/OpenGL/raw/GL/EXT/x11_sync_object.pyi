from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_SYNC_X11_FENCE_EXT: Incomplete

@_f
def glImportSyncEXT(external_sync_type, external_sync, flags) -> None: ...
