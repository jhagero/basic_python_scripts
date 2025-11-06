from OpenGL.raw.GL.ARB.sync import *
from OpenGL import arrays as arrays, constant as constant, extensions as extensions, platform as platform, wrapper as wrapper
from OpenGL.arrays import GLintArray as GLintArray
from OpenGL.raw.GL._types import GLint as GLint
from _typeshed import Incomplete

def glInitSyncARB(): ...

glGetInteger64v: Incomplete
glGetSynciv: Incomplete

def glGetSync(sync, pname, bufSize: int = 1, length=None, values=None): ...
