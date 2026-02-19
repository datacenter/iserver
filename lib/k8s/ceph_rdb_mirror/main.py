from lib.k8s.ceph_rdb_mirror.api import K8sCephRdbMirrorApi
from lib.k8s.ceph_rdb_mirror.info import K8sCephRdbMirrorInfo


class K8sCephRdbMirror(
        K8sCephRdbMirrorApi,
        K8sCephRdbMirrorInfo
        ):
    def __init__(self):
        K8sCephRdbMirrorApi.__init__(self)
        K8sCephRdbMirrorInfo.__init__(self)
