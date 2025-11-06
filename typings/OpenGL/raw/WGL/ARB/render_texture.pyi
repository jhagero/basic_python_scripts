from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_AUX0_ARB: Incomplete
WGL_AUX1_ARB: Incomplete
WGL_AUX2_ARB: Incomplete
WGL_AUX3_ARB: Incomplete
WGL_AUX4_ARB: Incomplete
WGL_AUX5_ARB: Incomplete
WGL_AUX6_ARB: Incomplete
WGL_AUX7_ARB: Incomplete
WGL_AUX8_ARB: Incomplete
WGL_AUX9_ARB: Incomplete
WGL_BACK_LEFT_ARB: Incomplete
WGL_BACK_RIGHT_ARB: Incomplete
WGL_BIND_TO_TEXTURE_RGBA_ARB: Incomplete
WGL_BIND_TO_TEXTURE_RGB_ARB: Incomplete
WGL_CUBE_MAP_FACE_ARB: Incomplete
WGL_FRONT_LEFT_ARB: Incomplete
WGL_FRONT_RIGHT_ARB: Incomplete
WGL_MIPMAP_LEVEL_ARB: Incomplete
WGL_MIPMAP_TEXTURE_ARB: Incomplete
WGL_NO_TEXTURE_ARB: Incomplete
WGL_TEXTURE_1D_ARB: Incomplete
WGL_TEXTURE_2D_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB: Incomplete
WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB: Incomplete
WGL_TEXTURE_FORMAT_ARB: Incomplete
WGL_TEXTURE_RGBA_ARB: Incomplete
WGL_TEXTURE_RGB_ARB: Incomplete
WGL_TEXTURE_TARGET_ARB: Incomplete

@_f
def wglBindTexImageARB(hPbuffer, iBuffer) -> None: ...
@_f
def wglReleaseTexImageARB(hPbuffer, iBuffer) -> None: ...
@_f
def wglSetPbufferAttribARB(hPbuffer, piAttribList) -> None: ...
