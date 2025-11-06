from OpenGL.raw.GLES2._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_NUM_PROGRAM_BINARY_FORMATS_OES: Incomplete
GL_PROGRAM_BINARY_FORMATS_OES: Incomplete
GL_PROGRAM_BINARY_LENGTH_OES: Incomplete

@_f
def glGetProgramBinaryOES(program, bufSize, length, binaryFormat, binary) -> None: ...
@_f
def glProgramBinaryOES(program, binaryFormat, binary, length) -> None: ...
