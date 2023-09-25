from lib.k8s.sriov_network.api import K8sSriovNetworkApi
from lib.k8s.sriov_network.info import K8sSriovNetworkInfo


class K8sSriovNetwork(
        K8sSriovNetworkApi,
        K8sSriovNetworkInfo
        ):
    def __init__(self):
        K8sSriovNetworkApi.__init__(self)
        K8sSriovNetworkInfo.__init__(self)
