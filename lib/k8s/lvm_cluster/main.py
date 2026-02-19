from lib.k8s.lvm_cluster.api import K8sLvmClusterApi
from lib.k8s.lvm_cluster.info import K8sLvmClusterInfo


class K8sLvmCluster(
        K8sLvmClusterApi,
        K8sLvmClusterInfo
        ):
    def __init__(self):
        K8sLvmClusterApi.__init__(self)
        K8sLvmClusterInfo.__init__(self)
