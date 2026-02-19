from lib.k8s.splunk_indexer_cluster.api import K8sSplunkIndexerClusterApi
from lib.k8s.splunk_indexer_cluster.info import K8sSplunkIndexerClusterInfo


class K8sSplunkIndexerCluster(
        K8sSplunkIndexerClusterApi,
        K8sSplunkIndexerClusterInfo
        ):
    def __init__(self):
        K8sSplunkIndexerClusterApi.__init__(self)
        K8sSplunkIndexerClusterInfo.__init__(self)
