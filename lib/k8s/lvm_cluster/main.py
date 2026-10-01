from lib.k8s.lvm_cluster.api import K8sLvmClusterApi
from lib.k8s.lvm_cluster.info import K8sLvmClusterInfo
from lib.k8s.lvm_cluster.create import K8sLvmClusterCreate
from lib.k8s.lvm_cluster.delete import K8sLvmClusterDelete
from lib.k8s.lvm_cluster.wait import K8sLvmClusterWait


class K8sLvmCluster(
        K8sLvmClusterApi,
        K8sLvmClusterInfo,
        K8sLvmClusterCreate,
        K8sLvmClusterDelete,
        K8sLvmClusterWait
        ):
    def __init__(self):
        K8sLvmClusterApi.__init__(self)
        K8sLvmClusterInfo.__init__(self)
        K8sLvmClusterCreate.__init__(self)
        K8sLvmClusterDelete.__init__(self)
        K8sLvmClusterWait.__init__(self)