from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COMPRESSED_SLUMINANCE: Incomplete
GL_COMPRESSED_SLUMINANCE_ALPHA: Incomplete
GL_COMPRESSED_SRGB: Incomplete
GL_COMPRESSED_SRGB_ALPHA: Incomplete
GL_CURRENT_RASTER_SECONDARY_COLOR: Incomplete
GL_FLOAT_MAT2x3: Incomplete
GL_FLOAT_MAT2x4: Incomplete
GL_FLOAT_MAT3x2: Incomplete
GL_FLOAT_MAT3x4: Incomplete
GL_FLOAT_MAT4x2: Incomplete
GL_FLOAT_MAT4x3: Incomplete
GL_PIXEL_PACK_BUFFER: Incomplete
GL_PIXEL_PACK_BUFFER_BINDING: Incomplete
GL_PIXEL_UNPACK_BUFFER: Incomplete
GL_PIXEL_UNPACK_BUFFER_BINDING: Incomplete
GL_SLUMINANCE: Incomplete
GL_SLUMINANCE8: Incomplete
GL_SLUMINANCE8_ALPHA8: Incomplete
GL_SLUMINANCE_ALPHA: Incomplete
GL_SRGB: Incomplete
GL_SRGB8: Incomplete
GL_SRGB8_ALPHA8: Incomplete
GL_SRGB_ALPHA: Incomplete

@_f
def glUniformMatrix2x3fv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix2x4fv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3x2fv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix3x4fv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4x2fv(location, count, transpose, value) -> None: ...
@_f
def glUniformMatrix4x3fv(location, count, transpose, value) -> None: ...
