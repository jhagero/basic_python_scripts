import ctypes
from OpenGL import extensions as extensions
from OpenGL._bytes import as_8_bit as as_8_bit
from _typeshed import Incomplete

class _EGLQuerier(extensions.ExtensionQuerier):
    prefix: Incomplete
    assumed_version: Incomplete
    version_prefix: Incomplete
    def getDisplay(self): ...
    def pullVersion(self): ...
    def pullExtensions(self): ...

EGLQuerier: Incomplete
EGLBoolean = ctypes.c_uint32
EGLenum = ctypes.c_uint32
EGLint = ctypes.c_int32
c_int = ctypes.c_int32
EGLConfig: Incomplete
EGLContext: Incomplete
EGLDisplay: Incomplete
EGLSurface: Incomplete
EGLClientBuffer: Incomplete
EGLImageKHR: Incomplete
EGLImage: Incomplete
EGLDeviceEXT: Incomplete
EGLOutputLayerEXT: Incomplete
EGLOutputPortEXT: Incomplete
EGLScreenMESA = ctypes.c_ulong
EGLModeMESA = ctypes.c_ulong
EGLNativeFileDescriptorKHR = ctypes.c_int
EGLSyncKHR: Incomplete
EGLSyncNV: Incomplete
EGLSync: Incomplete
EGLTimeKHR = ctypes.c_ulonglong
EGLTimeNV = ctypes.c_ulonglong
EGLTime = ctypes.c_ulonglong
EGLuint64KHR = ctypes.c_ulonglong
EGLuint64NV = ctypes.c_ulonglong
EGLStreamKHR: Incomplete
EGLsizeiANDROID = ctypes.c_size_t
EGLAttribKHR: Incomplete
EGLAttrib: Incomplete

class EGLClientPixmapHI(ctypes.Structure): ...
class wl_display(ctypes.Structure): ...

EGLNativeDisplayType: Incomplete
EGLNativePixmapType: Incomplete
EGLNativeWindowType: Incomplete
NativeDisplayType = EGLNativeDisplayType
NativePixmapType = EGLNativePixmapType
NativeWindowType = EGLNativeWindowType
CALLBACK_TYPE: Incomplete
EGLSetBlobFuncANDROID: Incomplete
EGLGetBlobFuncANDROID: Incomplete
EGL_DEFAULT_DISPLAY: Incomplete
EGL_NO_CONTEXT: Incomplete
EGL_NO_DISPLAY: Incomplete
EGL_NO_SURFACE: Incomplete
EGL_DONT_CARE: int
raw_eglQueryString: Incomplete
