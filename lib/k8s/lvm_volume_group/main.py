from lib.k8s.lvm_volume_group.api import K8sLvmVolumeGroupApi
from lib.k8s.lvm_volume_group.info import K8sLvmVolumeGroupInfo
from lib.k8s.lvm_volume_group.delete import K8sLvmVolumeGroupDelete


class K8sLvmVolumeGroup(
        K8sLvmVolumeGroupApi,
        K8sLvmVolumeGroupInfo,
        K8sLvmVolumeGroupDelete
        ):
    def __init__(self):
        K8sLvmVolumeGroupApi.__init__(self)
        K8sLvmVolumeGroupInfo.__init__(self)
        K8sLvmVolumeGroupDelete.__init__(self)
