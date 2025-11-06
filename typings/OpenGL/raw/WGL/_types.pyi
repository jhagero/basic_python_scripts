from ctypes import *
from OpenGL.raw.GL._types import *
from OpenGL import extensions as extensions
from OpenGL._bytes import as_8_bit as as_8_bit
from _typeshed import Incomplete
from ctypes import _SimpleCData

c_void: Incomplete

class _WGLQuerier(extensions.ExtensionQuerier):
    prefix: bytes
    assumed_version: Incomplete
    version_prefix: bytes
    def pullVersion(self): ...
    def pullExtensions(self): ...

WGLQuerier: Incomplete
INT8 = c_char
PINT8 = c_char_p
INT16 = c_short
PINT16: Incomplete
INT32 = c_int
PINT32: Incomplete
UINT8 = c_ubyte
PUINT8: Incomplete
UINT16 = c_ushort
PUINT16: Incomplete
UINT32 = c_uint
PUINT32: Incomplete
LONG32 = c_int
PLONG32: Incomplete
ULONG32 = c_uint
PULONG32: Incomplete
DWORD32 = c_uint
PDWORD32: Incomplete
INT64 = c_longlong
PINT64: Incomplete
UINT64 = c_ulonglong
PUINT64: Incomplete
VOID: Incomplete
LPVOID: Incomplete
LPCSTR = c_char_p
CHAR = c_char
BYTE = c_ubyte
WORD = c_ushort
USHORT = c_ushort
UINT = c_uint
INT = c_int
INT_PTR: Incomplete
BOOL = c_long
LONG = c_long
DWORD = c_ulong
FLOAT = c_float
COLORREF = DWORD
LPCOLORREF: Incomplete

class HANDLE(_SimpleCData): ...
HGLRC = HANDLE
HDC = HANDLE
PROC: Incomplete
HPBUFFERARB = HANDLE
HPBUFFEREXT = HANDLE

class struct__POINTFLOAT(Structure): ...
POINTFLOAT = struct__POINTFLOAT
PPOINTFLOAT: Incomplete

class struct__GLYPHMETRICSFLOAT(Structure): ...
GLYPHMETRICSFLOAT = struct__GLYPHMETRICSFLOAT
PGLYPHMETRICSFLOAT: Incomplete
LPGLYPHMETRICSFLOAT: Incomplete

class struct_tagLAYERPLANEDESCRIPTOR(Structure): ...
LAYERPLANEDESCRIPTOR = struct_tagLAYERPLANEDESCRIPTOR
PLAYERPLANEDESCRIPTOR: Incomplete
LPLAYERPLANEDESCRIPTOR: Incomplete

class struct__WGLSWAP(Structure): ...
WGLSWAP = struct__WGLSWAP
PWGLSWAP: Incomplete
LPWGLSWAP: Incomplete

class struct_tagRECT(Structure): ...
RECT = struct_tagRECT
PRECT: Incomplete
NPRECT: Incomplete
LPRECT: Incomplete

class PIXELFORMATDESCRIPTOR(Structure): ...

HENHMETAFILE: Incomplete
