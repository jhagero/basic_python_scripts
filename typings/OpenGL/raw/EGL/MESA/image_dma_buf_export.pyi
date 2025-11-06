from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays

@_f
def eglExportDMABUFImageMESA(dpy, image, fds, strides, offsets) -> None: ...
@_f
def eglExportDMABUFImageQueryMESA(dpy, image, fourcc, num_planes, modifiers) -> None: ...
