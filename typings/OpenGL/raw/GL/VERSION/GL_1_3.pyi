from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ACTIVE_TEXTURE: Incomplete
GL_ADD_SIGNED: Incomplete
GL_CLAMP_TO_BORDER: Incomplete
GL_CLIENT_ACTIVE_TEXTURE: Incomplete
GL_COMBINE: Incomplete
GL_COMBINE_ALPHA: Incomplete
GL_COMBINE_RGB: Incomplete
GL_COMPRESSED_ALPHA: Incomplete
GL_COMPRESSED_INTENSITY: Incomplete
GL_COMPRESSED_LUMINANCE: Incomplete
GL_COMPRESSED_LUMINANCE_ALPHA: Incomplete
GL_COMPRESSED_RGB: Incomplete
GL_COMPRESSED_RGBA: Incomplete
GL_COMPRESSED_TEXTURE_FORMATS: Incomplete
GL_CONSTANT: Incomplete
GL_DOT3_RGB: Incomplete
GL_DOT3_RGBA: Incomplete
GL_INTERPOLATE: Incomplete
GL_MAX_CUBE_MAP_TEXTURE_SIZE: Incomplete
GL_MAX_TEXTURE_UNITS: Incomplete
GL_MULTISAMPLE: Incomplete
GL_MULTISAMPLE_BIT: Incomplete
GL_NORMAL_MAP: Incomplete
GL_NUM_COMPRESSED_TEXTURE_FORMATS: Incomplete
GL_OPERAND0_ALPHA: Incomplete
GL_OPERAND0_RGB: Incomplete
GL_OPERAND1_ALPHA: Incomplete
GL_OPERAND1_RGB: Incomplete
GL_OPERAND2_ALPHA: Incomplete
GL_OPERAND2_RGB: Incomplete
GL_PREVIOUS: Incomplete
GL_PRIMARY_COLOR: Incomplete
GL_PROXY_TEXTURE_CUBE_MAP: Incomplete
GL_REFLECTION_MAP: Incomplete
GL_RGB_SCALE: Incomplete
GL_SAMPLES: Incomplete
GL_SAMPLE_ALPHA_TO_COVERAGE: Incomplete
GL_SAMPLE_ALPHA_TO_ONE: Incomplete
GL_SAMPLE_BUFFERS: Incomplete
GL_SAMPLE_COVERAGE: Incomplete
GL_SAMPLE_COVERAGE_INVERT: Incomplete
GL_SAMPLE_COVERAGE_VALUE: Incomplete
GL_SOURCE0_ALPHA: Incomplete
GL_SOURCE0_RGB: Incomplete
GL_SOURCE1_ALPHA: Incomplete
GL_SOURCE1_RGB: Incomplete
GL_SOURCE2_ALPHA: Incomplete
GL_SOURCE2_RGB: Incomplete
GL_SUBTRACT: Incomplete
GL_TEXTURE0: Incomplete
GL_TEXTURE1: Incomplete
GL_TEXTURE10: Incomplete
GL_TEXTURE11: Incomplete
GL_TEXTURE12: Incomplete
GL_TEXTURE13: Incomplete
GL_TEXTURE14: Incomplete
GL_TEXTURE15: Incomplete
GL_TEXTURE16: Incomplete
GL_TEXTURE17: Incomplete
GL_TEXTURE18: Incomplete
GL_TEXTURE19: Incomplete
GL_TEXTURE2: Incomplete
GL_TEXTURE20: Incomplete
GL_TEXTURE21: Incomplete
GL_TEXTURE22: Incomplete
GL_TEXTURE23: Incomplete
GL_TEXTURE24: Incomplete
GL_TEXTURE25: Incomplete
GL_TEXTURE26: Incomplete
GL_TEXTURE27: Incomplete
GL_TEXTURE28: Incomplete
GL_TEXTURE29: Incomplete
GL_TEXTURE3: Incomplete
GL_TEXTURE30: Incomplete
GL_TEXTURE31: Incomplete
GL_TEXTURE4: Incomplete
GL_TEXTURE5: Incomplete
GL_TEXTURE6: Incomplete
GL_TEXTURE7: Incomplete
GL_TEXTURE8: Incomplete
GL_TEXTURE9: Incomplete
GL_TEXTURE_BINDING_CUBE_MAP: Incomplete
GL_TEXTURE_COMPRESSED: Incomplete
GL_TEXTURE_COMPRESSED_IMAGE_SIZE: Incomplete
GL_TEXTURE_COMPRESSION_HINT: Incomplete
GL_TEXTURE_CUBE_MAP: Incomplete
GL_TEXTURE_CUBE_MAP_NEGATIVE_X: Incomplete
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: Incomplete
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: Incomplete
GL_TEXTURE_CUBE_MAP_POSITIVE_X: Incomplete
GL_TEXTURE_CUBE_MAP_POSITIVE_Y: Incomplete
GL_TEXTURE_CUBE_MAP_POSITIVE_Z: Incomplete
GL_TRANSPOSE_COLOR_MATRIX: Incomplete
GL_TRANSPOSE_MODELVIEW_MATRIX: Incomplete
GL_TRANSPOSE_PROJECTION_MATRIX: Incomplete
GL_TRANSPOSE_TEXTURE_MATRIX: Incomplete

