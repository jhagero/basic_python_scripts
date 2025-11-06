from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_ACCELERATION_ARB: Incomplete
WGL_ACCUM_ALPHA_BITS_ARB: Incomplete
WGL_ACCUM_BITS_ARB: Incomplete
WGL_ACCUM_BLUE_BITS_ARB: Incomplete
WGL_ACCUM_GREEN_BITS_ARB: Incomplete
WGL_ACCUM_RED_BITS_ARB: Incomplete
WGL_ALPHA_BITS_ARB: Incomplete
WGL_ALPHA_SHIFT_ARB: Incomplete
WGL_AUX_BUFFERS_ARB: Incomplete
WGL_BLUE_BITS_ARB: Incomplete
WGL_BLUE_SHIFT_ARB: Incomplete
WGL_COLOR_BITS_ARB: Incomplete
WGL_DEPTH_BITS_ARB: Incomplete
WGL_DOUBLE_BUFFER_ARB: Incomplete
WGL_DRAW_TO_BITMAP_ARB: Incomplete
WGL_DRAW_TO_WINDOW_ARB: Incomplete
WGL_FULL_ACCELERATION_ARB: Incomplete
WGL_GENERIC_ACCELERATION_ARB: Incomplete
WGL_GREEN_BITS_ARB: Incomplete
WGL_GREEN_SHIFT_ARB: Incomplete
WGL_NEED_PALETTE_ARB: Incomplete
WGL_NEED_SYSTEM_PALETTE_ARB: Incomplete
WGL_NO_ACCELERATION_ARB: Incomplete
WGL_NUMBER_OVERLAYS_ARB: Incomplete
WGL_NUMBER_PIXEL_FORMATS_ARB: Incomplete
WGL_NUMBER_UNDERLAYS_ARB: Incomplete
WGL_PIXEL_TYPE_ARB: Incomplete
WGL_RED_BITS_ARB: Incomplete
WGL_RED_SHIFT_ARB: Incomplete
WGL_SHARE_ACCUM_ARB: Incomplete
WGL_SHARE_DEPTH_ARB: Incomplete
WGL_SHARE_STENCIL_ARB: Incomplete
WGL_STENCIL_BITS_ARB: Incomplete
WGL_STEREO_ARB: Incomplete
WGL_SUPPORT_GDI_ARB: Incomplete
WGL_SUPPORT_OPENGL_ARB: Incomplete
WGL_SWAP_COPY_ARB: Incomplete
WGL_SWAP_EXCHANGE_ARB: Incomplete
WGL_SWAP_LAYER_BUFFERS_ARB: Incomplete
WGL_SWAP_METHOD_ARB: Incomplete
WGL_SWAP_UNDEFINED_ARB: Incomplete
WGL_TRANSPARENT_ALPHA_VALUE_ARB: Incomplete
WGL_TRANSPARENT_ARB: Incomplete
WGL_TRANSPARENT_BLUE_VALUE_ARB: Incomplete
WGL_TRANSPARENT_GREEN_VALUE_ARB: Incomplete
WGL_TRANSPARENT_INDEX_VALUE_ARB: Incomplete
WGL_TRANSPARENT_RED_VALUE_ARB: Incomplete
WGL_TYPE_COLORINDEX_ARB: Incomplete
WGL_TYPE_RGBA_ARB: Incomplete

@_f
def wglChoosePixelFormatARB(hdc, piAttribIList, pfAttribFList, nMaxFormats, piFormats, nNumFormats) -> None: ...
@_f
def wglGetPixelFormatAttribfvARB(hdc, iPixelFormat, iLayerPlane, nAttributes, piAttributes, pfValues) -> None: ...
@_f
def wglGetPixelFormatAttribivARB(hdc, iPixelFormat, iLayerPlane, nAttributes, piAttributes, piValues) -> None: ...
