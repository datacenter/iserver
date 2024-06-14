from lib.k8s.sriov_network_node_state.api import K8sSriovNetworkNodeStateApi
from lib.k8s.sriov_network_node_state.info import K8sSriovNetworkNodeStateInfo


class K8sSriovNetworkNodeState(
        K8sSriovNetworkNodeStateApi,
        K8sSriovNetworkNodeStateInfo
        ):
    def __init__(self):
        K8sSriovNetworkNodeStateApi.__init__(self)
        K8sSriovNetworkNodeStateInfo.__init__(self)

        self.network_vendor = {}
        self.network_vendor['1137'] = 'Cisco'
        self.network_vendor['8086'] = 'Intel'

        self.network_vendor_device = {}
        self.network_vendor_device['8086'] = {}
        self.network_vendor_device['8086']['158b'] = 'Ethernet Controller XXV710 for 25GbE SFP28'
        self.network_vendor_device['1137'] = {}
