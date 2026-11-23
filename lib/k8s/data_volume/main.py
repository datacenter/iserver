from lib.k8s.data_volume.api import K8sDataVolumeApi
from lib.k8s.data_volume.info import K8sDataVolumeInfo
from lib.k8s.data_volume.create import K8sDataVolumeCreate
from lib.k8s.data_volume.delete import K8sDataVolumeDelete
from lib.k8s.data_volume.wait import K8sDataVolumeWait

class K8sDataVolume(
        K8sDataVolumeApi,
        K8sDataVolumeInfo,
        K8sDataVolumeCreate,
        K8sDataVolumeDelete,
        K8sDataVolumeWait
        ):
    def __init__(self):
        K8sDataVolumeApi.__init__(self)
        K8sDataVolumeInfo.__init__(self)
        K8sDataVolumeCreate.__init__(self)
        K8sDataVolumeDelete.__init__(self)
        K8sDataVolumeWait.__init__(self)
