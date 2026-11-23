from lib.k8s.network.api import K8sNetworkApi
from lib.k8s.network.info import K8sNetworkInfo


class K8sNetwork(
        K8sNetworkApi,
        K8sNetworkInfo
        ):
    def __init__(self):
        K8sNetworkApi.__init__(self)
        K8sNetworkInfo.__init__(self)
