from lib.k8s.node_network_configuration_enactment.api import K8sNodeNetworkConfigurationEnactmentApi
from lib.k8s.node_network_configuration_enactment.info import K8sNodeNetworkConfigurationEnactmentInfo


class K8sNodeNetworkConfigurationEnactment(
        K8sNodeNetworkConfigurationEnactmentApi,
        K8sNodeNetworkConfigurationEnactmentInfo
        ):
    def __init__(self):
        K8sNodeNetworkConfigurationEnactmentApi.__init__(self)
        K8sNodeNetworkConfigurationEnactmentInfo.__init__(self)
