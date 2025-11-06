from _typeshed import Incomplete

__all__ = ['glReadPixels', 'glReadPixelsb', 'glReadPixelsd', 'glReadPixelsf', 'glReadPixelsi', 'glReadPixelss', 'glReadPixelsub', 'glReadPixelsui', 'glReadPixelsus', 'glGetTexImage', 'glDrawPixels', 'glDrawPixelsb', 'glDrawPixelsf', 'glDrawPixelsi', 'glDrawPixelss', 'glDrawPixelsub', 'glDrawPixelsui', 'glDrawPixelsus', 'glTexSubImage2D', 'glTexSubImage1D', 'glTexImage1D', 'glTexImage2D', 'glGetTexImageb', 'glGetTexImaged', 'glGetTexImagef', 'glGetTexImagei', 'glGetTexImages', 'glGetTexImageub', 'glGetTexImageui', 'glGetTexImageus', 'glTexImage1Db', 'glTexImage2Db', 'glTexSubImage1Db', 'glTexSubImage2Db', 'glTexImage1Df', 'glTexImage2Df', 'glTexSubImage1Df', 'glTexSubImage2Df', 'glTexImage1Di', 'glTexImage2Di', 'glTexSubImage1Di', 'glTexSubImage2Di', 'glTexImage1Ds', 'glTexImage2Ds', 'glTexSubImage1Ds', 'glTexSubImage2Ds', 'glTexImage1Dub', 'glTexImage2Dub', 'glTexSubImage1Dub', 'glTexSubImage2Dub', 'glTexImage1Dui', 'glTexImage2Dui', 'glTexSubImage1Dui', 'glTexSubImage2Dui', 'glTexImage1Dus', 'glTexImage2Dus', 'glTexSubImage1Dus', 'glTexSubImage2Dus']

def glReadPixels(x, y, width, height, format, type=..., array=None, outputType=...): ...
def glGetTexImage(target, level, format, type=..., array=None, outputType=...): ...

class ImageInputConverter:
    rank: Incomplete
    typeName: Incomplete
    pixelsName: Incomplete
    def __init__(self, rank, pixelsName=None, typeName: str = 'type') -> None: ...
    typeIndex: Incomplete
    pixelsIndex: Incomplete
    def finalise(self, wrapper) -> None: ...
    def __call__(self, arg, baseOperation, pyArgs): ...

class TypedImageInputConverter(ImageInputConverter):
    rank: Incomplete
    arrayType: Incomplete
    pixelsName: Incomplete
    typeName: Incomplete
    def __init__(self, rank, pixelsName, arrayType, typeName=None) -> None: ...
    def __call__(self, arg, baseOperation, pyArgs): ...
    pixelsIndex: Incomplete
    def finalise(self, wrapper) -> None: ...
    def width(self, pyArgs, index, wrappedOperation): ...
    def height(self, pyArgs, index, wrappedOperation): ...
    def depth(self, pyArgs, index, wrappedOperation): ...
    def type(self, pyArgs, index, wrappedOperation): ...

class CompressedImageConverter:
    dataIndex: Incomplete
    def finalise(self, wrapper) -> None: ...
    def __call__(self, pyArgs, index, wrappedOperation): ...

glDrawPixels: Incomplete
glTexSubImage2D: Incomplete
glTexSubImage1D: Incomplete
glTexImage2D: Incomplete
glTexImage1D: Incomplete

# Names in __all__ with no definition:
#   glDrawPixelsb
#   glDrawPixelsf
#   glDrawPixelsi
#   glDrawPixelss
#   glDrawPixelsub
#   glDrawPixelsui
#   glDrawPixelsus
#   glGetTexImageb
#   glGetTexImaged
#   glGetTexImagef
#   glGetTexImagei
#   glGetTexImages
#   glGetTexImageub
#   glGetTexImageui
#   glGetTexImageus
#   glReadPixelsb
#   glReadPixelsd
#   glReadPixelsf
#   glReadPixelsi
#   glReadPixelss
#   glReadPixelsub
#   glReadPixelsui
#   glReadPixelsus
#   glTexImage1Db
#   glTexImage1Df
#   glTexImage1Di
#   glTexImage1Ds
#   glTexImage1Dub
#   glTexImage1Dui
#   glTexImage1Dus
#   glTexImage2Db
#   glTexImage2Df
#   glTexImage2Di
#   glTexImage2Ds
#   glTexImage2Dub
#   glTexImage2Dui
#   glTexImage2Dus
#   glTexSubImage1Db
#   glTexSubImage1Df
#   glTexSubImage1Di
#   glTexSubImage1Ds
#   glTexSubImage1Dub
#   glTexSubImage1Dui
#   glTexSubImage1Dus
#   glTexSubImage2Db
#   glTexSubImage2Df
#   glTexSubImage2Di
#   glTexSubImage2Ds
#   glTexSubImage2Dub
#   glTexSubImage2Dui
#   glTexSubImage2Dus
