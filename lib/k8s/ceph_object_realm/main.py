from lib.k8s.ceph_object_realm.api import K8sCephObjectRealmApi
from lib.k8s.ceph_object_realm.info import K8sCephObjectRealmInfo


class K8sCephObjectRealm(
        K8sCephObjectRealmApi,
        K8sCephObjectRealmInfo
        ):
    def __init__(self):
        K8sCephObjectRealmApi.__init__(self)
        K8sCephObjectRealmInfo.__init__(self)
