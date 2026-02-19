from lib.k8s.network_operator.api import K8sNetworkOperatorApi
from lib.k8s.network_operator.info import K8sNetworkOperatorInfo


class K8sNetworkOperator(
        K8sNetworkOperatorApi,
        K8sNetworkOperatorInfo
        ):
    def __init__(self):
        K8sNetworkOperatorApi.__init__(self)
        K8sNetworkOperatorInfo.__init__(self)
