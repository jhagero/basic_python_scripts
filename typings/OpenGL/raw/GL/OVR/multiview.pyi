from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR: Incomplete
GL_MAX_VIEWS_OVR: Incomplete

@_f
def glFramebufferTextureMultiviewOVR(target, attachment, texture, level, baseViewIndex, numViews) -> None: ...
@_f
def glNamedFramebufferTextureMultiviewOVR(framebuffer, attachment, texture, level, baseViewIndex, numViews) -> None: ...
