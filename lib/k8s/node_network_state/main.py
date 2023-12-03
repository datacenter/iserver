from lib.k8s.node_network_state.api import K8sNodeNetworkStateApi
from lib.k8s.node_network_state.info import K8sNodeNetworkStateInfo


class K8sNodeNetworkState(
        K8sNodeNetworkStateApi,
        K8sNodeNetworkStateInfo
        ):
    def __init__(self):
        K8sNodeNetworkStateApi.__init__(self)
        K8sNodeNetworkStateInfo.__init__(self)
