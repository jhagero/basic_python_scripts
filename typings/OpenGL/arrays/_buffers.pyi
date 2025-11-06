from ._arrayconstants import *
import ctypes
from _typeshed import Incomplete

PyBUF_SIMPLE: int
PyBUF_WRITABLE: int
PyBUF_WRITEABLE: int
PyBUF_ND: int
PyBUF_STRIDES: Incomplete
PyBUF_CONTIG = PyBUF_ND | PyBUF_WRITABLE
PyBUF_CONTIG_RO = PyBUF_ND
PyBUF_C_CONTIGUOUS: Incomplete
PyBUF_FORMAT: int
c_ssize_t: Incomplete

class Py_buffer(ctypes.Structure):
    @classmethod
    def from_object(cls, object, flags=...): ...
    @property
    def dims(self): ...
    def __len__(self) -> int: ...
    @property
    def dim_strides(self): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type=None, exc_value=None, traceback=None) -> None: ...
    def __del__(self) -> None: ...

BUFFER_POINTER: Incomplete
CheckBuffer: Incomplete
IncRef: Incomplete
GetBuffer: Incomplete
ReleaseBuffer: Incomplete
