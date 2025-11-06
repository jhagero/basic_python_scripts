from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_SYNC_CL_EVENT_ARB: Incomplete
GL_SYNC_CL_EVENT_COMPLETE_ARB: Incomplete

@_f
def glCreateSyncFromCLeventARB(context, event, flags) -> None: ...
