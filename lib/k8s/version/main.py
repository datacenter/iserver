from lib.k8s.version.api import K8sVersionApi
from lib.k8s.version.info import K8sVersionInfo


class K8sVersion(
        K8sVersionApi,
        K8sVersionInfo
        ):
    def __init__(self):
        K8sVersionApi.__init__(self)
        K8sVersionInfo.__init__(self)
