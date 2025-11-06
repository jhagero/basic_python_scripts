from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_NUM_VIDEO_SLOTS_NV: Incomplete

@_f
def glXBindVideoDeviceNV(dpy, video_slot, video_device, attrib_list) -> None: ...
@_f
def glXEnumerateVideoDevicesNV(dpy, screen, nelements) -> None: ...
