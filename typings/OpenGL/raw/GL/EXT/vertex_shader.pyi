from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_CURRENT_VERTEX_EXT: Incomplete
GL_FULL_RANGE_EXT: Incomplete
GL_INVARIANT_DATATYPE_EXT: Incomplete
GL_INVARIANT_EXT: Incomplete
GL_INVARIANT_VALUE_EXT: Incomplete
GL_LOCAL_CONSTANT_DATATYPE_EXT: Incomplete
GL_LOCAL_CONSTANT_EXT: Incomplete
GL_LOCAL_CONSTANT_VALUE_EXT: Incomplete
GL_LOCAL_EXT: Incomplete
GL_MATRIX_EXT: Incomplete
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT: Incomplete
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT: Incomplete
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT: Incomplete
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT: Incomplete
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT: Incomplete
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT: Incomplete
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT: Incomplete
GL_MAX_VERTEX_SHADER_LOCALS_EXT: Incomplete
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT: Incomplete
GL_MAX_VERTEX_SHADER_VARIANTS_EXT: Incomplete
GL_MVP_MATRIX_EXT: Incomplete
GL_NEGATIVE_ONE_EXT: Incomplete
GL_NEGATIVE_W_EXT: Incomplete
GL_NEGATIVE_X_EXT: Incomplete
GL_NEGATIVE_Y_EXT: Incomplete
GL_NEGATIVE_Z_EXT: Incomplete
GL_NORMALIZED_RANGE_EXT: Incomplete
GL_ONE_EXT: Incomplete
GL_OP_ADD_EXT: Incomplete
GL_OP_CLAMP_EXT: Incomplete
GL_OP_CROSS_PRODUCT_EXT: Incomplete
GL_OP_DOT3_EXT: Incomplete
GL_OP_DOT4_EXT: Incomplete
GL_OP_EXP_BASE_2_EXT: Incomplete
GL_OP_FLOOR_EXT: Incomplete
GL_OP_FRAC_EXT: Incomplete
GL_OP_INDEX_EXT: Incomplete
GL_OP_LOG_BASE_2_EXT: Incomplete
GL_OP_MADD_EXT: Incomplete
GL_OP_MAX_EXT: Incomplete
GL_OP_MIN_EXT: Incomplete
GL_OP_MOV_EXT: Incomplete
GL_OP_MULTIPLY_MATRIX_EXT: Incomplete
GL_OP_MUL_EXT: Incomplete
GL_OP_NEGATE_EXT: Incomplete
GL_OP_POWER_EXT: Incomplete
GL_OP_RECIP_EXT: Incomplete
GL_OP_RECIP_SQRT_EXT: Incomplete
GL_OP_ROUND_EXT: Incomplete
GL_OP_SET_GE_EXT: Incomplete
GL_OP_SET_LT_EXT: Incomplete
GL_OP_SUB_EXT: Incomplete
GL_OUTPUT_COLOR0_EXT: Incomplete
GL_OUTPUT_COLOR1_EXT: Incomplete
GL_OUTPUT_FOG_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD0_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD10_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD11_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD12_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD13_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD14_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD15_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD16_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD17_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD18_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD19_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD1_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD20_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD21_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD22_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD23_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD24_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD25_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD26_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD27_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD28_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD29_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD2_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD30_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD31_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD3_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD4_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD5_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD6_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD7_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD8_EXT: Incomplete
GL_OUTPUT_TEXTURE_COORD9_EXT: Incomplete
GL_OUTPUT_VERTEX_EXT: Incomplete
GL_SCALAR_EXT: Incomplete
GL_VARIANT_ARRAY_EXT: Incomplete
GL_VARIANT_ARRAY_POINTER_EXT: Incomplete
GL_VARIANT_ARRAY_STRIDE_EXT: Incomplete
GL_VARIANT_ARRAY_TYPE_EXT: Incomplete
GL_VARIANT_DATATYPE_EXT: Incomplete
GL_VARIANT_EXT: Incomplete
GL_VARIANT_VALUE_EXT: Incomplete
GL_VECTOR_EXT: Incomplete
GL_VERTEX_SHADER_BINDING_EXT: Incomplete
GL_VERTEX_SHADER_EXT: Incomplete
GL_VERTEX_SHADER_INSTRUCTIONS_EXT: Incomplete
GL_VERTEX_SHADER_INVARIANTS_EXT: Incomplete
GL_VERTEX_SHADER_LOCALS_EXT: Incomplete
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT: Incomplete
GL_VERTEX_SHADER_OPTIMIZED_EXT: Incomplete
GL_VERTEX_SHADER_VARIANTS_EXT: Incomplete
GL_W_EXT: Incomplete
GL_X_EXT: Incomplete
GL_Y_EXT: Incomplete
GL_ZERO_EXT: Incomplete
GL_Z_EXT: Incomplete

