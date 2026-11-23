from lib.k8s.cluster_service_version.api import K8sClusterServiceVersionApi
from lib.k8s.cluster_service_version.info import K8sClusterServiceVersionInfo
from lib.k8s.cluster_service_version.wait import K8sClusterServiceVersionWait


class K8sClusterServiceVersion(
        K8sClusterServiceVersionApi,
        K8sClusterServiceVersionInfo,
        K8sClusterServiceVersionWait
        ):
    def __init__(self):
        K8sClusterServiceVersionApi.__init__(self)
        K8sClusterServiceVersionInfo.__init__(self)
        K8sClusterServiceVersionWait.__init__(self)
