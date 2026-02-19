from lib.k8s.logical_volume.api import K8sLogicalVolumeApi
from lib.k8s.logical_volume.info import K8sLogicalVolumeInfo


class K8sLogicalVolume(
        K8sLogicalVolumeApi,
        K8sLogicalVolumeInfo
        ):
    def __init__(self):
        K8sLogicalVolumeApi.__init__(self)
        K8sLogicalVolumeInfo.__init__(self)
