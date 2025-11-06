from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_YUV_BUFFER_EXT: Incomplete
EGL_YUV_NUMBER_OF_PLANES_EXT: Incomplete
EGL_YUV_PLANE0_TEXTURE_UNIT_NV: Incomplete
EGL_YUV_PLANE1_TEXTURE_UNIT_NV: Incomplete
EGL_YUV_PLANE2_TEXTURE_UNIT_NV: Incomplete

@_f
def eglStreamConsumerGLTextureExternalAttribsNV(dpy, stream, *attrib_list) -> None: ...
