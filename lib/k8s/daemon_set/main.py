from lib.k8s.daemon_set.api import K8sDaemonSetApi
from lib.k8s.daemon_set.info import K8sDaemonSetInfo


class K8sDaemonSet(
        K8sDaemonSetApi,
        K8sDaemonSetInfo
        ):
    def __init__(self):
        K8sDaemonSetApi.__init__(self)
        K8sDaemonSetInfo.__init__(self)
