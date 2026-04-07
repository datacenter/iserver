from lib.k8s.node_network_configuration_policy.api import K8sNodeNetworkConfigurationPolicyApi
from lib.k8s.node_network_configuration_policy.info import K8sNodeNetworkConfigurationPolicyInfo
from lib.k8s.node_network_configuration_policy.bridge import K8sNodeNetworkConfigurationPolicyBridge
from lib.k8s.node_network_configuration_policy.create import K8sNodeNetworkConfigurationPolicyCreate
from lib.k8s.node_network_configuration_policy.delete import K8sNodeNetworkConfigurationPolicyDelete
from lib.k8s.node_network_configuration_policy.lldp import K8sNodeNetworkConfigurationPolicyLldp
from lib.k8s.node_network_configuration_policy.wait import K8sNodeNetworkConfigurationPolicyWait


class K8sNodeNetworkConfigurationPolicy(
        K8sNodeNetworkConfigurationPolicyApi,
        K8sNodeNetworkConfigurationPolicyInfo,
        K8sNodeNetworkConfigurationPolicyBridge,
        K8sNodeNetworkConfigurationPolicyCreate,
        K8sNodeNetworkConfigurationPolicyDelete,
        K8sNodeNetworkConfigurationPolicyLldp,
        K8sNodeNetworkConfigurationPolicyWait
        ):
    def __init__(self):
        K8sNodeNetworkConfigurationPolicyApi.__init__(self)
        K8sNodeNetworkConfigurationPolicyInfo.__init__(self)
        K8sNodeNetworkConfigurationPolicyBridge.__init__(self)
        K8sNodeNetworkConfigurationPolicyCreate.__init__(self)
        K8sNodeNetworkConfigurationPolicyDelete.__init__(self)
        K8sNodeNetworkConfigurationPolicyLldp.__init__(self)
        K8sNodeNetworkConfigurationPolicyWait.__init__(self)
