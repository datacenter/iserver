from lib.k8s.cluster_service_version.api import K8sClusterServiceVersionApi
from lib.k8s.cluster_service_version.info import K8sClusterServiceVersionInfo


class K8sClusterServiceVersion(
        K8sClusterServiceVersionApi,
        K8sClusterServiceVersionInfo
        ):
    def __init__(self):
        K8sClusterServiceVersionApi.__init__(self)
        K8sClusterServiceVersionInfo.__init__(self)
