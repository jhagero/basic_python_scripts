from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FAILURE_NV: Incomplete
GL_FIELD_LOWER_NV: Incomplete
GL_FIELD_UPPER_NV: Incomplete
GL_LAST_VIDEO_CAPTURE_STATUS_NV: Incomplete
GL_NEXT_VIDEO_CAPTURE_BUFFER_STATUS_NV: Incomplete
GL_NUM_VIDEO_CAPTURE_STREAMS_NV: Incomplete
GL_PARTIAL_SUCCESS_NV: Incomplete
GL_SUCCESS_NV: Incomplete
GL_VIDEO_BUFFER_BINDING_NV: Incomplete
GL_VIDEO_BUFFER_INTERNAL_FORMAT_NV: Incomplete
GL_VIDEO_BUFFER_NV: Incomplete
GL_VIDEO_BUFFER_PITCH_NV: Incomplete
GL_VIDEO_CAPTURE_FIELD_LOWER_HEIGHT_NV: Incomplete
GL_VIDEO_CAPTURE_FIELD_UPPER_HEIGHT_NV: Incomplete
GL_VIDEO_CAPTURE_FRAME_HEIGHT_NV: Incomplete
GL_VIDEO_CAPTURE_FRAME_WIDTH_NV: Incomplete
GL_VIDEO_CAPTURE_SURFACE_ORIGIN_NV: Incomplete
GL_VIDEO_CAPTURE_TO_422_SUPPORTED_NV: Incomplete
GL_VIDEO_COLOR_CONVERSION_MATRIX_NV: Incomplete
GL_VIDEO_COLOR_CONVERSION_MAX_NV: Incomplete
GL_VIDEO_COLOR_CONVERSION_MIN_NV: Incomplete
GL_VIDEO_COLOR_CONVERSION_OFFSET_NV: Incomplete
GL_YCBAYCR8A_4224_NV: Incomplete
GL_YCBYCR8_422_NV: Incomplete
GL_Z4Y12Z4CB12Z4A12Z4Y12Z4CR12Z4A12_4224_NV: Incomplete
GL_Z4Y12Z4CB12Z4CR12_444_NV: Incomplete
GL_Z4Y12Z4CB12Z4Y12Z4CR12_422_NV: Incomplete
GL_Z6Y10Z6CB10Z6A10Z6Y10Z6CR10Z6A10_4224_NV: Incomplete
GL_Z6Y10Z6CB10Z6Y10Z6CR10_422_NV: Incomplete

@_f
def glBeginVideoCaptureNV(video_capture_slot) -> None: ...
@_f
def glBindVideoCaptureStreamBufferNV(video_capture_slot, stream, frame_region, offset) -> None: ...
@_f
def glBindVideoCaptureStreamTextureNV(video_capture_slot, stream, frame_region, target, texture) -> None: ...
@_f
def glEndVideoCaptureNV(video_capture_slot) -> None: ...
@_f
def glGetVideoCaptureStreamdvNV(video_capture_slot, stream, pname, params) -> None: ...
@_f
def glGetVideoCaptureStreamfvNV(video_capture_slot, stream, pname, params) -> None: ...
@_f
def glGetVideoCaptureStreamivNV(video_capture_slot, stream, pname, params) -> None: ...
@_f
def glGetVideoCaptureivNV(video_capture_slot, pname, params) -> None: ...
@_f
def glVideoCaptureNV(video_capture_slot, sequence_num, capture_time) -> None: ...
@_f
def glVideoCaptureStreamParameterdvNV(video_capture_slot, stream, pname, params) -> None: ...
@_f
def glVideoCaptureStreamParameterfvNV(video_capture_slot, stream, pname, params) -> None: ...
@_f
def glVideoCaptureStreamParameterivNV(video_capture_slot, stream, pname, params) -> None: ...
