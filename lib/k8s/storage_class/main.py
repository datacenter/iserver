from lib.k8s.storage_class.api import K8sStorageClassApi
from lib.k8s.storage_class.info import K8sStorageClassInfo
from lib.k8s.storage_class.default import K8sStorageClassDefault
from lib.k8s.storage_class.lso import K8sStorageClassLso
from lib.k8s.storage_class.lvm import K8sStorageClassLvm
from lib.k8s.storage_class.wait import K8sStorageClassWait

class K8sStorageClass(
        K8sStorageClassApi,
        K8sStorageClassInfo,
        K8sStorageClassDefault,
        K8sStorageClassLso,
        K8sStorageClassLvm,
        K8sStorageClassWait
        ):
    def __init__(self):
        K8sStorageClassApi.__init__(self)
        K8sStorageClassInfo.__init__(self)
        K8sStorageClassDefault.__init__(self)
        K8sStorageClassLso.__init__(self)
        K8sStorageClassLvm.__init__(self)
        K8sStorageClassWait.__init__(self)
