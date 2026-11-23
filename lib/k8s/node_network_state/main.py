from lib.k8s.node_network_state.api import K8sNodeNetworkStateApi
from lib.k8s.node_network_state.info import K8sNodeNetworkStateInfo
from lib.k8s.node_network_state.dns import K8sNodeNetworkStateDnsInfo
from lib.k8s.node_network_state.interface import K8sNodeNetworkStateInterfaceInfo
from lib.k8s.node_network_state.route import K8sNodeNetworkStateRouteInfo
from lib.k8s.node_network_state.wait import K8sNodeNetworkStateWait


class K8sNodeNetworkState(
        K8sNodeNetworkStateApi,
        K8sNodeNetworkStateInfo,
        K8sNodeNetworkStateDnsInfo,
        K8sNodeNetworkStateInterfaceInfo,
        K8sNodeNetworkStateRouteInfo,
        K8sNodeNetworkStateWait
        ):
    def __init__(self):
        K8sNodeNetworkStateApi.__init__(self)
        K8sNodeNetworkStateInfo.__init__(self)
        K8sNodeNetworkStateDnsInfo.__init__(self)
        K8sNodeNetworkStateInterfaceInfo.__init__(self)
        K8sNodeNetworkStateRouteInfo.__init__(self)
        K8sNodeNetworkStateWait.__init__(self)
