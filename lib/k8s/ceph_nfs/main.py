from lib.k8s.ceph_nfs.api import K8sCephNfsApi
from lib.k8s.ceph_nfs.info import K8sCephNfsInfo


class K8sCephNfs(
        K8sCephNfsApi,
        K8sCephNfsInfo
        ):
    def __init__(self):
        K8sCephNfsApi.__init__(self)
        K8sCephNfsInfo.__init__(self)
