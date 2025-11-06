from OpenGL import constant as constant, error as error
from OpenGL._bytes import as_8_bit as as_8_bit, bytes as bytes, unicode as unicode
from OpenGL._configflags import ERROR_ON_COPY as ERROR_ON_COPY
from OpenGL.arrays import formathandler as formathandler
from _typeshed import Incomplete
from collections.abc import Generator

REGISTRY_NAME: str
HANDLED_TYPES: Incomplete

def err_on_copy(func): ...

class ListHandler(formathandler.FormatHandler):
    @err_on_copy
    def from_param(self, instance, typeCode=None): ...
    dataPointer: Incomplete
    HANDLED_TYPES = HANDLED_TYPES
    isOutput: bool
    @err_on_copy
    @classmethod
    def voidDataPointer(cls, value): ...
    @classmethod
    def zeros(cls, dims, typeCode): ...
    @classmethod
    def dimsOf(cls, x): ...
    @classmethod
    def arrayToGLType(cls, value): ...
    @classmethod
    def arraySize(cls, value, typeCode=None): ...
    @classmethod
    def types(cls, value) -> Generator[Incomplete]: ...
    @classmethod
    def dims(cls, value) -> Generator[Incomplete]: ...
    @err_on_copy
    @classmethod
    def asArray(cls, value, typeCode=None): ...
    @err_on_copy
    @classmethod
    def unitSize(cls, value, typeCode=None): ...
    @err_on_copy
    @classmethod
    def dimensions(cls, value, typeCode=None): ...
    @classmethod
    def arrayByteCount(cls, value, typeCode=None): ...

ARRAY_TO_GL_TYPE_MAPPING: Incomplete
GL_TYPE_TO_ARRAY_MAPPING: Incomplete
