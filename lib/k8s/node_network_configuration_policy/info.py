import time
from lib import ip_helper
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

        conditions_mo = self.get(node_network_configuration_policy_mo, 'status:conditions')

        info['status'] = None
        info['reason'] = None
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                if condition_mo['status'] == 'True':
                    info['status'] = condition_mo['type']
                    info['reason'] = condition_mo['reason']

        info['available'] = False
        info['degraded'] = False
        info['progressing'] = False

        if info['status'] is not None:
            if info['status'] == 'Available':
                info['available'] = True

            if info['status'] == 'Degraded':
                info['degraded'] = True

            if info['status'] == 'Progressing':
                info['progressing'] = True

        if info['status'] is None:
            info['status'] = 'Unknown'
            info['reason'] = 'N/A'

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

            if key == 'names':
                key_found = True
                value_found = False
                for policy_name in value.split(','):
                    if filter_helper.match_string(policy_name, node_network_configuration_policy_info['name']):
                        value_found = True
                        break

                if not value_found:
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

    def get_new_nncp_name(self, base_name):
        if not self.is_node_network_configuration_policy(base_name, cache_enabled=False):
            return base_name

        while True:
            policy_name = '%s-%s' % (base_name, ip_helper.get_short_uuid())
            if not self.is_node_network_configuration_policy(policy_name, cache_enabled=False):
                return policy_name

    def set_nncp_interface_lldp_enabled(self, interface_name, policy_name=None, node_name=None):
        policy = {}
        policy['apiVersion'] = 'nmstate.io/v1'
        policy['kind'] = 'NodeNetworkConfigurationPolicy'
        policy['metadata'] = {}

        if policy_name is None:
            if node_name is not None:
                policy_name = 'enable-lldp-%s-%s' % (node_name, interface_name)
            else:
                policy_name = 'enable-lldp-%s' % (interface_name)

        policy['metadata']['name'] = self.get_new_nncp_name(policy_name)

        policy['spec'] = {}
        policy['spec']['nodeSelector'] = {}

        if node_name is not None:
            policy['spec']['nodeSelector']['kubernetes.io/hostname'] = node_name
        else:
            policy['spec']['nodeSelector']['node-role.kubernetes.io/worker'] = '""'

        policy['spec']['desiredState'] = {}
        policy['spec']['desiredState']['interfaces'] = []

        interface_mo = {}
        interface_mo['name'] = interface_name
        interface_mo['type'] = 'ethernet'
        interface_mo['lldp'] = {}
        interface_mo['lldp']['enabled'] = True
        policy['spec']['desiredState']['interfaces'].append(
            interface_mo
        )

        return self.create_node_network_configuration_policy(policy), policy['metadata']['name']

    def delete_node_network_configuration_policies(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Node Network Configuration Policies', before_newline=True, underline=True)

        items = self.get_node_network_configuration_policies(cache_enabled=False)
        if items is None:
            if my_output is not None:
                my_output.error('Failed to get nncp information')
            return False
        
        if len(items) == 0:
            if my_output is not None:
                my_output.default('- no nncp found')
            return True
        
        for item in items:
            if my_output is not None:
                my_output.default('- %s' % (item['name']))

            success = self.delete_node_network_configuration_policy_mo(item['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
            
            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nncp...')
                
                success = self.wait_no_node_network_configuration_policy(item['name'])
                if not success:
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False
                
        return True

    def wait_no_node_network_configuration_policy(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.is_node_network_configuration_policy(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_node_network_configuration_policy',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def wait_node_network_configuration_policy(self, policy_names=None, max_time=1800, log_error_on_timeout=True, my_output=None):
        start_time = int(time.time())
        while True:
            policies = self.get_node_network_configuration_policies(cache_enabled=False)
            if policies is not None:
                pending = []
                for policy in policies:
                    if policy_names is None or policy['name'] in policy_names:
                        if policy['status'] not in ['Available', 'Degraded']:
                            pending.append(
                                policy['name']
                            )

                if len(pending) == 0:
                    return True

                if my_output is not None:
                    my_output.default(
                        'Waiting for [%s]: %s' % (
                            len(pending),
                            ', '.join(pending)
                        )
                    )

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_node_network_configuration_policy',
                        'Max time reached'
                    )
                return False

            time.sleep(10)
