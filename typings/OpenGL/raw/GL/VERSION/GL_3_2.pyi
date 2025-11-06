from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_ALREADY_SIGNALED: Incomplete
GL_CONDITION_SATISFIED: Incomplete
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT: Incomplete
GL_CONTEXT_CORE_PROFILE_BIT: Incomplete
GL_CONTEXT_PROFILE_MASK: Incomplete
GL_DEPTH_CLAMP: Incomplete
GL_FIRST_VERTEX_CONVENTION: Incomplete
GL_FRAMEBUFFER_ATTACHMENT_LAYERED: Incomplete
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS: Incomplete
GL_GEOMETRY_INPUT_TYPE: Incomplete
GL_GEOMETRY_OUTPUT_TYPE: Incomplete
GL_GEOMETRY_SHADER: Incomplete
GL_GEOMETRY_VERTICES_OUT: Incomplete
GL_INT_SAMPLER_2D_MULTISAMPLE: Incomplete
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: Incomplete
GL_LAST_VERTEX_CONVENTION: Incomplete
GL_LINES_ADJACENCY: Incomplete
GL_LINE_STRIP_ADJACENCY: Incomplete
GL_MAX_COLOR_TEXTURE_SAMPLES: Incomplete
GL_MAX_DEPTH_TEXTURE_SAMPLES: Incomplete
GL_MAX_FRAGMENT_INPUT_COMPONENTS: Incomplete
GL_MAX_GEOMETRY_INPUT_COMPONENTS: Incomplete
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS: Incomplete
GL_MAX_GEOMETRY_OUTPUT_VERTICES: Incomplete
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS: Incomplete
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS: Incomplete
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS: Incomplete
GL_MAX_INTEGER_SAMPLES: Incomplete
GL_MAX_SAMPLE_MASK_WORDS: Incomplete
GL_MAX_SERVER_WAIT_TIMEOUT: Incomplete
GL_MAX_VERTEX_OUTPUT_COMPONENTS: Incomplete
GL_OBJECT_TYPE: Incomplete
GL_PROGRAM_POINT_SIZE: Incomplete
GL_PROVOKING_VERTEX: Incomplete
GL_PROXY_TEXTURE_2D_MULTISAMPLE: Incomplete
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY: Incomplete
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION: Incomplete
GL_SAMPLER_2D_MULTISAMPLE: Incomplete
GL_SAMPLER_2D_MULTISAMPLE_ARRAY: Incomplete
GL_SAMPLE_MASK: Incomplete
GL_SAMPLE_MASK_VALUE: Incomplete
GL_SAMPLE_POSITION: Incomplete
GL_SIGNALED: Incomplete
GL_SYNC_CONDITION: Incomplete
GL_SYNC_FENCE: Incomplete
GL_SYNC_FLAGS: Incomplete
GL_SYNC_FLUSH_COMMANDS_BIT: Incomplete
GL_SYNC_GPU_COMMANDS_COMPLETE: Incomplete
GL_SYNC_STATUS: Incomplete
GL_TEXTURE_2D_MULTISAMPLE: Incomplete
GL_TEXTURE_2D_MULTISAMPLE_ARRAY: Incomplete
GL_TEXTURE_BINDING_2D_MULTISAMPLE: Incomplete
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: Incomplete
GL_TEXTURE_CUBE_MAP_SEAMLESS: Incomplete
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: Incomplete
GL_TEXTURE_SAMPLES: Incomplete
GL_TIMEOUT_EXPIRED: Incomplete
GL_TIMEOUT_IGNORED: Incomplete
GL_TRIANGLES_ADJACENCY: Incomplete
GL_TRIANGLE_STRIP_ADJACENCY: Incomplete
GL_UNSIGNALED: Incomplete
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: Incomplete
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: Incomplete
GL_WAIT_FAILED: Incomplete

@_f
def glClientWaitSync(sync, flags, timeout) -> None: ...
@_f
def glDeleteSync(sync) -> None: ...
@_f
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex) -> None: ...
@_f
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex) -> None: ...
@_f
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex) -> None: ...
@_f
def glFenceSync(condition, flags) -> None: ...
@_f
def glFramebufferTexture(target, attachment, texture, level) -> None: ...
@_f
def glGetBufferParameteri64v(target, pname, params) -> None: ...
@_f
def glGetInteger64i_v(target, index, data) -> None: ...
@_f
def glGetInteger64v(pname, data) -> None: ...
@_f
def glGetMultisamplefv(pname, index, val) -> None: ...
@_f
def glGetSynciv(sync, pname, count, length, values) -> None: ...
@_f
def glIsSync(sync) -> None: ...
@_f
def glMultiDrawElementsBaseVertex(mode, count, type, indices, drawcount, basevertex) -> None: ...
@_f
def glProvokingVertex(mode) -> None: ...
@_f
def glSampleMaski(maskNumber, mask) -> None: ...
@_f
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations) -> None: ...
@_f
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations) -> None: ...
@_f
def glWaitSync(sync, flags, timeout) -> None: ...
