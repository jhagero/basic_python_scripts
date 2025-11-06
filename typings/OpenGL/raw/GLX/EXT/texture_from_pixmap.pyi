from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_AUX0_EXT: Incomplete
GLX_AUX1_EXT: Incomplete
GLX_AUX2_EXT: Incomplete
GLX_AUX3_EXT: Incomplete
GLX_AUX4_EXT: Incomplete
GLX_AUX5_EXT: Incomplete
GLX_AUX6_EXT: Incomplete
GLX_AUX7_EXT: Incomplete
GLX_AUX8_EXT: Incomplete
GLX_AUX9_EXT: Incomplete
GLX_BACK_EXT: Incomplete
GLX_BACK_LEFT_EXT: Incomplete
GLX_BACK_RIGHT_EXT: Incomplete
GLX_BIND_TO_MIPMAP_TEXTURE_EXT: Incomplete
GLX_BIND_TO_TEXTURE_RGBA_EXT: Incomplete
GLX_BIND_TO_TEXTURE_RGB_EXT: Incomplete
GLX_BIND_TO_TEXTURE_TARGETS_EXT: Incomplete
GLX_FRONT_EXT: Incomplete
GLX_FRONT_LEFT_EXT: Incomplete
GLX_FRONT_RIGHT_EXT: Incomplete
GLX_MIPMAP_TEXTURE_EXT: Incomplete
GLX_TEXTURE_1D_BIT_EXT: Incomplete
GLX_TEXTURE_1D_EXT: Incomplete
GLX_TEXTURE_2D_BIT_EXT: Incomplete
GLX_TEXTURE_2D_EXT: Incomplete
GLX_TEXTURE_FORMAT_EXT: Incomplete
GLX_TEXTURE_FORMAT_NONE_EXT: Incomplete
GLX_TEXTURE_FORMAT_RGBA_EXT: Incomplete
GLX_TEXTURE_FORMAT_RGB_EXT: Incomplete
GLX_TEXTURE_RECTANGLE_BIT_EXT: Incomplete
GLX_TEXTURE_RECTANGLE_EXT: Incomplete
GLX_TEXTURE_TARGET_EXT: Incomplete
GLX_Y_INVERTED_EXT: Incomplete

@_f
def glXBindTexImageEXT(dpy, drawable, buffer, attrib_list) -> None: ...
@_f
def glXReleaseTexImageEXT(dpy, drawable, buffer) -> None: ...
