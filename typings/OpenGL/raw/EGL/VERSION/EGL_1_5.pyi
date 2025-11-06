from OpenGL.raw.EGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

EGL_CL_EVENT_HANDLE: Incomplete
EGL_CONDITION_SATISFIED: Incomplete
EGL_CONTEXT_MAJOR_VERSION: Incomplete
EGL_CONTEXT_MINOR_VERSION: Incomplete
EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT: Incomplete
EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT: Incomplete
EGL_CONTEXT_OPENGL_DEBUG: Incomplete
EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE: Incomplete
EGL_CONTEXT_OPENGL_PROFILE_MASK: Incomplete
EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY: Incomplete
EGL_CONTEXT_OPENGL_ROBUST_ACCESS: Incomplete
EGL_FOREVER: Incomplete
EGL_GL_COLORSPACE: Incomplete
EGL_GL_COLORSPACE_LINEAR: Incomplete
EGL_GL_COLORSPACE_SRGB: Incomplete
EGL_GL_RENDERBUFFER: Incomplete
EGL_GL_TEXTURE_2D: Incomplete
EGL_GL_TEXTURE_3D: Incomplete
EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X: Incomplete
EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: Incomplete
EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: Incomplete
EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X: Incomplete
EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y: Incomplete
EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z: Incomplete
EGL_GL_TEXTURE_LEVEL: Incomplete
EGL_GL_TEXTURE_ZOFFSET: Incomplete
EGL_IMAGE_PRESERVED: Incomplete
EGL_LOSE_CONTEXT_ON_RESET: Incomplete
EGL_NO_RESET_NOTIFICATION: Incomplete
EGL_OPENGL_ES3_BIT: Incomplete
EGL_SIGNALED: Incomplete
EGL_SYNC_CL_EVENT: Incomplete
EGL_SYNC_CL_EVENT_COMPLETE: Incomplete
EGL_SYNC_CONDITION: Incomplete
EGL_SYNC_FENCE: Incomplete
EGL_SYNC_FLUSH_COMMANDS_BIT: Incomplete
EGL_SYNC_PRIOR_COMMANDS_COMPLETE: Incomplete
EGL_SYNC_STATUS: Incomplete
EGL_SYNC_TYPE: Incomplete
EGL_TIMEOUT_EXPIRED: Incomplete
EGL_UNSIGNALED: Incomplete

@_f
def eglClientWaitSync(dpy, sync, flags, timeout) -> None: ...
@_f
def eglCreateImage(dpy, ctx, target, buffer, attrib_list) -> None: ...
@_f
def eglCreatePlatformPixmapSurface(dpy, config, native_pixmap, attrib_list) -> None: ...
@_f
def eglCreatePlatformWindowSurface(dpy, config, native_window, attrib_list) -> None: ...
@_f
def eglCreateSync(dpy, type, attrib_list) -> None: ...
@_f
def eglDestroyImage(dpy, image) -> None: ...
@_f
def eglDestroySync(dpy, sync) -> None: ...
@_f
def eglGetPlatformDisplay(platform, native_display, attrib_list) -> None: ...
@_f
def eglGetSyncAttrib(dpy, sync, attribute, value) -> None: ...
@_f
def eglWaitSync(dpy, sync, flags) -> None: ...
