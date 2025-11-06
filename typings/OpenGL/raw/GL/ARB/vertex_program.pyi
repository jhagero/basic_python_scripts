from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_COLOR_SUM_ARB: Incomplete
GL_CURRENT_MATRIX_ARB: Incomplete
GL_CURRENT_MATRIX_STACK_DEPTH_ARB: Incomplete
GL_CURRENT_VERTEX_ATTRIB_ARB: Incomplete
GL_MATRIX0_ARB: Incomplete
GL_MATRIX10_ARB: Incomplete
GL_MATRIX11_ARB: Incomplete
GL_MATRIX12_ARB: Incomplete
GL_MATRIX13_ARB: Incomplete
GL_MATRIX14_ARB: Incomplete
GL_MATRIX15_ARB: Incomplete
GL_MATRIX16_ARB: Incomplete
GL_MATRIX17_ARB: Incomplete
GL_MATRIX18_ARB: Incomplete
GL_MATRIX19_ARB: Incomplete
GL_MATRIX1_ARB: Incomplete
GL_MATRIX20_ARB: Incomplete
GL_MATRIX21_ARB: Incomplete
GL_MATRIX22_ARB: Incomplete
GL_MATRIX23_ARB: Incomplete
GL_MATRIX24_ARB: Incomplete
GL_MATRIX25_ARB: Incomplete
GL_MATRIX26_ARB: Incomplete
GL_MATRIX27_ARB: Incomplete
GL_MATRIX28_ARB: Incomplete
GL_MATRIX29_ARB: Incomplete
GL_MATRIX2_ARB: Incomplete
GL_MATRIX30_ARB: Incomplete
GL_MATRIX31_ARB: Incomplete
GL_MATRIX3_ARB: Incomplete
GL_MATRIX4_ARB: Incomplete
GL_MATRIX5_ARB: Incomplete
GL_MATRIX6_ARB: Incomplete
GL_MATRIX7_ARB: Incomplete
GL_MATRIX8_ARB: Incomplete
GL_MATRIX9_ARB: Incomplete
GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB: Incomplete
GL_MAX_PROGRAM_ATTRIBS_ARB: Incomplete
GL_MAX_PROGRAM_ENV_PARAMETERS_ARB: Incomplete
GL_MAX_PROGRAM_INSTRUCTIONS_ARB: Incomplete
GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB: Incomplete
GL_MAX_PROGRAM_MATRICES_ARB: Incomplete
GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB: Incomplete
GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB: Incomplete
GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB: Incomplete
GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB: Incomplete
GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB: Incomplete
GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB: Incomplete
GL_MAX_PROGRAM_PARAMETERS_ARB: Incomplete
GL_MAX_PROGRAM_TEMPORARIES_ARB: Incomplete
GL_MAX_VERTEX_ATTRIBS_ARB: Incomplete
GL_PROGRAM_ADDRESS_REGISTERS_ARB: Incomplete
GL_PROGRAM_ATTRIBS_ARB: Incomplete
GL_PROGRAM_BINDING_ARB: Incomplete
GL_PROGRAM_ERROR_POSITION_ARB: Incomplete
GL_PROGRAM_ERROR_STRING_ARB: Incomplete
GL_PROGRAM_FORMAT_ARB: Incomplete
GL_PROGRAM_FORMAT_ASCII_ARB: Incomplete
GL_PROGRAM_INSTRUCTIONS_ARB: Incomplete
GL_PROGRAM_LENGTH_ARB: Incomplete
GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB: Incomplete
GL_PROGRAM_NATIVE_ATTRIBS_ARB: Incomplete
GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB: Incomplete
GL_PROGRAM_NATIVE_PARAMETERS_ARB: Incomplete
GL_PROGRAM_NATIVE_TEMPORARIES_ARB: Incomplete
GL_PROGRAM_PARAMETERS_ARB: Incomplete
GL_PROGRAM_STRING_ARB: Incomplete
GL_PROGRAM_TEMPORARIES_ARB: Incomplete
GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB: Incomplete
GL_TRANSPOSE_CURRENT_MATRIX_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB: Incomplete
GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB: Incomplete
GL_VERTEX_PROGRAM_ARB: Incomplete
GL_VERTEX_PROGRAM_POINT_SIZE_ARB: Incomplete
GL_VERTEX_PROGRAM_TWO_SIDE_ARB: Incomplete

