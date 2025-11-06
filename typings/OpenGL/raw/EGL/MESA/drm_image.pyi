from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_DRM_BUFFER_FORMAT_ARGB32_MESA: Incomplete
EGL_DRM_BUFFER_FORMAT_MESA: Incomplete
EGL_DRM_BUFFER_MESA: Incomplete
EGL_DRM_BUFFER_STRIDE_MESA: Incomplete
EGL_DRM_BUFFER_USE_MESA: Incomplete
EGL_DRM_BUFFER_USE_SCANOUT_MESA: Incomplete
EGL_DRM_BUFFER_USE_SHARE_MESA: Incomplete

@_f
def eglCreateDRMImageMESA(dpy, attrib_list) -> None: ...
@_f
def eglExportDRMImageMESA(dpy, image, name, handle, stride) -> None: ...
