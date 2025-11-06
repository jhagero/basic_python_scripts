from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ATTACHMENT0_EXT: Incomplete
GL_COLOR_ATTACHMENT10_EXT: Incomplete
GL_COLOR_ATTACHMENT11_EXT: Incomplete
GL_COLOR_ATTACHMENT12_EXT: Incomplete
GL_COLOR_ATTACHMENT13_EXT: Incomplete
GL_COLOR_ATTACHMENT14_EXT: Incomplete
GL_COLOR_ATTACHMENT15_EXT: Incomplete
GL_COLOR_ATTACHMENT1_EXT: Incomplete
GL_COLOR_ATTACHMENT2_EXT: Incomplete
GL_COLOR_ATTACHMENT3_EXT: Incomplete
GL_COLOR_ATTACHMENT4_EXT: Incomplete
GL_COLOR_ATTACHMENT5_EXT: Incomplete
GL_COLOR_ATTACHMENT6_EXT: Incomplete
GL_COLOR_ATTACHMENT7_EXT: Incomplete
GL_COLOR_ATTACHMENT8_EXT: Incomplete
GL_COLOR_ATTACHMENT9_EXT: Incomplete
GL_DEPTH_ATTACHMENT_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT: Incomplete
GL_FRAMEBUFFER_BINDING_EXT: Incomplete
GL_FRAMEBUFFER_COMPLETE_EXT: Incomplete
GL_FRAMEBUFFER_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT: Incomplete
GL_FRAMEBUFFER_UNSUPPORTED_EXT: Incomplete
GL_INVALID_FRAMEBUFFER_OPERATION_EXT: Incomplete
GL_MAX_COLOR_ATTACHMENTS_EXT: Incomplete
GL_MAX_RENDERBUFFER_SIZE_EXT: Incomplete
GL_RENDERBUFFER_ALPHA_SIZE_EXT: Incomplete
GL_RENDERBUFFER_BINDING_EXT: Incomplete
GL_RENDERBUFFER_BLUE_SIZE_EXT: Incomplete
GL_RENDERBUFFER_DEPTH_SIZE_EXT: Incomplete
GL_RENDERBUFFER_EXT: Incomplete
GL_RENDERBUFFER_GREEN_SIZE_EXT: Incomplete
GL_RENDERBUFFER_HEIGHT_EXT: Incomplete
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT: Incomplete
GL_RENDERBUFFER_RED_SIZE_EXT: Incomplete
GL_RENDERBUFFER_STENCIL_SIZE_EXT: Incomplete
GL_RENDERBUFFER_WIDTH_EXT: Incomplete
GL_STENCIL_ATTACHMENT_EXT: Incomplete
GL_STENCIL_INDEX16_EXT: Incomplete
GL_STENCIL_INDEX1_EXT: Incomplete
GL_STENCIL_INDEX4_EXT: Incomplete
GL_STENCIL_INDEX8_EXT: Incomplete

@_f
def glBindFramebufferEXT(target, framebuffer) -> None: ...
@_f
def glBindRenderbufferEXT(target, renderbuffer) -> None: ...
@_f
def glCheckFramebufferStatusEXT(target) -> None: ...
@_f
def glDeleteFramebuffersEXT(n, framebuffers) -> None: ...
@_f
def glDeleteRenderbuffersEXT(n, renderbuffers) -> None: ...
@_f
def glFramebufferRenderbufferEXT(target, attachment, renderbuffertarget, renderbuffer) -> None: ...
@_f
def glFramebufferTexture1DEXT(target, attachment, textarget, texture, level) -> None: ...
@_f
def glFramebufferTexture2DEXT(target, attachment, textarget, texture, level) -> None: ...
@_f
def glFramebufferTexture3DEXT(target, attachment, textarget, texture, level, zoffset) -> None: ...
@_f
def glGenFramebuffersEXT(n, framebuffers) -> None: ...
@_f
def glGenRenderbuffersEXT(n, renderbuffers) -> None: ...
@_f
def glGenerateMipmapEXT(target) -> None: ...
@_f
def glGetFramebufferAttachmentParameterivEXT(target, attachment, pname, params) -> None: ...
@_f
def glGetRenderbufferParameterivEXT(target, pname, params) -> None: ...
@_f
def glIsFramebufferEXT(framebuffer) -> None: ...
@_f
def glIsRenderbufferEXT(renderbuffer) -> None: ...
@_f
def glRenderbufferStorageEXT(target, internalformat, width, height) -> None: ...
