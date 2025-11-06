from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_ATTACHMENT0_OES: Incomplete
GL_DEPTH_ATTACHMENT_OES: Incomplete
GL_DEPTH_COMPONENT16_OES: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES: Incomplete
GL_FRAMEBUFFER_BINDING_OES: Incomplete
GL_FRAMEBUFFER_COMPLETE_OES: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES: Incomplete
GL_FRAMEBUFFER_OES: Incomplete
GL_FRAMEBUFFER_UNSUPPORTED_OES: Incomplete
GL_INVALID_FRAMEBUFFER_OPERATION_OES: Incomplete
GL_MAX_RENDERBUFFER_SIZE_OES: Incomplete
GL_NONE_OES: Incomplete
GL_RENDERBUFFER_ALPHA_SIZE_OES: Incomplete
GL_RENDERBUFFER_BINDING_OES: Incomplete
GL_RENDERBUFFER_BLUE_SIZE_OES: Incomplete
GL_RENDERBUFFER_DEPTH_SIZE_OES: Incomplete
GL_RENDERBUFFER_GREEN_SIZE_OES: Incomplete
GL_RENDERBUFFER_HEIGHT_OES: Incomplete
GL_RENDERBUFFER_INTERNAL_FORMAT_OES: Incomplete
GL_RENDERBUFFER_OES: Incomplete
GL_RENDERBUFFER_RED_SIZE_OES: Incomplete
GL_RENDERBUFFER_STENCIL_SIZE_OES: Incomplete
GL_RENDERBUFFER_WIDTH_OES: Incomplete
GL_RGB565_OES: Incomplete
GL_RGB5_A1_OES: Incomplete
GL_RGBA4_OES: Incomplete
GL_STENCIL_ATTACHMENT_OES: Incomplete

@_f
def glBindFramebufferOES(target, framebuffer) -> None: ...
@_f
def glBindRenderbufferOES(target, renderbuffer) -> None: ...
@_f
def glCheckFramebufferStatusOES(target) -> None: ...
@_f
def glDeleteFramebuffersOES(n, framebuffers) -> None: ...
@_f
def glDeleteRenderbuffersOES(n, renderbuffers) -> None: ...
@_f
def glFramebufferRenderbufferOES(target, attachment, renderbuffertarget, renderbuffer) -> None: ...
@_f
def glFramebufferTexture2DOES(target, attachment, textarget, texture, level) -> None: ...
@_f
def glGenFramebuffersOES(n, framebuffers) -> None: ...
@_f
def glGenRenderbuffersOES(n, renderbuffers) -> None: ...
@_f
def glGenerateMipmapOES(target) -> None: ...
@_f
def glGetFramebufferAttachmentParameterivOES(target, attachment, pname, params) -> None: ...
@_f
def glGetRenderbufferParameterivOES(target, pname, params) -> None: ...
@_f
def glIsFramebufferOES(framebuffer) -> None: ...
@_f
def glIsRenderbufferOES(renderbuffer) -> None: ...
@_f
def glRenderbufferStorageOES(target, internalformat, width, height) -> None: ...
