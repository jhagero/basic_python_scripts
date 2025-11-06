from OpenGL.raw.GL.ARB.texture_compression import *
from OpenGL import arrays as arrays, constant as constant, extensions as extensions, platform as platform, wrapper as wrapper
from OpenGL.GL import images as images
from _typeshed import Incomplete

def glInitTextureCompressionARB(): ...

glCompressedTexImage3DARB: Incomplete
glCompressedTexImage2DARB: Incomplete
glCompressedTexImage1DARB: Incomplete
glCompressedTexSubImage3DARB: Incomplete
glCompressedTexSubImage2DARB: Incomplete
glCompressedTexSubImage1DARB: Incomplete
name: Incomplete

def glGetCompressedTexImageARB(target, level, img=None): ...
