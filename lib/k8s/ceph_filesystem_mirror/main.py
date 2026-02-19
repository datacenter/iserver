from lib.k8s.ceph_filesystem_mirror.api import K8sCephFilesystemMirrorApi
from lib.k8s.ceph_filesystem_mirror.info import K8sCephFilesystemMirrorInfo


class K8sCephFilesystemMirror(
        K8sCephFilesystemMirrorApi,
        K8sCephFilesystemMirrorInfo
        ):
    def __init__(self):
        K8sCephFilesystemMirrorApi.__init__(self)
        K8sCephFilesystemMirrorInfo.__init__(self)
