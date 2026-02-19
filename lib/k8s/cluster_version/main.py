from lib.k8s.cluster_version.api import K8sClusterVersionApi
from lib.k8s.cluster_version.info import K8sClusterVersionInfo


class K8sClusterVersion(
        K8sClusterVersionApi,
        K8sClusterVersionInfo
        ):
    def __init__(self):
        K8sClusterVersionApi.__init__(self)
        K8sClusterVersionInfo.__init__(self)
