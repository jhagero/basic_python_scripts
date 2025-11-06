from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_ACCELERATION_EXT: Incomplete
WGL_ACCUM_ALPHA_BITS_EXT: Incomplete
WGL_ACCUM_BITS_EXT: Incomplete
WGL_ACCUM_BLUE_BITS_EXT: Incomplete
WGL_ACCUM_GREEN_BITS_EXT: Incomplete
WGL_ACCUM_RED_BITS_EXT: Incomplete
WGL_ALPHA_BITS_EXT: Incomplete
WGL_ALPHA_SHIFT_EXT: Incomplete
WGL_AUX_BUFFERS_EXT: Incomplete
WGL_BLUE_BITS_EXT: Incomplete
WGL_BLUE_SHIFT_EXT: Incomplete
WGL_COLOR_BITS_EXT: Incomplete
WGL_DEPTH_BITS_EXT: Incomplete
WGL_DOUBLE_BUFFER_EXT: Incomplete
WGL_DRAW_TO_BITMAP_EXT: Incomplete
WGL_DRAW_TO_WINDOW_EXT: Incomplete
WGL_FULL_ACCELERATION_EXT: Incomplete
WGL_GENERIC_ACCELERATION_EXT: Incomplete
WGL_GREEN_BITS_EXT: Incomplete
WGL_GREEN_SHIFT_EXT: Incomplete
WGL_NEED_PALETTE_EXT: Incomplete
WGL_NEED_SYSTEM_PALETTE_EXT: Incomplete
WGL_NO_ACCELERATION_EXT: Incomplete
WGL_NUMBER_OVERLAYS_EXT: Incomplete
WGL_NUMBER_PIXEL_FORMATS_EXT: Incomplete
WGL_NUMBER_UNDERLAYS_EXT: Incomplete
WGL_PIXEL_TYPE_EXT: Incomplete
WGL_RED_BITS_EXT: Incomplete
WGL_RED_SHIFT_EXT: Incomplete
WGL_SHARE_ACCUM_EXT: Incomplete
WGL_SHARE_DEPTH_EXT: Incomplete
WGL_SHARE_STENCIL_EXT: Incomplete
WGL_STENCIL_BITS_EXT: Incomplete
WGL_STEREO_EXT: Incomplete
WGL_SUPPORT_GDI_EXT: Incomplete
WGL_SUPPORT_OPENGL_EXT: Incomplete
WGL_SWAP_COPY_EXT: Incomplete
WGL_SWAP_EXCHANGE_EXT: Incomplete
WGL_SWAP_LAYER_BUFFERS_EXT: Incomplete
WGL_SWAP_METHOD_EXT: Incomplete
WGL_SWAP_UNDEFINED_EXT: Incomplete
WGL_TRANSPARENT_EXT: Incomplete
WGL_TRANSPARENT_VALUE_EXT: Incomplete
WGL_TYPE_COLORINDEX_EXT: Incomplete
WGL_TYPE_RGBA_EXT: Incomplete

@_f
def wglChoosePixelFormatEXT(hdc, piAttribIList, pfAttribFList, nMaxFormats, piFormats, nNumFormats) -> None: ...
@_f
def wglGetPixelFormatAttribfvEXT(hdc, iPixelFormat, iLayerPlane, nAttributes, piAttributes, pfValues) -> None: ...
@_f
def wglGetPixelFormatAttribivEXT(hdc, iPixelFormat, iLayerPlane, nAttributes, piAttributes, piValues) -> None: ...
