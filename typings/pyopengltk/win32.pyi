from _typeshed import Incomplete
from pyopengltk.base import BaseOpenGLFrame as BaseOpenGLFrame

GetDC: Incomplete
pfd: Incomplete
PFD_TYPE_RGBA: int
PFD_MAIN_PLANE: int
PFD_DOUBLEBUFFER: int
PFD_DRAW_TO_WINDOW: int
PFD_SUPPORT_OPENGL: int

class OpenGLFrame(BaseOpenGLFrame):
    def tkCreateContext(self) -> None: ...
    def tkMakeCurrent(self) -> None: ...
    def tkSwapBuffers(self) -> None: ...
