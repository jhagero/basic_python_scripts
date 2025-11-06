from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_BIAS_BY_NEGATIVE_ONE_HALF_NV: Incomplete
GL_COLOR_SUM_CLAMP_NV: Incomplete
GL_COMBINER0_NV: Incomplete
GL_COMBINER1_NV: Incomplete
GL_COMBINER2_NV: Incomplete
GL_COMBINER3_NV: Incomplete
GL_COMBINER4_NV: Incomplete
GL_COMBINER5_NV: Incomplete
GL_COMBINER6_NV: Incomplete
GL_COMBINER7_NV: Incomplete
GL_COMBINER_AB_DOT_PRODUCT_NV: Incomplete
GL_COMBINER_AB_OUTPUT_NV: Incomplete
GL_COMBINER_BIAS_NV: Incomplete
GL_COMBINER_CD_DOT_PRODUCT_NV: Incomplete
GL_COMBINER_CD_OUTPUT_NV: Incomplete
GL_COMBINER_COMPONENT_USAGE_NV: Incomplete
GL_COMBINER_INPUT_NV: Incomplete
GL_COMBINER_MAPPING_NV: Incomplete
GL_COMBINER_MUX_SUM_NV: Incomplete
GL_COMBINER_SCALE_NV: Incomplete
GL_COMBINER_SUM_OUTPUT_NV: Incomplete
GL_CONSTANT_COLOR0_NV: Incomplete
GL_CONSTANT_COLOR1_NV: Incomplete
GL_DISCARD_NV: Incomplete
GL_EXPAND_NEGATE_NV: Incomplete
GL_EXPAND_NORMAL_NV: Incomplete
GL_E_TIMES_F_NV: Incomplete
GL_FOG: Incomplete
GL_HALF_BIAS_NEGATE_NV: Incomplete
GL_HALF_BIAS_NORMAL_NV: Incomplete
GL_MAX_GENERAL_COMBINERS_NV: Incomplete
GL_NONE: Incomplete
GL_NUM_GENERAL_COMBINERS_NV: Incomplete
GL_PRIMARY_COLOR_NV: Incomplete
GL_REGISTER_COMBINERS_NV: Incomplete
GL_SCALE_BY_FOUR_NV: Incomplete
GL_SCALE_BY_ONE_HALF_NV: Incomplete
GL_SCALE_BY_TWO_NV: Incomplete
GL_SECONDARY_COLOR_NV: Incomplete
GL_SIGNED_IDENTITY_NV: Incomplete
GL_SIGNED_NEGATE_NV: Incomplete
GL_SPARE0_NV: Incomplete
GL_SPARE0_PLUS_SECONDARY_COLOR_NV: Incomplete
GL_SPARE1_NV: Incomplete
GL_TEXTURE0_ARB: Incomplete
GL_TEXTURE1_ARB: Incomplete
GL_UNSIGNED_IDENTITY_NV: Incomplete
GL_UNSIGNED_INVERT_NV: Incomplete
GL_VARIABLE_A_NV: Incomplete
GL_VARIABLE_B_NV: Incomplete
GL_VARIABLE_C_NV: Incomplete
GL_VARIABLE_D_NV: Incomplete
GL_VARIABLE_E_NV: Incomplete
GL_VARIABLE_F_NV: Incomplete
GL_VARIABLE_G_NV: Incomplete
GL_ZERO: Incomplete

@_f
def glCombinerInputNV(stage, portion, variable, input, mapping, componentUsage) -> None: ...
@_f
def glCombinerOutputNV(stage, portion, abOutput, cdOutput, sumOutput, scale, bias, abDotProduct, cdDotProduct, muxSum) -> None: ...
@_f
def glCombinerParameterfNV(pname, param) -> None: ...
@_f
def glCombinerParameterfvNV(pname, params) -> None: ...
@_f
def glCombinerParameteriNV(pname, param) -> None: ...
@_f
def glCombinerParameterivNV(pname, params) -> None: ...
@_f
def glFinalCombinerInputNV(variable, input, mapping, componentUsage) -> None: ...
@_f
def glGetCombinerInputParameterfvNV(stage, portion, variable, pname, params) -> None: ...
@_f
def glGetCombinerInputParameterivNV(stage, portion, variable, pname, params) -> None: ...
@_f
def glGetCombinerOutputParameterfvNV(stage, portion, pname, params) -> None: ...
@_f
def glGetCombinerOutputParameterivNV(stage, portion, pname, params) -> None: ...
@_f
def glGetFinalCombinerInputParameterfvNV(variable, pname, params) -> None: ...
@_f
def glGetFinalCombinerInputParameterivNV(variable, pname, params) -> None: ...
