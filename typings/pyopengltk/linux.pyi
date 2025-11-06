from _typeshed import Incomplete
from ctypes import CFUNCTYPE as CFUNCTYPE, c_void_p, pointer as pointer
from pyopengltk.base import BaseOpenGLFrame as BaseOpenGLFrame

XOpenDisplay: Incomplete
Colormap = c_void_p
att: Incomplete
fbatt: Incomplete

class OpenGLFrame(BaseOpenGLFrame):
    def tkCreateContext(self) -> None: ...
    def tkMakeCurrent(self) -> None: ...
    def tkSwapBuffers(self) -> None: ...
