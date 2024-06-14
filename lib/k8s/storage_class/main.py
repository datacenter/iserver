from lib.k8s.storage_class.api import K8sStorageClassApi
from lib.k8s.storage_class.info import K8sStorageClassInfo


class K8sStorageClass(
        K8sStorageClassApi,
        K8sStorageClassInfo
        ):
    def __init__(self):
        K8sStorageClassApi.__init__(self)
        K8sStorageClassInfo.__init__(self)
