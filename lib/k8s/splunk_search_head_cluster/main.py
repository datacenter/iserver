from lib.k8s.splunk_search_head_cluster.api import K8sSplunkSearchHeadClusterApi
from lib.k8s.splunk_search_head_cluster.info import K8sSplunkSearchHeadClusterInfo


class K8sSplunkSearchHeadCluster(
        K8sSplunkSearchHeadClusterApi,
        K8sSplunkSearchHeadClusterInfo
        ):
    def __init__(self):
        K8sSplunkSearchHeadClusterApi.__init__(self)
        K8sSplunkSearchHeadClusterInfo.__init__(self)
