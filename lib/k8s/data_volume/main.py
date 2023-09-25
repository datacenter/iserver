from lib.k8s.data_volume.api import K8sDataVolumeApi
from lib.k8s.data_volume.info import K8sDataVolumeInfo


class K8sDataVolume(
        K8sDataVolumeApi,
        K8sDataVolumeInfo
        ):
    def __init__(self):
        K8sDataVolumeApi.__init__(self)
        K8sDataVolumeInfo.__init__(self)
