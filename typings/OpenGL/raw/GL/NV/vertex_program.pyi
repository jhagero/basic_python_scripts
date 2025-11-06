from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ATTRIB_ARRAY_POINTER_NV: Incomplete
GL_ATTRIB_ARRAY_SIZE_NV: Incomplete
GL_ATTRIB_ARRAY_STRIDE_NV: Incomplete
GL_ATTRIB_ARRAY_TYPE_NV: Incomplete
GL_CURRENT_ATTRIB_NV: Incomplete
GL_CURRENT_MATRIX_NV: Incomplete
GL_CURRENT_MATRIX_STACK_DEPTH_NV: Incomplete
GL_IDENTITY_NV: Incomplete
GL_INVERSE_NV: Incomplete
GL_INVERSE_TRANSPOSE_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB0_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB10_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB11_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB12_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB13_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB14_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB15_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB1_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB2_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB3_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB4_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB5_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB6_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB7_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB8_4_NV: Incomplete
GL_MAP1_VERTEX_ATTRIB9_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB0_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB10_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB11_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB12_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB13_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB14_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB15_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB1_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB2_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB3_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB4_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB5_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB6_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB7_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB8_4_NV: Incomplete
GL_MAP2_VERTEX_ATTRIB9_4_NV: Incomplete
GL_MATRIX0_NV: Incomplete
GL_MATRIX1_NV: Incomplete
GL_MATRIX2_NV: Incomplete
GL_MATRIX3_NV: Incomplete
GL_MATRIX4_NV: Incomplete
GL_MATRIX5_NV: Incomplete
GL_MATRIX6_NV: Incomplete
GL_MATRIX7_NV: Incomplete
GL_MAX_TRACK_MATRICES_NV: Incomplete
GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV: Incomplete
GL_MODELVIEW_PROJECTION_NV: Incomplete
GL_PROGRAM_ERROR_POSITION_NV: Incomplete
GL_PROGRAM_LENGTH_NV: Incomplete
GL_PROGRAM_PARAMETER_NV: Incomplete
GL_PROGRAM_RESIDENT_NV: Incomplete
GL_PROGRAM_STRING_NV: Incomplete
GL_PROGRAM_TARGET_NV: Incomplete
GL_TRACK_MATRIX_NV: Incomplete
GL_TRACK_MATRIX_TRANSFORM_NV: Incomplete
GL_TRANSPOSE_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY0_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY10_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY11_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY12_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY13_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY14_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY15_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY1_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY2_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY3_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY4_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY5_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY6_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY7_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY8_NV: Incomplete
GL_VERTEX_ATTRIB_ARRAY9_NV: Incomplete
GL_VERTEX_PROGRAM_BINDING_NV: Incomplete
GL_VERTEX_PROGRAM_NV: Incomplete
GL_VERTEX_PROGRAM_POINT_SIZE_NV: Incomplete
GL_VERTEX_PROGRAM_TWO_SIDE_NV: Incomplete
GL_VERTEX_STATE_PROGRAM_NV: Incomplete

@_f
def glAreProgramsResidentNV(n, programs, residences) -> None: ...
@_f
def glBindProgramNV(target, id) -> None: ...
@_f
def glDeleteProgramsNV(n, programs) -> None: ...
@_f
def glExecuteProgramNV(target, id, params) -> None: ...
@_f
def glGenProgramsNV(n, programs) -> None: ...
@_f
def glGetProgramParameterdvNV(target, index, pname, params) -> None: ...
@_f
def glGetProgramParameterfvNV(target, index, pname, params) -> None: ...
@_f
def glGetProgramStringNV(id, pname, program) -> None: ...
@_f
def glGetProgramivNV(id, pname, params) -> None: ...
@_f
def glGetTrackMatrixivNV(target, address, pname, params) -> None: ...
@_f
def glGetVertexAttribPointervNV(index, pname, pointer) -> None: ...
@_f
def glGetVertexAttribdvNV(index, pname, params) -> None: ...
@_f
def glGetVertexAttribfvNV(index, pname, params) -> None: ...
@_f
def glGetVertexAttribivNV(index, pname, params) -> None: ...
@_f
def glIsProgramNV(id) -> None: ...
@_f
def glLoadProgramNV(target, id, len, program) -> None: ...
@_f
def glProgramParameter4dNV(target, index, x, y, z, w) -> None: ...
@_f
def glProgramParameter4dvNV(target, index, v) -> None: ...
@_f
def glProgramParameter4fNV(target, index, x, y, z, w) -> None: ...
@_f
def glProgramParameter4fvNV(target, index, v) -> None: ...
@_f
def glProgramParameters4dvNV(target, index, count, v) -> None: ...
@_f
def glProgramParameters4fvNV(target, index, count, v) -> None: ...
@_f
def glRequestResidentProgramsNV(n, programs) -> None: ...
@_f
def glTrackMatrixNV(target, address, matrix, transform) -> None: ...
@_f
def glVertexAttrib1dNV(index, x) -> None: ...
@_f
def glVertexAttrib1dvNV(index, v) -> None: ...
@_f
def glVertexAttrib1fNV(index, x) -> None: ...
@_f
def glVertexAttrib1fvNV(index, v) -> None: ...
@_f
def glVertexAttrib1sNV(index, x) -> None: ...
@_f
def glVertexAttrib1svNV(index, v) -> None: ...
@_f
def glVertexAttrib2dNV(index, x, y) -> None: ...
@_f
def glVertexAttrib2dvNV(index, v) -> None: ...
@_f
def glVertexAttrib2fNV(index, x, y) -> None: ...
@_f
def glVertexAttrib2fvNV(index, v) -> None: ...
@_f
def glVertexAttrib2sNV(index, x, y) -> None: ...
@_f
def glVertexAttrib2svNV(index, v) -> None: ...
@_f
def glVertexAttrib3dNV(index, x, y, z) -> None: ...
@_f
def glVertexAttrib3dvNV(index, v) -> None: ...
@_f
def glVertexAttrib3fNV(index, x, y, z) -> None: ...
@_f
def glVertexAttrib3fvNV(index, v) -> None: ...
@_f
def glVertexAttrib3sNV(index, x, y, z) -> None: ...
@_f
def glVertexAttrib3svNV(index, v) -> None: ...
@_f
def glVertexAttrib4dNV(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4dvNV(index, v) -> None: ...
@_f
def glVertexAttrib4fNV(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4fvNV(index, v) -> None: ...
@_f
def glVertexAttrib4sNV(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4svNV(index, v) -> None: ...
@_f
def glVertexAttrib4ubNV(index, x, y, z, w) -> None: ...
@_f
def glVertexAttrib4ubvNV(index, v) -> None: ...
@_f
def glVertexAttribPointerNV(index, fsize, type, stride, pointer) -> None: ...
@_f
def glVertexAttribs1dvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs1fvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs1svNV(index, count, v) -> None: ...
@_f
def glVertexAttribs2dvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs2fvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs2svNV(index, count, v) -> None: ...
@_f
def glVertexAttribs3dvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs3fvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs3svNV(index, count, v) -> None: ...
@_f
def glVertexAttribs4dvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs4fvNV(index, count, v) -> None: ...
@_f
def glVertexAttribs4svNV(index, count, v) -> None: ...
@_f
def glVertexAttribs4ubvNV(index, count, v) -> None: ...
