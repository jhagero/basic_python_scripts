from OpenGL import acceleratesupport as acceleratesupport
from OpenGL._bytes import as_8_bit as as_8_bit, bytes as bytes, unicode as unicode
from OpenGL._null import NULL as NULL
from OpenGL_accelerate.arraydatatype import Output, SizedOutput
from OpenGL_accelerate.wrapper import DefaultCConverter as DefaultCConverter, getPyArgsName as getPyArgsName, returnCArgument as returnCArgument, returnPyArgument as returnPyArgument
from _typeshed import Incomplete

class Converter:
    argNames: Incomplete
    indexLookups: Incomplete
    def __init__(self, *args, **named) -> None: ...
    def finalise(self, wrapper) -> None: ...

class PyConverter(Converter):
    def __call__(self, incoming, function, arguments) -> None: ...

class CConverter(Converter):
    def __call__(self, pyArgs, index, baseOperation) -> None: ...

class ReturnValues(Converter):
    def __call__(self, result, baseOperation, pyArgs, cArgs) -> None: ...

CallFuncPyConverter: Incomplete

class CallFuncPyConverter(PyConverter):
    function: Incomplete
    def __init__(self, function) -> None: ...
    def __call__(self, incoming, function, argument): ...

class DefaultCConverter(CConverter):
    index: Incomplete
    def __init__(self, index) -> None: ...
    def __call__(self, pyArgs, index, wrapper): ...

class getPyArgsName(CConverter):
    argNames: Incomplete
    indexLookups: Incomplete
    def __call__(self, pyArgs, index, baseOperation): ...

class Output(CConverter):
    argNames: Incomplete
    indexLookups: Incomplete
    def __call__(self, pyArgs, index, baseOperation): ...
    def getSize(self, pyArgs): ...
    def oldStyleReturn(self, result, baseOperation, pyArgs, cArgs): ...

class OutputOrInput(Output):
    DO_OUTPUT: Incomplete
    def __call__(self, pyArgs, index, baseOperation): ...

class SizedOutput(Output):
    argNames: Incomplete
    indexLookups: Incomplete
    def getSize(self, pyArgs): ...

class SizedOutputOrInput(SizedOutput):
    DO_OUTPUT: Incomplete
    def __call__(self, pyArgs, index, baseOperation): ...

class returnCArgument(ReturnValues):
    argNames: Incomplete
    indexLookups: Incomplete
    def __call__(self, result, baseOperation, pyArgs, cArgs): ...

class returnPyArgument(ReturnValues):
    argNames: Incomplete
    indexLookups: Incomplete
    def __call__(self, result, baseOperation, pyArgs, cArgs): ...

class StringLengths(CConverter):
    argNames: Incomplete
    indexLookups: Incomplete
    def __call__(self, pyArgs, index, baseOperation): ...
    def totalCount(self, pyArgs, index, baseOperation): ...
    def stringArray(self, arg, baseOperation, args): ...
    def stringArrayForC(self, strings): ...
