from lib.k8s.node_network_configuration_policy.api import K8sNodeNetworkConfigurationPolicyApi
from lib.k8s.node_network_configuration_policy.info import K8sNodeNetworkConfigurationPolicyInfo


class K8sNodeNetworkConfigurationPolicy(
        K8sNodeNetworkConfigurationPolicyApi,
        K8sNodeNetworkConfigurationPolicyInfo
        ):
    def __init__(self):
        K8sNodeNetworkConfigurationPolicyApi.__init__(self)
        K8sNodeNetworkConfigurationPolicyInfo.__init__(self)
