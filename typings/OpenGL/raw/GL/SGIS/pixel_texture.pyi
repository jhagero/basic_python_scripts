from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS: Incomplete
GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS: Incomplete
GL_PIXEL_GROUP_COLOR_SGIS: Incomplete
GL_PIXEL_TEXTURE_SGIS: Incomplete

@_f
def glGetPixelTexGenParameterfvSGIS(pname, params) -> None: ...
@_f
def glGetPixelTexGenParameterivSGIS(pname, params) -> None: ...
@_f
def glPixelTexGenParameterfSGIS(pname, param) -> None: ...
@_f
def glPixelTexGenParameterfvSGIS(pname, params) -> None: ...
@_f
def glPixelTexGenParameteriSGIS(pname, param) -> None: ...
@_f
def glPixelTexGenParameterivSGIS(pname, params) -> None: ...
