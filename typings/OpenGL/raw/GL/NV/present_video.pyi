from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_TIME_NV: Incomplete
GL_FIELDS_NV: Incomplete
GL_FRAME_NV: Incomplete
GL_NUM_FILL_STREAMS_NV: Incomplete
GL_PRESENT_DURATION_NV: Incomplete
GL_PRESENT_TIME_NV: Incomplete

@_f
def glGetVideoi64vNV(video_slot, pname, params) -> None: ...
@_f
def glGetVideoivNV(video_slot, pname, params) -> None: ...
@_f
def glGetVideoui64vNV(video_slot, pname, params) -> None: ...
@_f
def glGetVideouivNV(video_slot, pname, params) -> None: ...
@_f
def glPresentFrameDualFillNV(video_slot, minPresentTime, beginPresentTimeId, presentDurationId, type, target0, fill0, target1, fill1, target2, fill2, target3, fill3) -> None: ...
@_f
def glPresentFrameKeyedNV(video_slot, minPresentTime, beginPresentTimeId, presentDurationId, type, target0, fill0, key0, target1, fill1, key1) -> None: ...
