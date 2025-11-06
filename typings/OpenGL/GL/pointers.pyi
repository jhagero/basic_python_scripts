import ctypes
from _typeshed import Incomplete

__all__ = ['glColorPointer', 'glColorPointerb', 'glColorPointerd', 'glColorPointerf', 'glColorPointeri', 'glColorPointers', 'glColorPointerub', 'glColorPointerui', 'glColorPointerus', 'glEdgeFlagPointer', 'glEdgeFlagPointerb', 'glIndexPointer', 'glIndexPointerb', 'glIndexPointerd', 'glIndexPointerf', 'glIndexPointeri', 'glIndexPointers', 'glIndexPointerub', 'glNormalPointer', 'glNormalPointerb', 'glNormalPointerd', 'glNormalPointerf', 'glNormalPointeri', 'glNormalPointers', 'glTexCoordPointer', 'glTexCoordPointerb', 'glTexCoordPointerd', 'glTexCoordPointerf', 'glTexCoordPointeri', 'glTexCoordPointers', 'glVertexPointer', 'glVertexPointerb', 'glVertexPointerd', 'glVertexPointerf', 'glVertexPointeri', 'glVertexPointers', 'glDrawElements', 'glDrawElementsui', 'glDrawElementsub', 'glDrawElementsus', 'glFeedbackBuffer', 'glSelectBuffer', 'glRenderMode', 'glGetPointerv', 'glInterleavedArrays', 'GL_INTERLEAVED_ARRAY_POINTER']

GLsizei = ctypes.c_int
GLenum = ctypes.c_uint
GLint = ctypes.c_int
GL_INTERLEAVED_ARRAY_POINTER: Incomplete
glVertexPointer: Incomplete
glTexCoordPointer: Incomplete
glNormalPointer: Incomplete
glIndexPointer: Incomplete
glEdgeFlagPointer: Incomplete
glColorPointer: Incomplete
glInterleavedArrays: Incomplete
glDrawElements: Incomplete

def glSelectBuffer(size, buffer=None): ...
def glFeedbackBuffer(size, type, buffer=None): ...
def glRenderMode(newMode): ...
def glGetPointerv(constant): ...

# Names in __all__ with no definition:
#   glColorPointerb
#   glColorPointerd
#   glColorPointerf
#   glColorPointeri
#   glColorPointers
#   glColorPointerub
#   glColorPointerui
#   glColorPointerus
#   glDrawElementsub
#   glDrawElementsui
#   glDrawElementsus
#   glEdgeFlagPointerb
#   glIndexPointerb
#   glIndexPointerd
#   glIndexPointerf
#   glIndexPointeri
#   glIndexPointers
#   glIndexPointerub
#   glNormalPointerb
#   glNormalPointerd
#   glNormalPointerf
#   glNormalPointeri
#   glNormalPointers
#   glTexCoordPointerb
#   glTexCoordPointerd
#   glTexCoordPointerf
#   glTexCoordPointeri
#   glTexCoordPointers
#   glVertexPointerb
#   glVertexPointerd
#   glVertexPointerf
#   glVertexPointeri
#   glVertexPointers
