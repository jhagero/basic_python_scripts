from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: Incomplete
GL_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: Incomplete
GL_TEXTURE_2D_MULTISAMPLE_ARRAY_OES: Incomplete
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY_OES: Incomplete
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: Incomplete

@_f
def glTexStorage3DMultisampleOES(target, samples, internalformat, width, height, depth, fixedsamplelocations) -> None: ...
