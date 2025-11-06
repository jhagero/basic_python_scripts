from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_BITMAP_ORIGIN_KHR: Incomplete
EGL_BITMAP_PITCH_KHR: Incomplete
EGL_BITMAP_PIXEL_ALPHA_OFFSET_KHR: Incomplete
EGL_BITMAP_PIXEL_BLUE_OFFSET_KHR: Incomplete
EGL_BITMAP_PIXEL_GREEN_OFFSET_KHR: Incomplete
EGL_BITMAP_PIXEL_LUMINANCE_OFFSET_KHR: Incomplete
EGL_BITMAP_PIXEL_RED_OFFSET_KHR: Incomplete
EGL_BITMAP_POINTER_KHR: Incomplete
EGL_FORMAT_RGBA_8888_EXACT_KHR: Incomplete
EGL_FORMAT_RGBA_8888_KHR: Incomplete
EGL_FORMAT_RGB_565_EXACT_KHR: Incomplete
EGL_FORMAT_RGB_565_KHR: Incomplete
EGL_LOCK_SURFACE_BIT_KHR: Incomplete
EGL_LOCK_USAGE_HINT_KHR: Incomplete
EGL_LOWER_LEFT_KHR: Incomplete
EGL_MAP_PRESERVE_PIXELS_KHR: Incomplete
EGL_MATCH_FORMAT_KHR: Incomplete
EGL_OPTIMAL_FORMAT_BIT_KHR: Incomplete
EGL_READ_SURFACE_BIT_KHR: Incomplete
EGL_UPPER_LEFT_KHR: Incomplete
EGL_WRITE_SURFACE_BIT_KHR: Incomplete

@_f
def eglLockSurfaceKHR(dpy, surface, attrib_list) -> None: ...
@_f
def eglUnlockSurfaceKHR(dpy, surface) -> None: ...
