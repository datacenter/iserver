from lib.k8s.splunk_cluster_master.api import K8sSplunkClusterMasterApi
from lib.k8s.splunk_cluster_master.info import K8sSplunkClusterMasterInfo


class K8sSplunkClusterMaster(
        K8sSplunkClusterMasterApi,
        K8sSplunkClusterMasterInfo
        ):
    def __init__(self):
        K8sSplunkClusterMasterApi.__init__(self)
        K8sSplunkClusterMasterInfo.__init__(self)
