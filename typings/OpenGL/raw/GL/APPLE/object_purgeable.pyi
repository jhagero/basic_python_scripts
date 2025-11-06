from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BUFFER_OBJECT_APPLE: Incomplete
GL_PURGEABLE_APPLE: Incomplete
GL_RELEASED_APPLE: Incomplete
GL_RETAINED_APPLE: Incomplete
GL_UNDEFINED_APPLE: Incomplete
GL_VOLATILE_APPLE: Incomplete

@_f
def glGetObjectParameterivAPPLE(objectType, name, pname, params) -> None: ...
@_f
def glObjectPurgeableAPPLE(objectType, name, option) -> None: ...
@_f
def glObjectUnpurgeableAPPLE(objectType, name, option) -> None: ...
