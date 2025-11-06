from OpenGL.plugins import PlatformPlugin as PlatformPlugin
from _typeshed import Incomplete

XDG: str
WAYLAND_DISPLAY: str
PLATFORM: Incomplete
nullFunction: Incomplete

def types(resultType, *argTypes): ...
def unpack_constants(constants, namespace) -> None: ...
def createFunction(function, dll, extension, deprecated: bool = False, error_checker=None, force_extension: bool = False): ...
