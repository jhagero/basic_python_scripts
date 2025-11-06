from OpenGL.raw.GL.VERSION.GL_2_0 import *
from OpenGL import arrays as arrays, constant as constant, contextdata as contextdata, converters as converters, error as error, extensions as extensions, platform as platform, wrapper as wrapper
from OpenGL._bytes import as_8_bit as as_8_bit, bytes as bytes
from OpenGL.arrays.arraydatatype import ArrayDatatype as ArrayDatatype, GLenumArray as GLenumArray
from _typeshed import Incomplete

def glInitGl20VERSION(): ...

glDrawBuffers: Incomplete
glGetActiveAttrib: Incomplete
glGetActiveUniform: Incomplete
glGetAttachedShaders: Incomplete
glGetProgramiv: Incomplete
glGetProgramInfoLog: Incomplete
glGetShaderiv: Incomplete
glGetShaderInfoLog: Incomplete
glGetShaderSource: Incomplete
glGetVertexAttribdv: Incomplete
glGetVertexAttribfv: Incomplete
glGetVertexAttribiv: Incomplete
glGetVertexAttribPointerv: Incomplete
glShaderSource: Incomplete
glUniform1fv: Incomplete
glUniform2fv: Incomplete
glUniform3fv: Incomplete
glUniform4fv: Incomplete
glUniform1iv: Incomplete
glUniform2iv: Incomplete
glUniform3iv: Incomplete
glUniform4iv: Incomplete
glUniformMatrix2fv: Incomplete
glUniformMatrix3fv: Incomplete
glUniformMatrix4fv: Incomplete
glVertexAttrib1dv: Incomplete
glVertexAttrib1fv: Incomplete
glVertexAttrib1sv: Incomplete
glVertexAttrib2dv: Incomplete
glVertexAttrib2fv: Incomplete
glVertexAttrib2sv: Incomplete
glVertexAttrib3dv: Incomplete
glVertexAttrib3fv: Incomplete
glVertexAttrib3sv: Incomplete
glVertexAttrib4Nbv: Incomplete
glVertexAttrib4Niv: Incomplete
glVertexAttrib4Nsv: Incomplete
glVertexAttrib4Nubv: Incomplete
glVertexAttrib4Nuiv: Incomplete
glVertexAttrib4Nusv: Incomplete
glVertexAttrib4bv: Incomplete
glVertexAttrib4dv: Incomplete
glVertexAttrib4fv: Incomplete
glVertexAttrib4iv: Incomplete
glVertexAttrib4sv: Incomplete
glVertexAttrib4ubv: Incomplete
glVertexAttrib4uiv: Incomplete
glVertexAttrib4usv: Incomplete
GL_INFO_LOG_LENGTH: Incomplete
conv: Incomplete

def glGetUniformLocation(baseOperation, program, name): ...
def glGetAttribLocation(baseOperation, program, name): ...
def glVertexAttribPointer(baseOperation, index, size, type, normalized, stride, pointer): ...
