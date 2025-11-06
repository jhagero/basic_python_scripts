from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_NUM_VIDEO_SLOTS_NV: Incomplete

@_f
def wglBindVideoDeviceNV(hDc, uVideoSlot, hVideoDevice, piAttribList) -> None: ...
@_f
def wglEnumerateVideoDevicesNV(hDc, phDeviceList) -> None: ...
@_f
def wglQueryCurrentContextNV(iAttribute, piValue) -> None: ...
