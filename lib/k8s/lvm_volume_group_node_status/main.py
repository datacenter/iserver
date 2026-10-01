from lib.k8s.lvm_volume_group_node_status.api import K8sLvmVolumeGroupNodeStatusApi
from lib.k8s.lvm_volume_group_node_status.info import K8sLvmVolumeGroupNodeStatusInfo
from lib.k8s.lvm_volume_group_node_status.delete import K8sLvmVolumeGroupNodeStatusDelete


class K8sLvmVolumeGroupNodeStatus(
        K8sLvmVolumeGroupNodeStatusApi,
        K8sLvmVolumeGroupNodeStatusInfo,
        K8sLvmVolumeGroupNodeStatusDelete
        ):
    def __init__(self):
        K8sLvmVolumeGroupNodeStatusApi.__init__(self)
        K8sLvmVolumeGroupNodeStatusInfo.__init__(self)
        K8sLvmVolumeGroupNodeStatusDelete.__init__(self)