@_f
def glActiveTexture(texture) -> None: ...
@_f
def glClientActiveTexture(texture) -> None: ...
@_f
def glCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data) -> None: ...
@_f
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data) -> None: ...
@_f
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data) -> None: ...
@_f
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data) -> None: ...
@_f
def glGetCompressedTexImage(target, level, img) -> None: ...
@_f
def glLoadTransposeMatrixd(m) -> None: ...
@_f
def glLoadTransposeMatrixf(m) -> None: ...
@_f
def glMultTransposeMatrixd(m) -> None: ...
@_f
def glMultTransposeMatrixf(m) -> None: ...
@_f
def glMultiTexCoord1d(target, s) -> None: ...
@_f
def glMultiTexCoord1dv(target, v) -> None: ...
@_f
def glMultiTexCoord1f(target, s) -> None: ...
@_f
def glMultiTexCoord1fv(target, v) -> None: ...
@_f
def glMultiTexCoord1i(target, s) -> None: ...
@_f
def glMultiTexCoord1iv(target, v) -> None: ...
@_f
def glMultiTexCoord1s(target, s) -> None: ...
@_f
def glMultiTexCoord1sv(target, v) -> None: ...
@_f
def glMultiTexCoord2d(target, s, t) -> None: ...
@_f
def glMultiTexCoord2dv(target, v) -> None: ...
@_f
def glMultiTexCoord2f(target, s, t) -> None: ...
@_f
def glMultiTexCoord2fv(target, v) -> None: ...
@_f
def glMultiTexCoord2i(target, s, t) -> None: ...
@_f
def glMultiTexCoord2iv(target, v) -> None: ...
@_f
def glMultiTexCoord2s(target, s, t) -> None: ...
@_f
def glMultiTexCoord2sv(target, v) -> None: ...
@_f
def glMultiTexCoord3d(target, s, t, r) -> None: ...
@_f
def glMultiTexCoord3dv(target, v) -> None: ...
@_f
def glMultiTexCoord3f(target, s, t, r) -> None: ...
@_f
def glMultiTexCoord3fv(target, v) -> None: ...
@_f
def glMultiTexCoord3i(target, s, t, r) -> None: ...
@_f
def glMultiTexCoord3iv(target, v) -> None: ...
@_f
def glMultiTexCoord3s(target, s, t, r) -> None: ...
@_f
def glMultiTexCoord3sv(target, v) -> None: ...
@_f
def glMultiTexCoord4d(target, s, t, r, q) -> None: ...
@_f
def glMultiTexCoord4dv(target, v) -> None: ...
@_f
def glMultiTexCoord4f(target, s, t, r, q) -> None: ...
@_f
def glMultiTexCoord4fv(target, v) -> None: ...
@_f
def glMultiTexCoord4i(target, s, t, r, q) -> None: ...
@_f
def glMultiTexCoord4iv(target, v) -> None: ...
@_f
def glMultiTexCoord4s(target, s, t, r, q) -> None: ...
@_f
def glMultiTexCoord4sv(target, v) -> None: ...
@_f
def glSampleCoverage(value, invert) -> None: ...