@_f
def glBeginVertexShaderEXT() -> None: ...
@_f
def glBindLightParameterEXT(light, value) -> None: ...
@_f
def glBindMaterialParameterEXT(face, value) -> None: ...
@_f
def glBindParameterEXT(value) -> None: ...
@_f
def glBindTexGenParameterEXT(unit, coord, value) -> None: ...
@_f
def glBindTextureUnitParameterEXT(unit, value) -> None: ...
@_f
def glBindVertexShaderEXT(id) -> None: ...
@_f
def glDeleteVertexShaderEXT(id) -> None: ...
@_f
def glDisableVariantClientStateEXT(id) -> None: ...
@_f
def glEnableVariantClientStateEXT(id) -> None: ...
@_f
def glEndVertexShaderEXT() -> None: ...
@_f
def glExtractComponentEXT(res, src, num) -> None: ...
@_f
def glGenSymbolsEXT(datatype, storagetype, range, components) -> None: ...
@_f
def glGenVertexShadersEXT(range) -> None: ...
@_f
def glGetInvariantBooleanvEXT(id, value, data) -> None: ...
@_f
def glGetInvariantFloatvEXT(id, value, data) -> None: ...
@_f
def glGetInvariantIntegervEXT(id, value, data) -> None: ...
@_f
def glGetLocalConstantBooleanvEXT(id, value, data) -> None: ...
@_f
def glGetLocalConstantFloatvEXT(id, value, data) -> None: ...
@_f
def glGetLocalConstantIntegervEXT(id, value, data) -> None: ...
@_f
def glGetVariantBooleanvEXT(id, value, data) -> None: ...
@_f
def glGetVariantFloatvEXT(id, value, data) -> None: ...
@_f
def glGetVariantIntegervEXT(id, value, data) -> None: ...
@_f
def glGetVariantPointervEXT(id, value, data) -> None: ...
@_f
def glInsertComponentEXT(res, src, num) -> None: ...
@_f
def glIsVariantEnabledEXT(id, cap) -> None: ...
@_f
def glSetInvariantEXT(id, type, addr) -> None: ...
@_f
def glSetLocalConstantEXT(id, type, addr) -> None: ...
@_f
def glShaderOp1EXT(op, res, arg1) -> None: ...
@_f
def glShaderOp2EXT(op, res, arg1, arg2) -> None: ...
@_f
def glShaderOp3EXT(op, res, arg1, arg2, arg3) -> None: ...
@_f
def glSwizzleEXT(res, in_, outX, outY, outZ, outW) -> None: ...
@_f
def glVariantPointerEXT(id, type, stride, addr) -> None: ...
@_f
def glVariantbvEXT(id, addr) -> None: ...
@_f
def glVariantdvEXT(id, addr) -> None: ...
@_f
def glVariantfvEXT(id, addr) -> None: ...
@_f
def glVariantivEXT(id, addr) -> None: ...
@_f
def glVariantsvEXT(id, addr) -> None: ...
@_f
def glVariantubvEXT(id, addr) -> None: ...
@_f
def glVariantuivEXT(id, addr) -> None: ...
@_f
def glVariantusvEXT(id, addr) -> None: ...
@_f
def glWriteMaskEXT(res, in_, outX, outY, outZ, outW) -> None: ...
