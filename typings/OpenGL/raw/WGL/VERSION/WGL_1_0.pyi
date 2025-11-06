from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

WGL_FONT_LINES: Incomplete
WGL_FONT_POLYGONS: Incomplete
WGL_SWAP_MAIN_PLANE: Incomplete
WGL_SWAP_OVERLAY1: Incomplete
WGL_SWAP_OVERLAY10: Incomplete
WGL_SWAP_OVERLAY11: Incomplete
WGL_SWAP_OVERLAY12: Incomplete
WGL_SWAP_OVERLAY13: Incomplete
WGL_SWAP_OVERLAY14: Incomplete
WGL_SWAP_OVERLAY15: Incomplete
WGL_SWAP_OVERLAY2: Incomplete
WGL_SWAP_OVERLAY3: Incomplete
WGL_SWAP_OVERLAY4: Incomplete
WGL_SWAP_OVERLAY5: Incomplete
WGL_SWAP_OVERLAY6: Incomplete
WGL_SWAP_OVERLAY7: Incomplete
WGL_SWAP_OVERLAY8: Incomplete
WGL_SWAP_OVERLAY9: Incomplete
WGL_SWAP_UNDERLAY1: Incomplete
WGL_SWAP_UNDERLAY10: Incomplete
WGL_SWAP_UNDERLAY11: Incomplete
WGL_SWAP_UNDERLAY12: Incomplete
WGL_SWAP_UNDERLAY13: Incomplete
WGL_SWAP_UNDERLAY14: Incomplete
WGL_SWAP_UNDERLAY15: Incomplete
WGL_SWAP_UNDERLAY2: Incomplete
WGL_SWAP_UNDERLAY3: Incomplete
WGL_SWAP_UNDERLAY4: Incomplete
WGL_SWAP_UNDERLAY5: Incomplete
WGL_SWAP_UNDERLAY6: Incomplete
WGL_SWAP_UNDERLAY7: Incomplete
WGL_SWAP_UNDERLAY8: Incomplete
WGL_SWAP_UNDERLAY9: Incomplete

@_f
def ChoosePixelFormat(hDc, pPfd) -> None: ...
@_f
def DescribePixelFormat(hdc, ipfd, cjpfd, ppfd) -> None: ...
@_f
def GetEnhMetaFilePixelFormat(hemf, cbBuffer, ppfd) -> None: ...
@_f
def GetPixelFormat(hdc) -> None: ...
@_f
def SetPixelFormat(hdc, ipfd, ppfd) -> None: ...
@_f
def SwapBuffers(hdc) -> None: ...
@_f
def wglCopyContext(hglrcSrc, hglrcDst, mask) -> None: ...
@_f
def wglCreateContext(hDc) -> None: ...
@_f
def wglCreateLayerContext(hDc, level) -> None: ...
@_f
def wglDeleteContext(oldContext) -> None: ...
@_f
def wglDescribeLayerPlane(hDc, pixelFormat, layerPlane, nBytes, plpd) -> None: ...
@_f
def wglGetCurrentContext() -> None: ...
@_f
def wglGetCurrentDC() -> None: ...
@_f
def wglGetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr) -> None: ...
@_f
def wglGetProcAddress(lpszProc) -> None: ...
@_f
def wglMakeCurrent(hDc, newContext) -> None: ...
@_f
def wglRealizeLayerPalette(hdc, iLayerPlane, bRealize) -> None: ...
@_f
def wglSetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr) -> None: ...
@_f
def wglShareLists(hrcSrvShare, hrcSrvSource) -> None: ...
@_f
def wglSwapLayerBuffers(hdc, fuFlags) -> None: ...
@_f
def wglUseFontBitmaps(hDC, first, count, listBase) -> None: ...
@_f
def wglUseFontBitmapsA(hDC, first, count, listBase) -> None: ...
@_f
def wglUseFontBitmapsW(hDC, first, count, listBase) -> None: ...
@_f
def wglUseFontOutlines(hDC, first, count, listBase, deviation, extrusion, format, lpgmf) -> None: ...
@_f
def wglUseFontOutlinesA(hDC, first, count, listBase, deviation, extrusion, format, lpgmf) -> None: ...
@_f
def wglUseFontOutlinesW(hDC, first, count, listBase, deviation, extrusion, format, lpgmf) -> None: ...
