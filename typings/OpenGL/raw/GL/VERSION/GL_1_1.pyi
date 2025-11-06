from OpenGL.raw.GL._types import *
from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALPHA12: Incomplete
GL_ALPHA16: Incomplete
GL_ALPHA4: Incomplete
GL_ALPHA8: Incomplete
GL_C3F_V3F: Incomplete
GL_C4F_N3F_V3F: Incomplete
GL_C4UB_V2F: Incomplete
GL_C4UB_V3F: Incomplete
GL_CLIENT_ALL_ATTRIB_BITS: Incomplete
GL_CLIENT_ATTRIB_STACK_DEPTH: Incomplete
GL_CLIENT_PIXEL_STORE_BIT: Incomplete
GL_CLIENT_VERTEX_ARRAY_BIT: Incomplete
GL_COLOR_ARRAY: Incomplete
GL_COLOR_ARRAY_POINTER: Incomplete
GL_COLOR_ARRAY_SIZE: Incomplete
GL_COLOR_ARRAY_STRIDE: Incomplete
GL_COLOR_ARRAY_TYPE: Incomplete
GL_COLOR_LOGIC_OP: Incomplete
GL_DOUBLE: Incomplete
GL_EDGE_FLAG_ARRAY: Incomplete
GL_EDGE_FLAG_ARRAY_POINTER: Incomplete
GL_EDGE_FLAG_ARRAY_STRIDE: Incomplete
GL_FEEDBACK_BUFFER_POINTER: Incomplete
GL_FEEDBACK_BUFFER_SIZE: Incomplete
GL_FEEDBACK_BUFFER_TYPE: Incomplete
GL_INDEX_ARRAY: Incomplete
GL_INDEX_ARRAY_POINTER: Incomplete
GL_INDEX_ARRAY_STRIDE: Incomplete
GL_INDEX_ARRAY_TYPE: Incomplete
GL_INDEX_LOGIC_OP: Incomplete
GL_INTENSITY: Incomplete
GL_INTENSITY12: Incomplete
GL_INTENSITY16: Incomplete
GL_INTENSITY4: Incomplete
GL_INTENSITY8: Incomplete
GL_LUMINANCE12: Incomplete
GL_LUMINANCE12_ALPHA12: Incomplete
GL_LUMINANCE12_ALPHA4: Incomplete
GL_LUMINANCE16: Incomplete
GL_LUMINANCE16_ALPHA16: Incomplete
GL_LUMINANCE4: Incomplete
GL_LUMINANCE4_ALPHA4: Incomplete
GL_LUMINANCE6_ALPHA2: Incomplete
GL_LUMINANCE8: Incomplete
GL_LUMINANCE8_ALPHA8: Incomplete
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH: Incomplete
GL_N3F_V3F: Incomplete
GL_NORMAL_ARRAY: Incomplete
GL_NORMAL_ARRAY_POINTER: Incomplete
GL_NORMAL_ARRAY_STRIDE: Incomplete
GL_NORMAL_ARRAY_TYPE: Incomplete
GL_POLYGON_OFFSET_FACTOR: Incomplete
GL_POLYGON_OFFSET_FILL: Incomplete
GL_POLYGON_OFFSET_LINE: Incomplete
GL_POLYGON_OFFSET_POINT: Incomplete
GL_POLYGON_OFFSET_UNITS: Incomplete
GL_PROXY_TEXTURE_1D: Incomplete
GL_PROXY_TEXTURE_2D: Incomplete
GL_R3_G3_B2: Incomplete
GL_RGB10: Incomplete
GL_RGB10_A2: Incomplete
GL_RGB12: Incomplete
GL_RGB16: Incomplete
GL_RGB4: Incomplete
GL_RGB5: Incomplete
GL_RGB5_A1: Incomplete
GL_RGB8: Incomplete
GL_RGBA12: Incomplete
GL_RGBA16: Incomplete
GL_RGBA2: Incomplete
GL_RGBA4: Incomplete
GL_RGBA8: Incomplete
GL_SELECTION_BUFFER_POINTER: Incomplete
GL_SELECTION_BUFFER_SIZE: Incomplete
GL_T2F_C3F_V3F: Incomplete
GL_T2F_C4F_N3F_V3F: Incomplete
GL_T2F_C4UB_V3F: Incomplete
GL_T2F_N3F_V3F: Incomplete
GL_T2F_V3F: Incomplete
GL_T4F_C4F_N3F_V4F: Incomplete
GL_T4F_V4F: Incomplete
GL_TEXTURE_ALPHA_SIZE: Incomplete
GL_TEXTURE_BINDING_1D: Incomplete
GL_TEXTURE_BINDING_2D: Incomplete
GL_TEXTURE_BLUE_SIZE: Incomplete
GL_TEXTURE_COORD_ARRAY: Incomplete
GL_TEXTURE_COORD_ARRAY_POINTER: Incomplete
GL_TEXTURE_COORD_ARRAY_SIZE: Incomplete
GL_TEXTURE_COORD_ARRAY_STRIDE: Incomplete
GL_TEXTURE_COORD_ARRAY_TYPE: Incomplete
GL_TEXTURE_GREEN_SIZE: Incomplete
GL_TEXTURE_INTENSITY_SIZE: Incomplete
GL_TEXTURE_INTERNAL_FORMAT: Incomplete
GL_TEXTURE_LUMINANCE_SIZE: Incomplete
GL_TEXTURE_PRIORITY: Incomplete
GL_TEXTURE_RED_SIZE: Incomplete
GL_TEXTURE_RESIDENT: Incomplete
GL_V2F: Incomplete
GL_V3F: Incomplete
GL_VERTEX_ARRAY: Incomplete
GL_VERTEX_ARRAY_POINTER: Incomplete
GL_VERTEX_ARRAY_SIZE: Incomplete
GL_VERTEX_ARRAY_STRIDE: Incomplete
GL_VERTEX_ARRAY_TYPE: Incomplete

