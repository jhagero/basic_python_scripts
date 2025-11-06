from OpenGL import contextdata as contextdata, error as error, logs as logs, platform as platform
from OpenGL._bytes import as_8_bit as as_8_bit, bytes as bytes, integer_types as integer_types, long as long, unicode as unicode
from OpenGL.platform import CurrentContextIsValid as CurrentContextIsValid, GLUT_GUARD_CALLBACKS as GLUT_GUARD_CALLBACKS, PLATFORM as PLATFORM
from _typeshed import Incomplete

GLUT: Incomplete
FUNCTION_TYPE: Incomplete

def glutCreateWindow(title): ...
def glutCreateMenu(callback): ...

class GLUTCallback:
    typeName: Incomplete
    __doc__: Incomplete
    wrappedOperation: Incomplete
    callbackType: Incomplete
    CONTEXT_DATA_KEY: Incomplete
    def __init__(self, typeName, parameterTypes, parameterNames) -> None: ...
    argNames: Incomplete
    def __call__(self, function, *args): ...

class GLUTTimerCallback(GLUTCallback):
    def __call__(self, milliseconds, function, value): ...

class GLUTMenuCallback:
    callbackType: Incomplete
    def glutCreateMenu(cls, func): ...
    glutCreateMenu: Incomplete
    def glutDestroyMenu(cls, menu): ...
    glutDestroyMenu: Incomplete

glutCreateMenu: Incomplete
glutDestroyMenu: Incomplete
glutButtonBoxFunc: Incomplete
glutDialsFunc: Incomplete
glutDisplayFunc: Incomplete
glutEntryFunc: Incomplete
glutIdleFunc: Incomplete
glutJoystickFunc: Incomplete
glutKeyboardFunc: Incomplete
glutKeyboardUpFunc: Incomplete
glutMenuStatusFunc: Incomplete
glutMenuStateFunc: Incomplete
glutMotionFunc: Incomplete
glutMouseFunc: Incomplete
glutOverlayDisplayFunc: Incomplete
glutPassiveMotionFunc: Incomplete
glutReshapeFunc: Incomplete
glutSpaceballButtonFunc: Incomplete
glutSpaceballMotionFunc: Incomplete
glutSpaceballRotateFunc: Incomplete
glutSpecialFunc: Incomplete
glutSpecialUpFunc: Incomplete
glutTabletButtonFunc: Incomplete
glutTabletMotionFunc: Incomplete
glutVisibilityFunc: Incomplete
glutWindowStatusFunc: Incomplete
glutTimerFunc: Incomplete
INITIALIZED: bool

def glutInit(*args): ...
def glutDestroyWindow(window): ...