@_f
def glBindProgramARB(target, program) -> None: ...
@_f
def glDeleteProgramsARB(n, programs) -> None: ...
@_f
def glDisableVertexAttribArrayARB(index) -> None: ...
@_f
def glEnableVertexAttribArrayARB(index) -> None: ...
@_f
def glGenProgramsARB(n, programs) -> None: ...
@_f
def glGetProgramEnvParameterdvARB(target, index, params) -> None: ...
@_f
def glGetProgramEnvParameterfvARB(target, index, params) -> None: ...
@_f
def glGetProgramLocalParameterdvARB(target, index, params) -> None: ...
@_f
def glGetProgramLocalParameterfvARB(target, index, params) -> None: ...
@_f
def glGetProgramStringARB(target, pname, string) -> None: ...
@_f
def glGetProgramivARB(target, pname, params) -> None: ...
@_f
def glGetVertexAttribPointervARB(index, pname, pointer) -> None: ...
@_f
def glGetVertexAttribdvARB(index, pname, params) -> None: ...
@_f
def glGetVertexAttribfvARB(index, pname, params) -> None: ...
@_f
def glGetVertexAttribivARB(index, pname, params) -> None: ...
@_f
def glIsProgramARB(program) -> None: ...
@_f
def glProgramEnvParameter4dARB(target, index, x, y, z, w) -> None: ...
@_f
def glProgramEnvParameter4dvARB(target, index, params) -> None: ...
@_f
def glProgramEnvParameter4fARB(target, index, x, y, z, w) -> None: ...
@_f
def glProgramEnvParameter4fvARB(target, index, params) -> None: ...
@_f
def glProgramLocalParameter4dARB(target, index, x, y, z, w) -> None: ...
@_f
def glProgramLocalParameter4dvARB(target, index, params) -> None: ...
@_f
def glProgramLocalParameter4fARB(target, index, x, y, z, w) -> None: ...
@_f
def glProgramLocalParameter4fvARB(target, index, params) -> None: ...
@_f
def glProgramStringARB(target, format, len, string) -> None: ...
@_f
def glVertexAttrib1dARB(index, x) -> None: ...
@_f
def glVertexAttrib1dvARB(index, v) -> None: ...
@_f
def glVertexAttrib1fARB(index, x) -> None: ...
@_f
def glVertexAttrib1fvARB(index, v) -> None: ...
@_f
def glVertexAttrib1sARB(index, x) -> None: ...
@_f
def glVertexAttrib1svARB(index, v) -> None: ...
@_f
def glVertexAttrib2dARB(index, x, y) -> None: ...
@_f
def glVertexAttrib2dvARB(index, v) -> None: ...
@_f
def glVertexAttrib2fARB(index, x, y) -> None: ...
@_f
def glVertexAttrib2fvARB(index, v) -> None: ...
@_f
def glVertexAttrib2sARB(index, x, y) -> None: ...
@_f
def glVertexAttrib2svARB(index, v) -> None: ...
@_f
def glVertexAttrib3dARB(index, x, y, z) -> None: ...
@_f
def glVertexAttrib3dvARB(index, v) -> None: ...
@_f
def glVertexAttrib3fARB(index, x, y, z) -> None: ...
@_f
def glVertexAttrib3fvARB(index, v) -> None: ...
@_f
def glVertexAttrib3sARB(index, x, y, z) -> None: ...
@_f
def glVertexAttrib3svARB(index, v) -> None: ...
@_f
def glVertexAttrib4NbvARB(index, v) -> None: ...
@_f
def glVertexAttrib4NivARB(index, v) -> None: ...
@_f
def glVertexAttrib4NsvARB(index, v) -> None: ...
@_f
def glVertexAttrib4NubARB(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4NubvARB(index, v) -> None: ...
@_f
def glVertexAttrib4NuivARB(index, v) -> None: ...
@_f
def glVertexAttrib4NusvARB(index, v) -> None: ...
@_f
def glVertexAttrib4bvARB(index, v) -> None: ...
@_f
def glVertexAttrib4dARB(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4dvARB(index, v) -> None: ...
@_f
def glVertexAttrib4fARB(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4fvARB(index, v) -> None: ...
@_f
def glVertexAttrib4ivARB(index, v) -> None: ...
@_f
def glVertexAttrib4sARB(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4svARB(index, v) -> None: ...
@_f
def glVertexAttrib4ubvARB(index, v) -> None: ...
@_f
def glVertexAttrib4uivARB(index, v) -> None: ...
@_f
def glVertexAttrib4usvARB(index, v) -> None: ...
@_f
def glVertexAttribPointerARB(index, size, type, normalized, stride, pointer) -> None: ...
