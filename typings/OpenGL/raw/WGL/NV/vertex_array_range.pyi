from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays

@_f
def wglAllocateMemoryNV(size, readfreq, writefreq, priority) -> None: ...
@_f
def wglFreeMemoryNV(pointer) -> None: ...
