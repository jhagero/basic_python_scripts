from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALPHA_REF_COMMAND_NV: Incomplete
GL_ATTRIBUTE_ADDRESS_COMMAND_NV: Incomplete
GL_BLEND_COLOR_COMMAND_NV: Incomplete
GL_DRAW_ARRAYS_COMMAND_NV: Incomplete
GL_DRAW_ARRAYS_INSTANCED_COMMAND_NV: Incomplete
GL_DRAW_ARRAYS_STRIP_COMMAND_NV: Incomplete
GL_DRAW_ELEMENTS_COMMAND_NV: Incomplete
GL_DRAW_ELEMENTS_INSTANCED_COMMAND_NV: Incomplete
GL_DRAW_ELEMENTS_STRIP_COMMAND_NV: Incomplete
GL_ELEMENT_ADDRESS_COMMAND_NV: Incomplete
GL_FRONT_FACE_COMMAND_NV: Incomplete
GL_LINE_WIDTH_COMMAND_NV: Incomplete
GL_NOP_COMMAND_NV: Incomplete
GL_POLYGON_OFFSET_COMMAND_NV: Incomplete
GL_SCISSOR_COMMAND_NV: Incomplete
GL_STENCIL_REF_COMMAND_NV: Incomplete
GL_TERMINATE_SEQUENCE_COMMAND_NV: Incomplete
GL_UNIFORM_ADDRESS_COMMAND_NV: Incomplete
GL_VIEWPORT_COMMAND_NV: Incomplete

@_f
def glCallCommandListNV(list) -> None: ...
@_f
def glCommandListSegmentsNV(list, segments) -> None: ...
@_f
def glCompileCommandListNV(list) -> None: ...
@_f
def glCreateCommandListsNV(n, lists) -> None: ...
@_f
def glCreateStatesNV(n, states) -> None: ...
@_f
def glDeleteCommandListsNV(n, lists) -> None: ...
@_f
def glDeleteStatesNV(n, states) -> None: ...
@_f
def glDrawCommandsAddressNV(primitiveMode, indirects, sizes, count) -> None: ...
@_f
def glDrawCommandsNV(primitiveMode, buffer, indirects, sizes, count) -> None: ...
@_f
def glDrawCommandsStatesAddressNV(indirects, sizes, states, fbos, count) -> None: ...
@_f
def glDrawCommandsStatesNV(buffer, indirects, sizes, states, fbos, count) -> None: ...
@_f
def glGetCommandHeaderNV(tokenID, size) -> None: ...
@_f
def glGetStageIndexNV(shadertype) -> None: ...
@_f
def glIsCommandListNV(list) -> None: ...
@_f
def glIsStateNV(state) -> None: ...
@_f
def glListDrawCommandsStatesClientNV(list, segment, indirects, sizes, states, fbos, count) -> None: ...
@_f
def glStateCaptureNV(state, mode) -> None: ...
