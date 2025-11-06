from OpenGL.raw.WGL._types import *
from OpenGL import arrays as arrays
from _typeshed import Incomplete

ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV: Incomplete
ERROR_MISSING_AFFINITY_MASK_NV: Incomplete

@_f
def wglCreateAffinityDCNV(phGpuList) -> None: ...
@_f
def wglDeleteDCNV(hdc) -> None: ...
@_f
def wglEnumGpuDevicesNV(hGpu, iDeviceIndex, lpGpuDevice) -> None: ...
@_f
def wglEnumGpusFromAffinityDCNV(hAffinityDC, iGpuIndex, hGpu) -> None: ...
@_f
def wglEnumGpusNV(iGpuIndex, phGpu) -> None: ...
