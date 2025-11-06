from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_SPARSE_BUFFER_PAGE_SIZE_ARB: Incomplete
GL_SPARSE_STORAGE_BIT_ARB: Incomplete

@_f
def glBufferPageCommitmentARB(target, offset, size, commit) -> None: ...
@_f
def glNamedBufferPageCommitmentARB(buffer, offset, size, commit) -> None: ...
@_f
def glNamedBufferPageCommitmentEXT(buffer, offset, size, commit) -> None: ...
