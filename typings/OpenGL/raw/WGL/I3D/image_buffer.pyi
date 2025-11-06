from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_IMAGE_BUFFER_LOCK_I3D: Incomplete
WGL_IMAGE_BUFFER_MIN_ACCESS_I3D: Incomplete

@_f
def wglAssociateImageBufferEventsI3D(hDC, pEvent, pAddress, pSize, count) -> None: ...
@_f
def wglCreateImageBufferI3D(hDC, dwSize, uFlags) -> None: ...
@_f
def wglDestroyImageBufferI3D(hDC, pAddress) -> None: ...
@_f
def wglReleaseImageBufferEventsI3D(hDC, pAddress, count) -> None: ...
