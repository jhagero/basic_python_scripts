from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_BIND_TO_VIDEO_RGBA_NV: Incomplete
WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV: Incomplete
WGL_BIND_TO_VIDEO_RGB_NV: Incomplete
WGL_VIDEO_OUT_ALPHA_NV: Incomplete
WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV: Incomplete
WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV: Incomplete
WGL_VIDEO_OUT_COLOR_NV: Incomplete
WGL_VIDEO_OUT_DEPTH_NV: Incomplete
WGL_VIDEO_OUT_FIELD_1: Incomplete
WGL_VIDEO_OUT_FIELD_2: Incomplete
WGL_VIDEO_OUT_FRAME: Incomplete
WGL_VIDEO_OUT_STACKED_FIELDS_1_2: Incomplete
WGL_VIDEO_OUT_STACKED_FIELDS_2_1: Incomplete

@_f
def wglBindVideoImageNV(hVideoDevice, hPbuffer, iVideoBuffer) -> None: ...
@_f
def wglGetVideoDeviceNV(hDC, numDevices, hVideoDevice) -> None: ...
@_f
def wglGetVideoInfoNV(hpVideoDevice, pulCounterOutputPbuffer, pulCounterOutputVideo) -> None: ...
@_f
def wglReleaseVideoDeviceNV(hVideoDevice) -> None: ...
@_f
def wglReleaseVideoImageNV(hPbuffer, iVideoBuffer) -> None: ...
@_f
def wglSendPbufferToVideoNV(hPbuffer, iBufferType, pulCounterPbuffer, bBlock) -> None: ...
