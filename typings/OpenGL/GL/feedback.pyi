from OpenGL import contextdata as contextdata
from _typeshed import Incomplete

def parseFeedback(buffer, entryCount): ...

SINGLE_VERTEX_TOKENS: Incomplete
DOUBLE_VERTEX_TOKENS: Incomplete

class Vertex:
    vertex: Incomplete
    color: Incomplete
    texture: Incomplete
    def __init__(self, vertex, color=None, texture=None) -> None: ...

def createGetVertex(): ...
