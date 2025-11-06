from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_SYNC_FRAME_SGIX: Incomplete
GLX_SYNC_SWAP_SGIX: Incomplete

@_f
def glXBindChannelToWindowSGIX(display, screen, channel, window) -> None: ...
@_f
def glXChannelRectSGIX(display, screen, channel, x, y, w, h) -> None: ...
@_f
def glXChannelRectSyncSGIX(display, screen, channel, synctype) -> None: ...
@_f
def glXQueryChannelDeltasSGIX(display, screen, channel, x, y, w, h) -> None: ...
@_f
def glXQueryChannelRectSGIX(display, screen, channel, dx, dy, dw, dh) -> None: ...
