from lib.k8s.storage_cluster.api import K8sStorageClusterApi
from lib.k8s.storage_cluster.info import K8sStorageClusterInfo


class K8sStorageCluster(
        K8sStorageClusterApi,
        K8sStorageClusterInfo
        ):
    def __init__(self):
        K8sStorageClusterApi.__init__(self)
        K8sStorageClusterInfo.__init__(self)
