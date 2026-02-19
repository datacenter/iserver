from lib.k8s.portworx_storage_node.api import K8sPortworxStorageNodeApi
from lib.k8s.portworx_storage_node.info import K8sPortworxStorageNodeInfo


class K8sPortworxStorageNode(
        K8sPortworxStorageNodeApi,
        K8sPortworxStorageNodeInfo
        ):
    def __init__(self):
        K8sPortworxStorageNodeApi.__init__(self)
        K8sPortworxStorageNodeInfo.__init__(self)
