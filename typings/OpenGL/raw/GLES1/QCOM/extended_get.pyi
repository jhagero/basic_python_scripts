from OpenGL.raw.GLES1._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_STATE_RESTORE: Incomplete
GL_TEXTURE_DEPTH_QCOM: Incomplete
GL_TEXTURE_FORMAT_QCOM: Incomplete
GL_TEXTURE_HEIGHT_QCOM: Incomplete
GL_TEXTURE_IMAGE_VALID_QCOM: Incomplete
GL_TEXTURE_INTERNAL_FORMAT_QCOM: Incomplete
GL_TEXTURE_NUM_LEVELS_QCOM: Incomplete
GL_TEXTURE_OBJECT_VALID_QCOM: Incomplete
GL_TEXTURE_TARGET_QCOM: Incomplete
GL_TEXTURE_TYPE_QCOM: Incomplete
GL_TEXTURE_WIDTH_QCOM: Incomplete

@_f
def glExtGetBufferPointervQCOM(target, params) -> None: ...
@_f
def glExtGetBuffersQCOM(buffers, maxBuffers, numBuffers) -> None: ...
@_f
def glExtGetFramebuffersQCOM(framebuffers, maxFramebuffers, numFramebuffers) -> None: ...
@_f
def glExtGetRenderbuffersQCOM(renderbuffers, maxRenderbuffers, numRenderbuffers) -> None: ...
@_f
def glExtGetTexLevelParameterivQCOM(texture, face, level, pname, params) -> None: ...
@_f
def glExtGetTexSubImageQCOM(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, texels) -> None: ...
@_f
def glExtGetTexturesQCOM(textures, maxTextures, numTextures) -> None: ...
@_f
def glExtTexObjectStateOverrideiQCOM(target, pname, param) -> None: ...
