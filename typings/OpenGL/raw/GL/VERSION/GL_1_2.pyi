from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALIASED_LINE_WIDTH_RANGE: Incomplete
GL_ALIASED_POINT_SIZE_RANGE: Incomplete
GL_BGR: Incomplete
GL_BGRA: Incomplete
GL_CLAMP_TO_EDGE: Incomplete
GL_LIGHT_MODEL_COLOR_CONTROL: Incomplete
GL_MAX_3D_TEXTURE_SIZE: Incomplete
GL_MAX_ELEMENTS_INDICES: Incomplete
GL_MAX_ELEMENTS_VERTICES: Incomplete
GL_PACK_IMAGE_HEIGHT: Incomplete
GL_PACK_SKIP_IMAGES: Incomplete
GL_PROXY_TEXTURE_3D: Incomplete
GL_RESCALE_NORMAL: Incomplete
GL_SEPARATE_SPECULAR_COLOR: Incomplete
GL_SINGLE_COLOR: Incomplete
GL_SMOOTH_LINE_WIDTH_GRANULARITY: Incomplete
GL_SMOOTH_LINE_WIDTH_RANGE: Incomplete
GL_SMOOTH_POINT_SIZE_GRANULARITY: Incomplete
GL_SMOOTH_POINT_SIZE_RANGE: Incomplete
GL_TEXTURE_3D: Incomplete
GL_TEXTURE_BASE_LEVEL: Incomplete
GL_TEXTURE_BINDING_3D: Incomplete
GL_TEXTURE_DEPTH: Incomplete
GL_TEXTURE_MAX_LEVEL: Incomplete
GL_TEXTURE_MAX_LOD: Incomplete
GL_TEXTURE_MIN_LOD: Incomplete
GL_TEXTURE_WRAP_R: Incomplete
GL_UNPACK_IMAGE_HEIGHT: Incomplete
GL_UNPACK_SKIP_IMAGES: Incomplete
GL_UNSIGNED_BYTE_2_3_3_REV: Incomplete
GL_UNSIGNED_BYTE_3_3_2: Incomplete
GL_UNSIGNED_INT_10_10_10_2: Incomplete
GL_UNSIGNED_INT_2_10_10_10_REV: Incomplete
GL_UNSIGNED_INT_8_8_8_8: Incomplete
GL_UNSIGNED_INT_8_8_8_8_REV: Incomplete
GL_UNSIGNED_SHORT_1_5_5_5_REV: Incomplete
GL_UNSIGNED_SHORT_4_4_4_4: Incomplete
GL_UNSIGNED_SHORT_4_4_4_4_REV: Incomplete
GL_UNSIGNED_SHORT_5_5_5_1: Incomplete
GL_UNSIGNED_SHORT_5_6_5: Incomplete
GL_UNSIGNED_SHORT_5_6_5_REV: Incomplete

@_f
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height) -> None: ...
@_f
def glDrawRangeElements(mode, start, end, count, type, indices) -> None: ...
@_f
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels) -> None: ...
@_f
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels) -> None: ...
