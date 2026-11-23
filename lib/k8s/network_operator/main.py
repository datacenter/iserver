from lib.k8s.network_operator.api import K8sNetworkOperatorApi
from lib.k8s.network_operator.info import K8sNetworkOperatorInfo
from lib.k8s.network_operator.update import K8sNetworkOperatorUpdate
from lib.k8s.network_operator.wait import K8sNetworkOperatorWait


class K8sNetworkOperator(
        K8sNetworkOperatorApi,
        K8sNetworkOperatorInfo,
        K8sNetworkOperatorUpdate,
        K8sNetworkOperatorWait
        ):
    def __init__(self):
        K8sNetworkOperatorApi.__init__(self)
        K8sNetworkOperatorInfo.__init__(self)
        K8sNetworkOperatorUpdate.__init__(self)
        K8sNetworkOperatorWait.__init__(self)
