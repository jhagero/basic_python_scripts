from OpenGL._bytes import as_8_bit as as_8_bit, bytes as bytes, unicode as unicode
from OpenGL.latebind import LateBind as LateBind
from _typeshed import Incomplete

VERSION_PREFIX: Incomplete
CURRENT_GL_VERSION: Incomplete
AVAILABLE_GL_EXTENSIONS: Incomplete
AVAILABLE_GLU_EXTENSIONS: Incomplete
VERSION_EXTENSIONS: Incomplete

class ExtensionQuerier:
    prefix: Incomplete
    version_prefix: Incomplete
    assumed_version: Incomplete
    version: Incomplete
    extensions: Incomplete
    version_string: Incomplete
    extensions_string: Incomplete
    registered: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def hasExtension(self, specifier): ...
    def __call__(self, specifier): ...
    def getVersion(self): ...
    def getExtensions(self): ...

class _GLQuerier(ExtensionQuerier):
    prefix: Incomplete
    version_prefix: Incomplete
    assumed_version: Incomplete
    version_matcher: Incomplete
    is_opengl_es: bool
    version_string: Incomplete
    def pullVersion(self): ...
    def pullExtensions(self): ...

GLQuerier: Incomplete

class _GLUQuerier(ExtensionQuerier):
    prefix: Incomplete
    version_prefix: Incomplete
    def pullVersion(self): ...
    def pullExtensions(self): ...

GLUQuerier: Incomplete

def hasExtension(specifier): ...
hasGLExtension = hasExtension
hasGLUExtension = hasExtension

class _Alternate(LateBind):
    __module__: Incomplete
    def __init__(self, name, *alternates) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def finalise(self): ...

def alternate(name, *functions): ...
