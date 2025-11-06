from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_INT_SAMPLER_2D_MULTISAMPLE: Incomplete
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: Incomplete
GL_MAX_COLOR_TEXTURE_SAMPLES: Incomplete
GL_MAX_DEPTH_TEXTURE_SAMPLES: Incomplete
GL_MAX_INTEGER_SAMPLES: Incomplete
GL_MAX_SAMPLE_MASK_WORDS: Incomplete
GL_PROXY_TEXTURE_2D_MULTISAMPLE: Incomplete
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY: Incomplete
GL_SAMPLER_2D_MULTISAMPLE: Incomplete
GL_SAMPLER_2D_MULTISAMPLE_ARRAY: Incomplete
GL_SAMPLE_MASK: Incomplete
GL_SAMPLE_MASK_VALUE: Incomplete
GL_SAMPLE_POSITION: Incomplete
GL_TEXTURE_2D_MULTISAMPLE: Incomplete
GL_TEXTURE_2D_MULTISAMPLE_ARRAY: Incomplete
GL_TEXTURE_BINDING_2D_MULTISAMPLE: Incomplete
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: Incomplete
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: Incomplete
GL_TEXTURE_SAMPLES: Incomplete
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: Incomplete
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: Incomplete

@_f
def glGetMultisamplefv(pname, index, val) -> None: ...
@_f
def glSampleMaski(maskNumber, mask) -> None: ...
@_f
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations) -> None: ...
@_f
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations) -> None: ...
