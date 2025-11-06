from OpenGL.raw import GLU as _simple
from _typeshed import Incomplete

__all__ = ['gluNewQuadric', 'gluQuadricCallback', 'GLUQuadric']

class GLUQuadric(_simple.GLUquadric):
    FUNCTION_TYPE: Incomplete
    CALLBACK_TYPES: Incomplete
    callbacks: Incomplete
    def addCallback(self, which, function): ...
GLUquadric = GLUQuadric

def gluQuadricCallback(quadric, which=..., function=None): ...

gluNewQuadric: Incomplete
