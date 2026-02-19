from lib.k8s.node_network_configuration_policy.api import K8sNodeNetworkConfigurationPolicyApi
from lib.k8s.node_network_configuration_policy.generate import K8sNodeNetworkConfigurationPolicyGenerate
from lib.k8s.node_network_configuration_policy.info import K8sNodeNetworkConfigurationPolicyInfo
from lib.k8s.node_network_configuration_policy.input import K8sNodeNetworkConfigurationPolicyInput
from lib.k8s.node_network_configuration_policy.validate import K8sNodeNetworkConfigurationPolicyValidate


class K8sNodeNetworkConfigurationPolicy(
        K8sNodeNetworkConfigurationPolicyApi,
        K8sNodeNetworkConfigurationPolicyGenerate,
        K8sNodeNetworkConfigurationPolicyInfo,
        K8sNodeNetworkConfigurationPolicyInput,
        K8sNodeNetworkConfigurationPolicyValidate
        ):
    def __init__(self):
        K8sNodeNetworkConfigurationPolicyApi.__init__(self)
        K8sNodeNetworkConfigurationPolicyGenerate.__init__(self)
        K8sNodeNetworkConfigurationPolicyInfo.__init__(self)
        K8sNodeNetworkConfigurationPolicyInput.__init__(self)
        K8sNodeNetworkConfigurationPolicyValidate.__init__(self)
