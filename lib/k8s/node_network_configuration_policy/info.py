from lib import filter_helper


class K8sNodeNetworkConfigurationPolicyInfo():
    def __init__(self):
        self.node_network_configuration_policy = None

    def get_node_network_configuration_policy_info(self, node_network_configuration_policy_mo):
        if node_network_configuration_policy_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            node_network_configuration_policy_mo
        )
        info.update(metadata_info)

        return info

    def get_node_network_configuration_policies_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_configuration_policy is not None:
                return self.node_network_configuration_policy

        managed_objects = self.get_node_network_configuration_policy_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_network_configuration_policy = []
        for managed_object in managed_objects:
            node_network_configuration_policy_info = {}
            node_network_configuration_policy_info['info'] = self.get_node_network_configuration_policy_info(
                managed_object
            )
            node_network_configuration_policy_info['mo'] = managed_object
            self.node_network_configuration_policy.append(
                node_network_configuration_policy_info
            )

        return self.node_network_configuration_policy

    def match_node_network_configuration_policy(self, node_network_configuration_policy_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_network_configuration_policy_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_network_configuration_policy',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_network_configuration_policies(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_node_network_configuration_policies = self.get_node_network_configuration_policies_info(cache_enabled=cache_enabled)
        if all_node_network_configuration_policies is None:
            return None

        node_network_configuration_policies = []

        for node_network_configuration_policy_info in all_node_network_configuration_policies:
            if not self.match_node_network_configuration_policy(node_network_configuration_policy_info['info'], object_filter):
                continue

            if return_mo:
                node_network_configuration_policies.append(
                    node_network_configuration_policy_info['mo']
                )
                continue

            node_network_configuration_policies.append(
                node_network_configuration_policy_info['info']
            )

        return node_network_configuration_policies

    def is_node_network_configuration_policy(self, name, cache_enabled=True):
        if self.get_node_network_configuration_policy(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_network_configuration_policy(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        node_network_configuration_policies = self.get_node_network_configuration_policies(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_network_configuration_policies is None:
            return None

        if len(node_network_configuration_policies) == 1:
            return node_network_configuration_policies[0]

        return None
