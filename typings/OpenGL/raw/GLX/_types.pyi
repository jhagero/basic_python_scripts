from ctypes import *
from OpenGL.raw.GL._types import *
from OpenGL import constant as constant, extensions as extensions
from OpenGL._bytes import as_8_bit as as_8_bit
from _typeshed import Incomplete

c_void: Incomplete
void: Incomplete
Bool = c_uint

class _GLXQuerier(extensions.ExtensionQuerier):
    prefix: Incomplete
    assumed_version: Incomplete
    version_prefix: Incomplete
    def getDisplay(self): ...
    def getScreen(self, display): ...
    def pullVersion(self): ...
    def pullExtensions(self): ...

GLXQuerier: Incomplete

class struct___GLXcontextRec(Structure): ...
class struct___GLXcontextRec(Structure): ...

GLXContext: Incomplete
XID = c_ulong
GLXPixmap = XID
GLXDrawable = XID

class struct___GLXFBConfigRec(Structure): ...
class struct___GLXFBConfigRec(Structure): ...

GLXFBConfig: Incomplete
GLXFBConfigID = XID
GLXContextID = XID
GLXWindow = XID
GLXPbuffer = XID
GLXPbufferSGIX = XID
GLXVideoSourceSGIX = XID

class struct_anon_103(Structure): ...
class struct_anon_18(Structure): ...
class struct__XExtData(Structure): ...
XPointer = c_char_p
XExtData = struct__XExtData
VisualID = c_ulong
Visual = struct_anon_18
XVisualInfo = struct_anon_103

class struct__XDisplay(Structure): ...
class struct__XDisplay(Structure): ...
Display = struct__XDisplay
Pixmap = XID
Font = XID
Window = XID
GLX_ARB_get_proc_address: Incomplete

class struct_anon_111(Structure): ...
GLXPbufferClobberEvent = struct_anon_111

class struct_anon_112(Structure): ...
GLXBufferSwapComplete = struct_anon_112

class struct___GLXEvent(Union): ...
GLXEvent = struct___GLXEvent

class GLXHyperpipeConfigSGIX(Structure): ...
