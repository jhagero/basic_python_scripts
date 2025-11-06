import ctypes
from OpenGL import acceleratesupport as acceleratesupport, logs as logs, plugins as plugins
from OpenGL.arrays import formathandler as formathandler
from _typeshed import Incomplete

unicode = str
ADT: Incomplete

class HandlerRegistry(dict):
    GENERIC_OUTPUT_PREFERENCES: Incomplete
    match: Incomplete
    output_handler: Incomplete
    preferredOutput: Incomplete
    all_output_handlers: Incomplete
    def __init__(self, plugin_match) -> None: ...
    def __call__(self, value): ...
    def handler_by_plugin_name(self, name): ...
    def get_output_handler(self): ...
    def register(self, handler, types=None) -> None: ...
    def registerReturn(self, handler) -> None: ...

GLOBAL_REGISTRY: Incomplete

class ArrayDatatype:
    typeConstant: Incomplete
    handler = GLOBAL_REGISTRY
    getHandler: Incomplete
    returnHandler: Incomplete
    isAccelerated: bool
    @classmethod
    def getRegistry(cls): ...
    def from_param(cls, value, typeConstant=None): ...
    from_param: Incomplete
    def dataPointer(cls, value): ...
    dataPointer: Incomplete
    def voidDataPointer(cls, value): ...
    voidDataPointer: Incomplete
    def typedPointer(cls, value): ...
    typedPointer: Incomplete
    def asArray(cls, value, typeCode=None): ...
    asArray: Incomplete
    def arrayToGLType(cls, value): ...
    arrayToGLType: Incomplete
    def arraySize(cls, value, typeCode=None): ...
    arraySize: Incomplete
    def unitSize(cls, value, typeCode=None): ...
    unitSize: Incomplete
    def zeros(cls, dims, typeCode=None): ...
    zeros: Incomplete
    def dimensions(cls, value): ...
    dimensions: Incomplete
    def arrayByteCount(cls, value): ...
    arrayByteCount: Incomplete

class GLclampdArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLclampfArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLfloat16Array(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLfloatArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLdoubleArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLbyteArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLcharArray(ArrayDatatype, ctypes.c_char_p):
    baseType: Incomplete
    typeConstant: Incomplete
GLcharARBArray = GLcharArray

class GLshortArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLintArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLubyteArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete
GLbooleanArray = GLubyteArray

class GLushortArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLuintArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLint64Array(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLuint64Array(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLenumArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLsizeiArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLvoidpArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete

class GLfixedArray(ArrayDatatype, Incomplete):
    baseType: Incomplete
    typeConstant: Incomplete
EGLAttribArray = GLintArray
GL_CONSTANT_TO_ARRAY_TYPE: Incomplete
