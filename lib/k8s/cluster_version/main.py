from lib.k8s.cluster_version.api import K8sClusterVersionApi
from lib.k8s.cluster_version.info import K8sClusterVersionInfo
from lib.k8s.cluster_version.enable import K8sClusterVersionEnable
from lib.k8s.cluster_version.disable import K8sClusterVersionDisable


class K8sClusterVersion(
        K8sClusterVersionApi,
        K8sClusterVersionInfo,
        K8sClusterVersionEnable,
        K8sClusterVersionDisable
        ):
    def __init__(self):
        K8sClusterVersionApi.__init__(self)
        K8sClusterVersionInfo.__init__(self)
        K8sClusterVersionEnable.__init__(self)
        K8sClusterVersionDisable.__init__(self)