@_f
def glAreTexturesResident(n, textures, residences) -> None: ...
@_f
def glArrayElement(i) -> None: ...
@_f
def glBindTexture(target, texture) -> None: ...
@_f
def glColorPointer(size, type, stride, pointer) -> None: ...
@_f
def glCopyTexImage1D(target, level, internalformat, x, y, width, border) -> None: ...
@_f
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border) -> None: ...
@_f
def glCopyTexSubImage1D(target, level, xoffset, x, y, width) -> None: ...
@_f
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height) -> None: ...
@_f
def glDeleteTextures(n, textures) -> None: ...
@_f
def glDisableClientState(array) -> None: ...
@_f
def glDrawArrays(mode, first, count) -> None: ...
@_f
def glDrawElements(mode, count, type, indices) -> None: ...
@_f
def glEdgeFlagPointer(stride, pointer) -> None: ...
@_f
def glEnableClientState(array) -> None: ...
@_f
def glGenTextures(n, textures) -> None: ...
@_f
def glGetPointerv(pname, params) -> None: ...
@_f
def glIndexPointer(type, stride, pointer) -> None: ...
@_f
def glIndexub(c) -> None: ...
@_f
def glIndexubv(c) -> None: ...
@_f
def glInterleavedArrays(format, stride, pointer) -> None: ...
@_f
def glIsTexture(texture) -> None: ...
@_f
def glNormalPointer(type, stride, pointer) -> None: ...
@_f
def glPolygonOffset(factor, units) -> None: ...
@_f
def glPopClientAttrib() -> None: ...
@_f
def glPrioritizeTextures(n, textures, priorities) -> None: ...
@_f
def glPushClientAttrib(mask) -> None: ...
@_f
def glTexCoordPointer(size, type, stride, pointer) -> None: ...
@_f
def glTexSubImage1D(target, level, xoffset, width, format, type, pixels) -> None: ...
@_f
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels) -> None: ...
@_f
def glVertexPointer(size, type, stride, pointer) -> None: ...
