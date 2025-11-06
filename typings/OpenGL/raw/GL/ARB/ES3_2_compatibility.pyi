from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY_ARB: Incomplete
GL_MULTISAMPLE_LINE_WIDTH_RANGE_ARB: Incomplete
GL_PRIMITIVE_BOUNDING_BOX_ARB: Incomplete

@_f
def glPrimitiveBoundingBoxARB(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW) -> None: ...
