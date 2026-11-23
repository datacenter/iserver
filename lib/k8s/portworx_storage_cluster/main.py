from lib.k8s.portworx_storage_cluster.api import K8sPortworxStorageClusterApi
from lib.k8s.portworx_storage_cluster.info import K8sPortworxStorageClusterInfo
from lib.k8s.portworx_storage_cluster.create import K8sPortworxStorageClusterCreate
from lib.k8s.portworx_storage_cluster.delete import K8sPortworxStorageClusterDelete
from lib.k8s.portworx_storage_cluster.wait import K8sPortworxStorageClusterWait


class K8sPortworxStorageCluster(
        K8sPortworxStorageClusterApi,
        K8sPortworxStorageClusterInfo,
        K8sPortworxStorageClusterCreate,
        K8sPortworxStorageClusterDelete,
        K8sPortworxStorageClusterWait
        ):
    def __init__(self):
        K8sPortworxStorageClusterApi.__init__(self)
        K8sPortworxStorageClusterInfo.__init__(self)
        K8sPortworxStorageClusterCreate.__init__(self)
        K8sPortworxStorageClusterDelete.__init__(self)
        K8sPortworxStorageClusterWait.__init__(self)
