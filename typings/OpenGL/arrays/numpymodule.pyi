import ctypes
from OpenGL import acceleratesupport as acceleratesupport, error as error
from OpenGL._bytes import long as long
from OpenGL.arrays import formathandler as formathandler
from OpenGL.raw.GL.VERSION import GL_1_1 as GL_1_1
from _typeshed import Incomplete

REGISTRY_NAME: str
c_void_p = ctypes.c_void_p
NumpyHandler: Incomplete
testArray: Incomplete

def dataPointer(cls, instance): ...

dataPointer: Incomplete

class NumpyHandler(formathandler.FormatHandler):
    HANDLED_TYPES: Incomplete
    dataPointer = dataPointer
    isOutput: bool
    ERROR_ON_COPY: Incomplete
    @classmethod
    def zeros(cls, dims, typeCode): ...
    @classmethod
    def arrayToGLType(cls, value): ...
    @classmethod
    def arraySize(cls, value, typeCode=None): ...
    @classmethod
    def arrayByteCount(cls, value, typeCode=None): ...
    @classmethod
    def asArray(cls, value, typeCode=None): ...
    @classmethod
    def contiguous(cls, source, typeCode=None): ...
    @classmethod
    def unitSize(cls, value, typeCode=None): ...
    @classmethod
    def dimensions(cls, value, typeCode=None): ...
    @classmethod
    def from_param(cls, instance, typeCode=None): ...

SHORT_TYPE: str
USHORT_TYPE: str

def lookupDtype(char): ...

ARRAY_TO_GL_TYPE_MAPPING: Incomplete
GL_TYPE_TO_ARRAY_MAPPING: Incomplete
