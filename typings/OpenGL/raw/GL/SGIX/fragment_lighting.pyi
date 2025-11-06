from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_RASTER_NORMAL_SGIX: Incomplete
GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX: Incomplete
GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX: Incomplete
GL_FRAGMENT_COLOR_MATERIAL_SGIX: Incomplete
GL_FRAGMENT_LIGHT0_SGIX: Incomplete
GL_FRAGMENT_LIGHT1_SGIX: Incomplete
GL_FRAGMENT_LIGHT2_SGIX: Incomplete
GL_FRAGMENT_LIGHT3_SGIX: Incomplete
GL_FRAGMENT_LIGHT4_SGIX: Incomplete
GL_FRAGMENT_LIGHT5_SGIX: Incomplete
GL_FRAGMENT_LIGHT6_SGIX: Incomplete
GL_FRAGMENT_LIGHT7_SGIX: Incomplete
GL_FRAGMENT_LIGHTING_SGIX: Incomplete
GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX: Incomplete
GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX: Incomplete
GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX: Incomplete
GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX: Incomplete
GL_LIGHT_ENV_MODE_SGIX: Incomplete
GL_MAX_ACTIVE_LIGHTS_SGIX: Incomplete
GL_MAX_FRAGMENT_LIGHTS_SGIX: Incomplete

@_f
def glFragmentColorMaterialSGIX(face, mode) -> None: ...
@_f
def glFragmentLightModelfSGIX(pname, param) -> None: ...
@_f
def glFragmentLightModelfvSGIX(pname, params) -> None: ...
@_f
def glFragmentLightModeliSGIX(pname, param) -> None: ...
@_f
def glFragmentLightModelivSGIX(pname, params) -> None: ...
@_f
def glFragmentLightfSGIX(light, pname, param) -> None: ...
@_f
def glFragmentLightfvSGIX(light, pname, params) -> None: ...
@_f
def glFragmentLightiSGIX(light, pname, param) -> None: ...
@_f
def glFragmentLightivSGIX(light, pname, params) -> None: ...
@_f
def glFragmentMaterialfSGIX(face, pname, param) -> None: ...
@_f
def glFragmentMaterialfvSGIX(face, pname, params) -> None: ...
@_f
def glFragmentMaterialiSGIX(face, pname, param) -> None: ...
@_f
def glFragmentMaterialivSGIX(face, pname, params) -> None: ...
@_f
def glGetFragmentLightfvSGIX(light, pname, params) -> None: ...
@_f
def glGetFragmentLightivSGIX(light, pname, params) -> None: ...
@_f
def glGetFragmentMaterialfvSGIX(face, pname, params) -> None: ...
@_f
def glGetFragmentMaterialivSGIX(face, pname, params) -> None: ...
@_f
def glLightEnviSGIX(pname, param) -> None: ...
