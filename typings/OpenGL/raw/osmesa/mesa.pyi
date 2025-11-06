from OpenGL.raw.osmesa._types import *
from _typeshed import Incomplete

__all__ = ['OSMesaCreateContext', 'OSMesaCreateContextExt', 'OSMesaMakeCurrent', 'OSMesaGetIntegerv', 'OSMesaGetCurrentContext', 'OSMesaDestroyContext', 'OSMesaPixelStore', 'OSMesaGetDepthBuffer', 'OSMesaGetColorBuffer', 'OSMesaCreateContextAttribs', 'OSMesaColorClamp', 'OSMesaPostprocess', 'OSMESA_COLOR_INDEX', 'OSMESA_RGBA', 'OSMESA_BGRA', 'OSMESA_ARGB', 'OSMESA_RGB', 'OSMESA_BGR', 'OSMESA_BGR', 'OSMESA_ROW_LENGTH', 'OSMESA_Y_UP', 'OSMESA_WIDTH', 'OSMESA_HEIGHT', 'OSMESA_FORMAT', 'OSMESA_TYPE', 'OSMESA_MAX_WIDTH', 'OSMESA_MAX_HEIGHT', 'OSMESA_DEPTH_BITS', 'OSMESA_STENCIL_BITS', 'OSMESA_ACCUM_BITS', 'OSMESA_PROFILE', 'OSMESA_CORE_PROFILE', 'OSMESA_COMPAT_PROFILE', 'OSMESA_CONTEXT_MAJOR_VERSION', 'OSMESA_CONTEXT_MINOR_VERSION']

OSMESA_COLOR_INDEX: Incomplete
OSMESA_RGBA: Incomplete
OSMESA_BGRA: Incomplete
OSMESA_ARGB: Incomplete
OSMESA_RGB: Incomplete
OSMESA_BGR: Incomplete
OSMESA_ROW_LENGTH: Incomplete
OSMESA_Y_UP: Incomplete
OSMESA_WIDTH: Incomplete
OSMESA_HEIGHT: Incomplete
OSMESA_FORMAT: Incomplete
OSMESA_TYPE: Incomplete
OSMESA_MAX_WIDTH: Incomplete
OSMESA_MAX_HEIGHT: Incomplete
OSMESA_DEPTH_BITS: Incomplete
OSMESA_STENCIL_BITS: Incomplete
OSMESA_ACCUM_BITS: Incomplete
OSMESA_PROFILE: Incomplete
OSMESA_CORE_PROFILE: Incomplete
OSMESA_COMPAT_PROFILE: Incomplete
OSMESA_CONTEXT_MAJOR_VERSION: Incomplete
OSMESA_CONTEXT_MINOR_VERSION: Incomplete
OSMesaGetCurrentContext: Incomplete

@_f
def OSMesaCreateContext(format, sharelist) -> None: ...
@_f
def OSMesaCreateContextExt(format, depthBits, stencilBits, accumBits, sharelist) -> None: ...
@_f
def OSMesaCreateContextAttribs(attribList, sharelist) -> None: ...
@_f
def OSMesaDestroyContext(ctx) -> None: ...
@_f
def OSMesaMakeCurrent(ctx, buffer, type, width, height) -> None: ...
@_f
def OSMesaPixelStore(ctx, buffer, type, width, height) -> None: ...
def OSMesaGetIntegerv(pname): ...
def OSMesaGetDepthBuffer(c): ...
def OSMesaGetColorBuffer(c): ...
@_f
def OSMesaColorClamp(enable) -> None: ...
@_f
def OSMesaPostprocess(osmesa, filter, enable_value) -> None: ...
