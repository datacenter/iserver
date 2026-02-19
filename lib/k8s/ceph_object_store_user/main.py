from lib.k8s.ceph_object_store_user.api import K8sCephObjectStoreUserApi
from lib.k8s.ceph_object_store_user.info import K8sCephObjectStoreUserInfo


class K8sCephObjectStoreUser(
        K8sCephObjectStoreUserApi,
        K8sCephObjectStoreUserInfo
        ):
    def __init__(self):
        K8sCephObjectStoreUserApi.__init__(self)
        K8sCephObjectStoreUserInfo.__init__(self)
