from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CONFORMANT_NV: Incomplete
GL_MULTISAMPLES_NV: Incomplete
GL_RENDERBUFFER: Incomplete
GL_SUPERSAMPLE_SCALE_X_NV: Incomplete
GL_SUPERSAMPLE_SCALE_Y_NV: Incomplete
GL_TEXTURE_2D_MULTISAMPLE: Incomplete
GL_TEXTURE_2D_MULTISAMPLE_ARRAY: Incomplete

@_f
def glGetInternalformatSampleivNV(target, internalformat, samples, pname, count, params) -> None: ...
