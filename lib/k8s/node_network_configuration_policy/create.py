from lib import ip_helper


class K8sNodeNetworkConfigurationPolicyCreate():
    def __init__(self):
        pass

    def get_new_nncp_name(self, base_name):
        if not self.is_node_network_configuration_policy(base_name, cache_enabled=False):
            return base_name

        while True:
            policy_name = '%s-%s' % (base_name, ip_helper.get_short_uuid())
            if not self.is_node_network_configuration_policy(policy_name, cache_enabled=False):
                return policy_name
