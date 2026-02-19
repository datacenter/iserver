from lib.k8s.ceph_filesystem.api import K8sCephFilesystemApi
from lib.k8s.ceph_filesystem.info import K8sCephFilesystemInfo


class K8sCephFilesystem(
        K8sCephFilesystemApi,
        K8sCephFilesystemInfo
        ):
    def __init__(self):
        K8sCephFilesystemApi.__init__(self)
        K8sCephFilesystemInfo.__init__(self)
