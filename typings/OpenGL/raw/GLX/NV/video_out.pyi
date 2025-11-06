from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_VIDEO_OUT_ALPHA_NV: Incomplete
GLX_VIDEO_OUT_COLOR_AND_ALPHA_NV: Incomplete
GLX_VIDEO_OUT_COLOR_AND_DEPTH_NV: Incomplete
GLX_VIDEO_OUT_COLOR_NV: Incomplete
GLX_VIDEO_OUT_DEPTH_NV: Incomplete
GLX_VIDEO_OUT_FIELD_1_NV: Incomplete
GLX_VIDEO_OUT_FIELD_2_NV: Incomplete
GLX_VIDEO_OUT_FRAME_NV: Incomplete
GLX_VIDEO_OUT_STACKED_FIELDS_1_2_NV: Incomplete
GLX_VIDEO_OUT_STACKED_FIELDS_2_1_NV: Incomplete

@_f
def glXBindVideoImageNV(dpy, VideoDevice, pbuf, iVideoBuffer) -> None: ...
@_f
def glXGetVideoDeviceNV(dpy, screen, numVideoDevices, pVideoDevice) -> None: ...
@_f
def glXGetVideoInfoNV(dpy, screen, VideoDevice, pulCounterOutputPbuffer, pulCounterOutputVideo) -> None: ...
@_f
def glXReleaseVideoDeviceNV(dpy, screen, VideoDevice) -> None: ...
@_f
def glXReleaseVideoImageNV(dpy, pbuf) -> None: ...
@_f
def glXSendPbufferToVideoNV(dpy, pbuf, iBufferType, pulCounterPbuffer, bBlock) -> None: ...
