from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ATTACHMENT0: Incomplete
GL_COLOR_ATTACHMENT1: Incomplete
GL_COLOR_ATTACHMENT10: Incomplete
GL_COLOR_ATTACHMENT11: Incomplete
GL_COLOR_ATTACHMENT12: Incomplete
GL_COLOR_ATTACHMENT13: Incomplete
GL_COLOR_ATTACHMENT14: Incomplete
GL_COLOR_ATTACHMENT15: Incomplete
GL_COLOR_ATTACHMENT2: Incomplete
GL_COLOR_ATTACHMENT3: Incomplete
GL_COLOR_ATTACHMENT4: Incomplete
GL_COLOR_ATTACHMENT5: Incomplete
GL_COLOR_ATTACHMENT6: Incomplete
GL_COLOR_ATTACHMENT7: Incomplete
GL_COLOR_ATTACHMENT8: Incomplete
GL_COLOR_ATTACHMENT9: Incomplete
GL_DEPTH24_STENCIL8: Incomplete
GL_DEPTH_ATTACHMENT: Incomplete
GL_DEPTH_STENCIL: Incomplete
GL_DEPTH_STENCIL_ATTACHMENT: Incomplete
GL_DRAW_FRAMEBUFFER: Incomplete
GL_DRAW_FRAMEBUFFER_BINDING: Incomplete
GL_FRAMEBUFFER: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: Incomplete
GL_FRAMEBUFFER_BINDING: Incomplete
GL_FRAMEBUFFER_COMPLETE: Incomplete
GL_FRAMEBUFFER_DEFAULT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER: Incomplete
GL_FRAMEBUFFER_UNDEFINED: Incomplete
GL_FRAMEBUFFER_UNSUPPORTED: Incomplete
GL_INDEX: Incomplete
GL_INVALID_FRAMEBUFFER_OPERATION: Incomplete
GL_MAX_COLOR_ATTACHMENTS: Incomplete
GL_MAX_RENDERBUFFER_SIZE: Incomplete
GL_MAX_SAMPLES: Incomplete
GL_READ_FRAMEBUFFER: Incomplete
GL_READ_FRAMEBUFFER_BINDING: Incomplete
GL_RENDERBUFFER: Incomplete
GL_RENDERBUFFER_ALPHA_SIZE: Incomplete
GL_RENDERBUFFER_BINDING: Incomplete
GL_RENDERBUFFER_BLUE_SIZE: Incomplete
GL_RENDERBUFFER_DEPTH_SIZE: Incomplete
GL_RENDERBUFFER_GREEN_SIZE: Incomplete
GL_RENDERBUFFER_HEIGHT: Incomplete
GL_RENDERBUFFER_INTERNAL_FORMAT: Incomplete
GL_RENDERBUFFER_RED_SIZE: Incomplete
GL_RENDERBUFFER_SAMPLES: Incomplete
GL_RENDERBUFFER_STENCIL_SIZE: Incomplete
GL_RENDERBUFFER_WIDTH: Incomplete
GL_STENCIL_ATTACHMENT: Incomplete
GL_STENCIL_INDEX1: Incomplete
GL_STENCIL_INDEX16: Incomplete
GL_STENCIL_INDEX4: Incomplete
GL_STENCIL_INDEX8: Incomplete
GL_TEXTURE_STENCIL_SIZE: Incomplete
GL_UNSIGNED_INT_24_8: Incomplete
GL_UNSIGNED_NORMALIZED: Incomplete

@_f
def glBindFramebuffer(target, framebuffer) -> None: ...
@_f
def glBindRenderbuffer(target, renderbuffer) -> None: ...
@_f
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter) -> None: ...
@_f
def glCheckFramebufferStatus(target) -> None: ...
@_f
def glDeleteFramebuffers(n, framebuffers) -> None: ...
@_f
def glDeleteRenderbuffers(n, renderbuffers) -> None: ...
@_f
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer) -> None: ...
@_f
def glFramebufferTexture1D(target, attachment, textarget, texture, level) -> None: ...
@_f
def glFramebufferTexture2D(target, attachment, textarget, texture, level) -> None: ...
@_f
def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset) -> None: ...
@_f
def glFramebufferTextureLayer(target, attachment, texture, level, layer) -> None: ...
@_f
def glGenFramebuffers(n, framebuffers) -> None: ...
@_f
def glGenRenderbuffers(n, renderbuffers) -> None: ...
@_f
def glGenerateMipmap(target) -> None: ...
@_f
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params) -> None: ...
@_f
def glGetRenderbufferParameteriv(target, pname, params) -> None: ...
@_f
def glIsFramebuffer(framebuffer) -> None: ...
@_f
def glIsRenderbuffer(renderbuffer) -> None: ...
@_f
def glRenderbufferStorage(target, internalformat, width, height) -> None: ...
@_f
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height) -> None: ...
