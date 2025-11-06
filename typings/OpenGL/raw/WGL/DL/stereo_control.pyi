from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_STEREO_EMITTER_DISABLE_3DL: Incomplete
WGL_STEREO_EMITTER_ENABLE_3DL: Incomplete
WGL_STEREO_POLARITY_INVERT_3DL: Incomplete
WGL_STEREO_POLARITY_NORMAL_3DL: Incomplete

@_f
def wglSetStereoEmitterState3DL(hDC, uState) -> None: ...
