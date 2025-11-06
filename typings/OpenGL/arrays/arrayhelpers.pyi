from OpenGL import acceleratesupport as acceleratesupport, contextdata as contextdata, converters as converters, error as error
from OpenGL._bytes import bytes as bytes, unicode as unicode
from OpenGL.arrays import arraydatatype as arraydatatype
from OpenGL_accelerate.arraydatatype import AsArrayOfType as AsArrayOfType, AsArrayTyped as AsArrayTyped, AsArrayTypedSize as AsArrayTypedSize, AsArrayTypedSizeChecked
from _typeshed import Incomplete

AsArrayTypedSizeChecked: Incomplete

def returnPointer(result, baseOperation, pyArgs, cArgs): ...

class AsArrayOfType(converters.PyConverter):
    argNames: Incomplete
    indexLookups: Incomplete
    arrayName: Incomplete
    typeName: Incomplete
    def __init__(self, arrayName: str = 'pointer', typeName: str = 'type') -> None: ...
    def __call__(self, arg, wrappedOperation, args): ...

class AsArrayTyped(converters.PyConverter):
    argNames: Incomplete
    indexLookups: Incomplete
    arrayName: Incomplete
    arrayType: Incomplete
    def __init__(self, arrayName: str = 'pointer', arrayType=None) -> None: ...
    def __call__(self, arg, wrappedOperation, args): ...

class AsArrayTypedSize(converters.CConverter):
    argNames: Incomplete
    indexLookups: Incomplete
    arrayName: Incomplete
    arrayType: Incomplete
    def __init__(self, arrayName: str = 'pointer', arrayType=None) -> None: ...
    def __call__(self, pyArgs, index, wrappedOperation): ...

returnPointer: Incomplete

def asArrayType(typ, size=None): ...
asArrayTypeSize = asArrayType
asArrayTypeSize = AsArrayTypedSizeChecked

def asVoidArray(): ...

class storePointerType:
    pointerName: Incomplete
    constant: Incomplete
    def __init__(self, pointerName, constant) -> None: ...
    pointerIndex: Incomplete
    def finalise(self, wrapper) -> None: ...
    def __call__(self, result, baseOperation, pyArgs, cArgs) -> None: ...

def setInputArraySizeType(baseOperation, size, type, argName: int = 0): ...
def arraySizeOfFirstType(typ, default): ...
