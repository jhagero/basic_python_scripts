from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_NUM_VIDEO_CAPTURE_SLOTS_NV: Incomplete
WGL_UNIQUE_ID_NV: Incomplete

@_f
def wglBindVideoCaptureDeviceNV(uVideoSlot, hDevice) -> None: ...
@_f
def wglEnumerateVideoCaptureDevicesNV(hDc, phDeviceList) -> None: ...
@_f
def wglLockVideoCaptureDeviceNV(hDc, hDevice) -> None: ...
@_f
def wglQueryVideoCaptureDeviceNV(hDc, hDevice, iAttribute, piValue) -> None: ...
@_f
def wglReleaseVideoCaptureDeviceNV(hDc, hDevice) -> None: ...
