from lib.k8s.local_volume_set.api import K8sLocalVolumeSetApi
from lib.k8s.local_volume_set.info import K8sLocalVolumeSetInfo


class K8sLocalVolumeSet(
        K8sLocalVolumeSetApi,
        K8sLocalVolumeSetInfo
        ):
    def __init__(self):
        K8sLocalVolumeSetApi.__init__(self)
        K8sLocalVolumeSetInfo.__init__(self)
