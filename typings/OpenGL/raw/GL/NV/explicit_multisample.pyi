from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_INT_SAMPLER_RENDERBUFFER_NV: Incomplete
GL_MAX_SAMPLE_MASK_WORDS_NV: Incomplete
GL_SAMPLER_RENDERBUFFER_NV: Incomplete
GL_SAMPLE_MASK_NV: Incomplete
GL_SAMPLE_MASK_VALUE_NV: Incomplete
GL_SAMPLE_POSITION_NV: Incomplete
GL_TEXTURE_BINDING_RENDERBUFFER_NV: Incomplete
GL_TEXTURE_RENDERBUFFER_DATA_STORE_BINDING_NV: Incomplete
GL_TEXTURE_RENDERBUFFER_NV: Incomplete
GL_UNSIGNED_INT_SAMPLER_RENDERBUFFER_NV: Incomplete

@_f
def glGetMultisamplefvNV(pname, index, val) -> None: ...
@_f
def glSampleMaskIndexedNV(index, mask) -> None: ...
@_f
def glTexRenderbufferNV(target, renderbuffer) -> None: ...
