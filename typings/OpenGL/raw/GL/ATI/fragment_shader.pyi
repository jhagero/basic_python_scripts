from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_2X_BIT_ATI: Incomplete
GL_4X_BIT_ATI: Incomplete
GL_8X_BIT_ATI: Incomplete
GL_ADD_ATI: Incomplete
GL_BIAS_BIT_ATI: Incomplete
GL_BLUE_BIT_ATI: Incomplete
GL_CND0_ATI: Incomplete
GL_CND_ATI: Incomplete
GL_COLOR_ALPHA_PAIRING_ATI: Incomplete
GL_COMP_BIT_ATI: Incomplete
GL_CON_0_ATI: Incomplete
GL_CON_10_ATI: Incomplete
GL_CON_11_ATI: Incomplete
GL_CON_12_ATI: Incomplete
GL_CON_13_ATI: Incomplete
GL_CON_14_ATI: Incomplete
GL_CON_15_ATI: Incomplete
GL_CON_16_ATI: Incomplete
GL_CON_17_ATI: Incomplete
GL_CON_18_ATI: Incomplete
GL_CON_19_ATI: Incomplete
GL_CON_1_ATI: Incomplete
GL_CON_20_ATI: Incomplete
GL_CON_21_ATI: Incomplete
GL_CON_22_ATI: Incomplete
GL_CON_23_ATI: Incomplete
GL_CON_24_ATI: Incomplete
GL_CON_25_ATI: Incomplete
GL_CON_26_ATI: Incomplete
GL_CON_27_ATI: Incomplete
GL_CON_28_ATI: Incomplete
GL_CON_29_ATI: Incomplete
GL_CON_2_ATI: Incomplete
GL_CON_30_ATI: Incomplete
GL_CON_31_ATI: Incomplete
GL_CON_3_ATI: Incomplete
GL_CON_4_ATI: Incomplete
GL_CON_5_ATI: Incomplete
GL_CON_6_ATI: Incomplete
GL_CON_7_ATI: Incomplete
GL_CON_8_ATI: Incomplete
GL_CON_9_ATI: Incomplete
GL_DOT2_ADD_ATI: Incomplete
GL_DOT3_ATI: Incomplete
GL_DOT4_ATI: Incomplete
GL_EIGHTH_BIT_ATI: Incomplete
GL_FRAGMENT_SHADER_ATI: Incomplete
GL_GREEN_BIT_ATI: Incomplete
GL_HALF_BIT_ATI: Incomplete
GL_LERP_ATI: Incomplete
GL_MAD_ATI: Incomplete
GL_MOV_ATI: Incomplete
GL_MUL_ATI: Incomplete
GL_NEGATE_BIT_ATI: Incomplete
GL_NUM_FRAGMENT_CONSTANTS_ATI: Incomplete
GL_NUM_FRAGMENT_REGISTERS_ATI: Incomplete
GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI: Incomplete
GL_NUM_INSTRUCTIONS_PER_PASS_ATI: Incomplete
GL_NUM_INSTRUCTIONS_TOTAL_ATI: Incomplete
GL_NUM_LOOPBACK_COMPONENTS_ATI: Incomplete
GL_NUM_PASSES_ATI: Incomplete
GL_QUARTER_BIT_ATI: Incomplete
GL_RED_BIT_ATI: Incomplete
GL_REG_0_ATI: Incomplete
GL_REG_10_ATI: Incomplete
GL_REG_11_ATI: Incomplete
GL_REG_12_ATI: Incomplete
GL_REG_13_ATI: Incomplete
GL_REG_14_ATI: Incomplete
GL_REG_15_ATI: Incomplete
GL_REG_16_ATI: Incomplete
GL_REG_17_ATI: Incomplete
GL_REG_18_ATI: Incomplete
GL_REG_19_ATI: Incomplete
GL_REG_1_ATI: Incomplete
GL_REG_20_ATI: Incomplete
GL_REG_21_ATI: Incomplete
GL_REG_22_ATI: Incomplete
GL_REG_23_ATI: Incomplete
GL_REG_24_ATI: Incomplete
GL_REG_25_ATI: Incomplete
GL_REG_26_ATI: Incomplete
GL_REG_27_ATI: Incomplete
GL_REG_28_ATI: Incomplete
GL_REG_29_ATI: Incomplete
GL_REG_2_ATI: Incomplete
GL_REG_30_ATI: Incomplete
GL_REG_31_ATI: Incomplete
GL_REG_3_ATI: Incomplete
GL_REG_4_ATI: Incomplete
GL_REG_5_ATI: Incomplete
GL_REG_6_ATI: Incomplete
GL_REG_7_ATI: Incomplete
GL_REG_8_ATI: Incomplete
GL_REG_9_ATI: Incomplete
GL_SATURATE_BIT_ATI: Incomplete
GL_SECONDARY_INTERPOLATOR_ATI: Incomplete
GL_SUB_ATI: Incomplete
GL_SWIZZLE_STQ_ATI: Incomplete
GL_SWIZZLE_STQ_DQ_ATI: Incomplete
GL_SWIZZLE_STRQ_ATI: Incomplete
GL_SWIZZLE_STRQ_DQ_ATI: Incomplete
GL_SWIZZLE_STR_ATI: Incomplete
GL_SWIZZLE_STR_DR_ATI: Incomplete

@_f
def glAlphaFragmentOp1ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod) -> None: ...
@_f
def glAlphaFragmentOp2ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod) -> None: ...
@_f
def glAlphaFragmentOp3ATI(op, dst, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod, arg3, arg3Rep, arg3Mod) -> None: ...
@_f
def glBeginFragmentShaderATI() -> None: ...
@_f
def glBindFragmentShaderATI(id) -> None: ...
@_f
def glColorFragmentOp1ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod) -> None: ...
@_f
def glColorFragmentOp2ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod) -> None: ...
@_f
def glColorFragmentOp3ATI(op, dst, dstMask, dstMod, arg1, arg1Rep, arg1Mod, arg2, arg2Rep, arg2Mod, arg3, arg3Rep, arg3Mod) -> None: ...
@_f
def glDeleteFragmentShaderATI(id) -> None: ...
@_f
def glEndFragmentShaderATI() -> None: ...
@_f
def glGenFragmentShadersATI(range) -> None: ...
@_f
def glPassTexCoordATI(dst, coord, swizzle) -> None: ...
@_f
def glSampleMapATI(dst, interp, swizzle) -> None: ...
@_f
def glSetFragmentShaderConstantATI(dst, value) -> None: ...
