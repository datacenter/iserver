from lib.k8s.local_volume.api import K8sLocalVolumeApi
from lib.k8s.local_volume.info import K8sLocalVolumeInfo


class K8sLocalVolume(
        K8sLocalVolumeApi,
        K8sLocalVolumeInfo
        ):
    def __init__(self):
        K8sLocalVolumeApi.__init__(self)
        K8sLocalVolumeInfo.__init__(self)
