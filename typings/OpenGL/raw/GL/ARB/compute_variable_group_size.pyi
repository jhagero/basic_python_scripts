from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB: Incomplete
GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB: Incomplete
GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB: Incomplete
GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB: Incomplete

@_f
def glDispatchComputeGroupSizeARB(num_groups_x, num_groups_y, num_groups_z, group_size_x, group_size_y, group_size_z) -> None: ...
