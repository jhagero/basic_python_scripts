from OpenGL import constant as constant, error as error
from OpenGL.arrays import buffers as buffers
from OpenGL.raw.GL.VERSION import GL_1_1 as GL_1_1
from _typeshed import Incomplete

REGISTRY_NAME: str

class NumpyHandler(buffers.BufferHandler):
    @classmethod
    def zeros(cls, dims, typeCode): ...
    @classmethod
    def asArray(cls, value, typeCode=None): ...
    @classmethod
    def contiguous(cls, source, typeCode=None): ...

SHORT_TYPE: str
USHORT_TYPE: str

def lookupDtype(char): ...

ARRAY_TO_GL_TYPE_MAPPING: Incomplete
GL_TYPE_TO_ARRAY_MAPPING: Incomplete
