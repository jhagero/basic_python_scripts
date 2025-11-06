from OpenGL.GL.ARB import enhanced_layouts as enhanced_layouts, texture_buffer_object as texture_buffer_object, uniform_buffer_object as uniform_buffer_object, vertex_buffer_object as vertex_buffer_object
from OpenGL.arrays import vbo as vbo

class Implementation(vbo.Implementation):
    available: bool
    def __init__(self) -> None: ...
