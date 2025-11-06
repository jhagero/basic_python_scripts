from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_NUM_PROGRAM_BINARY_FORMATS: Incomplete
GL_PROGRAM_BINARY_FORMATS: Incomplete
GL_PROGRAM_BINARY_LENGTH: Incomplete
GL_PROGRAM_BINARY_RETRIEVABLE_HINT: Incomplete

@_f
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary) -> None: ...
@_f
def glProgramBinary(program, binaryFormat, binary, length) -> None: ...
@_f
def glProgramParameteri(program, pname, value) -> None: ...
