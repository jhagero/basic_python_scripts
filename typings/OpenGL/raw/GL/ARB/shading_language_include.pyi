from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_NAMED_STRING_LENGTH_ARB: Incomplete
GL_NAMED_STRING_TYPE_ARB: Incomplete
GL_SHADER_INCLUDE_ARB: Incomplete

@_f
def glCompileShaderIncludeARB(shader, count, path, length) -> None: ...
@_f
def glDeleteNamedStringARB(namelen, name) -> None: ...
@_f
def glGetNamedStringARB(namelen, name, bufSize, stringlen, string) -> None: ...
@_f
def glGetNamedStringivARB(namelen, name, pname, params) -> None: ...
@_f
def glIsNamedStringARB(namelen, name) -> None: ...
@_f
def glNamedStringARB(type, namelen, name, stringlen, string) -> None: ...
