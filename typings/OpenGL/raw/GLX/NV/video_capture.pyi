from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_DEVICE_ID_NV: Incomplete
GLX_NUM_VIDEO_CAPTURE_SLOTS_NV: Incomplete
GLX_UNIQUE_ID_NV: Incomplete

@_f
def glXBindVideoCaptureDeviceNV(dpy, video_capture_slot, device) -> None: ...
@_f
def glXEnumerateVideoCaptureDevicesNV(dpy, screen, nelements) -> None: ...
@_f
def glXLockVideoCaptureDeviceNV(dpy, device) -> None: ...
@_f
def glXQueryVideoCaptureDeviceNV(dpy, device, attribute, value) -> None: ...
@_f
def glXReleaseVideoCaptureDeviceNV(dpy, device) -> None: ...
