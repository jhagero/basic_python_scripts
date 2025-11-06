from OpenGL import arrays as arrays, wrapper as wrapper
from _typeshed import Incomplete

class _lengthOfArgname:
    arrayName: Incomplete
    divisor: Incomplete
    arrayType: Incomplete
    def __init__(self, arrayName, divisor, arrayType=...) -> None: ...
    arrayIndex: Incomplete
    def finalise(self, wrapper) -> None: ...
    def __call__(self, pyArgs, index, wrappedOperation): ...

gleLathe: Incomplete
glePolyCone: Incomplete
glePolyCylinder: Incomplete
gleScrew: Incomplete
gleSpiral: Incomplete
gleExtrusion: Incomplete
gleSuperExtrusion: Incomplete
gleTwistExtrusion: Incomplete
