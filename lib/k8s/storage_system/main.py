from lib.k8s.storage_system.api import K8sStorageSystemApi
from lib.k8s.storage_system.info import K8sStorageSystemInfo


class K8sStorageSystem(
        K8sStorageSystemApi,
        K8sStorageSystemInfo
        ):
    def __init__(self):
        K8sStorageSystemApi.__init__(self)
        K8sStorageSystemInfo.__init__(self)
