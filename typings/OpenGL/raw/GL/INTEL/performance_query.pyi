from OpenGL.raw.GL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

GL_PERFQUERY_COUNTER_DATA_BOOL32_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DATA_DOUBLE_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DATA_FLOAT_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DATA_UINT32_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DATA_UINT64_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DESC_LENGTH_MAX_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DURATION_NORM_INTEL: Incomplete
GL_PERFQUERY_COUNTER_DURATION_RAW_INTEL: Incomplete
GL_PERFQUERY_COUNTER_EVENT_INTEL: Incomplete
GL_PERFQUERY_COUNTER_NAME_LENGTH_MAX_INTEL: Incomplete
GL_PERFQUERY_COUNTER_RAW_INTEL: Incomplete
GL_PERFQUERY_COUNTER_THROUGHPUT_INTEL: Incomplete
GL_PERFQUERY_COUNTER_TIMESTAMP_INTEL: Incomplete
GL_PERFQUERY_DONOT_FLUSH_INTEL: Incomplete
GL_PERFQUERY_FLUSH_INTEL: Incomplete
GL_PERFQUERY_GLOBAL_CONTEXT_INTEL: Incomplete
GL_PERFQUERY_GPA_EXTENDED_COUNTERS_INTEL: Incomplete
GL_PERFQUERY_QUERY_NAME_LENGTH_MAX_INTEL: Incomplete
GL_PERFQUERY_SINGLE_CONTEXT_INTEL: Incomplete
GL_PERFQUERY_WAIT_INTEL: Incomplete

@_f
def glBeginPerfQueryINTEL(queryHandle) -> None: ...
@_f
def glCreatePerfQueryINTEL(queryId, queryHandle) -> None: ...
@_f
def glDeletePerfQueryINTEL(queryHandle) -> None: ...
@_f
def glEndPerfQueryINTEL(queryHandle) -> None: ...
@_f
def glGetFirstPerfQueryIdINTEL(queryId) -> None: ...
@_f
def glGetNextPerfQueryIdINTEL(queryId, nextQueryId) -> None: ...
@_f
def glGetPerfCounterInfoINTEL(queryId, counterId, counterNameLength, counterName, counterDescLength, counterDesc, counterOffset, counterDataSize, counterTypeEnum, counterDataTypeEnum, rawCounterMaxValue) -> None: ...
@_f
def glGetPerfQueryDataINTEL(queryHandle, flags, dataSize, data, bytesWritten) -> None: ...
@_f
def glGetPerfQueryIdByNameINTEL(queryName, queryId) -> None: ...
@_f
def glGetPerfQueryInfoINTEL(queryId, queryNameLength, queryName, dataSize, noCounters, noInstances, capsMask) -> None: ...
