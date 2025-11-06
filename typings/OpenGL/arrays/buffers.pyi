from OpenGL import acceleratesupport as acceleratesupport
from OpenGL.arrays import formathandler as formathandler
from OpenGL_accelerate.buffers_formathandler import MemoryviewHandler
from _typeshed import Incomplete

MemoryviewHandler: Incomplete
BufferHandler: Incomplete
BufferHandler = MemoryviewHandler

class BufferHandler(formathandler.FormatHandler):
    isOutput: bool
    ERROR_ON_COPY: Incomplete
    @classmethod
    def from_param(cls, value, typeCode=None): ...
    def dataPointer(value): ...
    dataPointer: Incomplete
    @classmethod
    def zeros(cls, dims, typeCode=None): ...
    @classmethod
    def ones(cls, dims, typeCode=None) -> None: ...
    @classmethod
    def arrayToGLType(cls, value): ...
    @classmethod
    def arraySize(cls, value, typeCode=None): ...
    @classmethod
    def arrayByteCount(cls, value, typeCode=None): ...
    @classmethod
    def unitSize(cls, value, default=None): ...
    @classmethod
    def asArray(cls, value, typeCode=None): ...
    @classmethod
    def dimensions(cls, value, typeCode=None): ...

ARRAY_TO_GL_TYPE_MAPPING: Incomplete
BYTE_SIZES: Incomplete
