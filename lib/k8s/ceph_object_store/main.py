from lib.k8s.ceph_object_store.api import K8sCephObjectStoreApi
from lib.k8s.ceph_object_store.info import K8sCephObjectStoreInfo


class K8sCephObjectStore(
        K8sCephObjectStoreApi,
        K8sCephObjectStoreInfo
        ):
    def __init__(self):
        K8sCephObjectStoreApi.__init__(self)
        K8sCephObjectStoreInfo.__init__(self)
