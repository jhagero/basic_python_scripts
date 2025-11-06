from OpenGL.plugins import FormatHandler as FormatHandler, PlatformPlugin as PlatformPlugin
from OpenGL.version import __version__ as __version__
from _typeshed import Incomplete

def environ_key(name, default): ...

ERROR_CHECKING: Incomplete
ERROR_LOGGING: Incomplete
ERROR_ON_COPY: Incomplete
ARRAY_SIZE_CHECKING: Incomplete
STORE_POINTERS: Incomplete
WARN_ON_FORMAT_UNAVAILABLE: bool
FORWARD_COMPATIBLE_ONLY: bool
SIZE_1_ARRAY_UNPACK: bool
USE_ACCELERATE: Incomplete
CONTEXT_CHECKING: Incomplete
FULL_LOGGING: Incomplete
ALLOW_NUMPY_SCALARS: Incomplete
UNSIGNED_BYTE_IMAGES_AS_STRING: Incomplete
MODULE_ANNOTATIONS: bool
TYPE_ANNOTATIONS: bool

def setPlatform(key) -> None: ...
