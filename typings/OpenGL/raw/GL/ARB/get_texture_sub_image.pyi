from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays

@_f
def glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels) -> None: ...
@_f
def glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels) -> None: ...
