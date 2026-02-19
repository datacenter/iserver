from lib.k8s.splunk_cluster_manager.api import K8sSplunkClusterManagerApi
from lib.k8s.splunk_cluster_manager.info import K8sSplunkClusterManagerInfo


class K8sSplunkClusterManager(
        K8sSplunkClusterManagerApi,
        K8sSplunkClusterManagerInfo
        ):
    def __init__(self):
        K8sSplunkClusterManagerApi.__init__(self)
        K8sSplunkClusterManagerInfo.__init__(self)
