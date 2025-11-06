from OpenGL.GL.VERSION import GL_1_5 as GL_1_5, GL_3_0 as GL_3_0, GL_3_1 as GL_3_1
from OpenGL.arrays import vbo as vbo

class Implementation(vbo.Implementation):
    available: bool
    def __init__(self) -> None: ...
