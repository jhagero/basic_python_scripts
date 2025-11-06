from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations) -> None: ...
@_f
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations) -> None: ...
