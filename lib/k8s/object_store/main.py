from lib.k8s.object_store.api import K8sObjectStoreApi
from lib.k8s.object_store.info import K8sObjectStoreInfo
from lib.k8s.object_store.create import K8sObjectStoreCreate
from lib.k8s.object_store.delete import K8sObjectStoreDelete
from lib.k8s.object_store.wait import K8sObjectStoreWait


class K8sObjectStore(
        K8sObjectStoreApi,
        K8sObjectStoreInfo,
        K8sObjectStoreCreate,
        K8sObjectStoreDelete,
        K8sObjectStoreWait
        ):
    def __init__(self):
        K8sObjectStoreApi.__init__(self)
        K8sObjectStoreInfo.__init__(self)
        K8sObjectStoreCreate.__init__(self)
        K8sObjectStoreDelete.__init__(self)
        K8sObjectStoreWait.__init__(self)
