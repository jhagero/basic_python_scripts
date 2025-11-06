from OpenGL.raw.GLX._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GLX_ACCUM_ALPHA_SIZE: Incomplete
GLX_ACCUM_BLUE_SIZE: Incomplete
GLX_ACCUM_GREEN_SIZE: Incomplete
GLX_ACCUM_RED_SIZE: Incomplete
GLX_ALPHA_SIZE: Incomplete
GLX_AUX_BUFFERS: Incomplete
GLX_BAD_ATTRIBUTE: Incomplete
GLX_BAD_CONTEXT: Incomplete
GLX_BAD_ENUM: Incomplete
GLX_BAD_SCREEN: Incomplete
GLX_BAD_VALUE: Incomplete
GLX_BAD_VISUAL: Incomplete
GLX_BLUE_SIZE: Incomplete
GLX_BUFFER_SIZE: Incomplete
GLX_BufferSwapComplete: Incomplete
GLX_DEPTH_SIZE: Incomplete
GLX_DOUBLEBUFFER: Incomplete
GLX_GREEN_SIZE: Incomplete
GLX_LEVEL: Incomplete
GLX_NO_EXTENSION: Incomplete
GLX_PbufferClobber: Incomplete
GLX_RED_SIZE: Incomplete
GLX_RGBA: Incomplete
GLX_STENCIL_SIZE: Incomplete
GLX_STEREO: Incomplete
GLX_USE_GL: Incomplete

@_f
def glXChooseVisual(dpy, screen, attribList) -> None: ...
@_f
def glXCopyContext(dpy, src, dst, mask) -> None: ...
@_f
def glXCreateContext(dpy, vis, shareList, direct) -> None: ...
@_f
def glXCreateGLXPixmap(dpy, visual, pixmap) -> None: ...
@_f
def glXDestroyContext(dpy, ctx) -> None: ...
@_f
def glXDestroyGLXPixmap(dpy, pixmap) -> None: ...
@_f
def glXGetConfig(dpy, visual, attrib, value) -> None: ...
@_f
def glXGetCurrentContext() -> None: ...
@_f
def glXGetCurrentDrawable() -> None: ...
@_f
def glXIsDirect(dpy, ctx) -> None: ...
@_f
def glXMakeCurrent(dpy, drawable, ctx) -> None: ...
@_f
def glXQueryExtension(dpy, errorb, event) -> None: ...
@_f
def glXQueryVersion(dpy, maj, min) -> None: ...
@_f
def glXSwapBuffers(dpy, drawable) -> None: ...
@_f
def glXUseXFont(font, first, count, list) -> None: ...
@_f
def glXWaitGL() -> None: ...
@_f
def glXWaitX() -> None: ...
