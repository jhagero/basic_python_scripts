from OpenGL.error import EGLError as EGLError

class EGLError(EGLError):
    @property
    def err(self): ...
    @err.setter
    def err(self, value) -> None: ...
