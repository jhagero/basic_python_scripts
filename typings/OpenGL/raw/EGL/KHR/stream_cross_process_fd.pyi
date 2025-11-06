from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays

@_f
def eglCreateStreamFromFileDescriptorKHR(dpy, file_descriptor) -> None: ...
@_f
def eglGetStreamFileDescriptorKHR(dpy, stream) -> None: ...
