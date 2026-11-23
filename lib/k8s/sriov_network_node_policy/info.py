import json

from lib import filter_helper


class K8sSriovNetworkNodePolicyInfo():
    def __init__(self):
        self.sriov_network_node_policy = None

    def get_sriov_network_node_policy_info(self, sriov_network_node_policy_mo):
        if sriov_network_node_policy_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            sriov_network_node_policy_mo
        )
        info.update(metadata_info)

        info['device_type'] = self.get(sriov_network_node_policy_mo, 'spec:deviceType')
        info['device_typeT'] = info['device_type']
        if info['device_type'] is None:
            info['device_typeT'] = '--'

        info['is_rdma'] = self.get(sriov_network_node_policy_mo, 'spec:isRdma')

        info['nic_selector'] = self.get(sriov_network_node_policy_mo, 'spec:nicSelector')
        if len(info['nic_selector']) == 0:
            info['nic_selectorT'] = ['--']
        else:
            info['nic_selectorT'] = json.dumps(info['nic_selector'])[1:][:-1].split(',')

        info['interface'] = []
        if 'pfNames' in info['nic_selector']:
            for pf_name in info['nic_selector']['pfNames']:
                if len(pf_name.split('#')) == 1:
                    if pf_name not in info['interface']:
                        info['interface'].append(
                            pf_name
                        )
                    continue

                if len(pf_name.split('#')) == 2:
                    if pf_name.split('#')[0] not in info['interface']:
                        info['interface'].append(
                            pf_name.split('#')[0]
                        )
                    continue

        info['node_selector'] = self.get(sriov_network_node_policy_mo, 'spec:nodeSelector')
        if len(info['node_selector']) == 0:
            info['node_selectorT'] = ['--']
        else:
            info['node_selectorT'] = json.dumps(info['node_selector'])[1:][:-1].split(',')

        info['vfs'] = self.get(sriov_network_node_policy_mo, 'spec:numVfs')

        info['priority'] = self.get(sriov_network_node_policy_mo, 'spec:priority')
        info['priorityT'] = info['priority']
        if info['priority'] is None:
            info['priorityT'] = '--'

        info['resource_name'] = self.get(sriov_network_node_policy_mo, 'spec:resourceName')
        info['resource_nameT'] = info['resource_name']
        if info['resource_name'] is None or len(info['resource_name']) == 0:
            info['resource_nameT'] = '--'

        return info

    def get_sriov_network_node_policies_info(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_network_node_policy is not None:
                return self.sriov_network_node_policy

        managed_objects = self.get_sriov_network_node_policy_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.sriov_network_node_policy = []
        for managed_object in managed_objects:
            sriov_network_node_policy_info = {}
            sriov_network_node_policy_info['info'] = self.get_sriov_network_node_policy_info(
                managed_object
            )
            sriov_network_node_policy_info['mo'] = managed_object
            self.sriov_network_node_policy.append(
                sriov_network_node_policy_info
            )

        return self.sriov_network_node_policy

    def match_sriov_network_node_policy(self, sriov_network_node_policy_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_node_policy_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (sriov_network_node_policy_info['namespace'], sriov_network_node_policy_info['name'])):
                    return False

            if key == 'resource':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_node_policy_info['resource_name']):
                    return False

            if key == 'device_type':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_node_policy_info['device_type']):
                    return False

            if key == 'interface':
                key_found = True
                found = False
                for interface_name in sriov_network_node_policy_info['interface']:
                    if filter_helper.match_string(value, interface_name):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_sriov_network_node_policy',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_sriov_network_node_policies(self, object_filter=None, return_mo=False, sriov_network_info=False, cache_enabled=True):
        all_sriov_network_node_policies = self.get_sriov_network_node_policies_info(cache_enabled=cache_enabled)
        if all_sriov_network_node_policies is None:
            return None

        sriov_network_node_policies = []

        for sriov_network_node_policy_info in all_sriov_network_node_policies:
            if not self.match_sriov_network_node_policy(sriov_network_node_policy_info['info'], object_filter):
                continue

            if return_mo:
                sriov_network_node_policies.append(
                    sriov_network_node_policy_info['mo']
                )
                continue

            if sriov_network_info:
                sriov_network_node_policy_info['info']['sriov_network'] = []
                if len(sriov_network_node_policy_info['info']['resource_name']) > 0:
                    sriov_network_node_policy_info['info']['sriov_network'] = self.get_sriov_networks_with_resource_name(
                        sriov_network_node_policy_info['info']['resource_name']
                    )
                    if sriov_network_node_policy_info['info']['sriov_network'] is None:
                        self.log.error(
                            'get_sriov_network_node_policies',
                            'Failed to get sriov networks for policy: %s' % (sriov_network_node_policy_info['info']['name'])
                        )
                        sriov_network_node_policy_info['info']['sriov_network_count'] = 0
                    else:
                        sriov_network_node_policy_info['info']['sriov_network_count'] = len(
                            sriov_network_node_policy_info['info']['sriov_network']
                        )

            sriov_network_node_policies.append(
                sriov_network_node_policy_info['info']
            )

        return sriov_network_node_policies

    def is_sriov_network_node_policy(self, name, namespace='openshift-sriov-network-operator', cache_enabled=True):
        if self.get_sriov_network_node_policy(name, namespace=namespace, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_sriov_network_node_policy(self, name, namespace='openshift-sriov-network-operator', return_mo=False, sriov_network_info=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        sriov_network_node_policies = self.get_sriov_network_node_policies(
            object_filter=object_filter,
            return_mo=return_mo,
            sriov_network_info=sriov_network_info,
            cache_enabled=cache_enabled
        )
        if sriov_network_node_policies is None:
            return None

        if len(sriov_network_node_policies) == 1:
            return sriov_network_node_policies[0]

        return None

    def get_sriov_network_node_policy_with_resource_name(self, resource_name, return_mo=False, sriov_network_info=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'resource:%s' % (resource_name)
        )
        sriov_network_node_policies = self.get_sriov_network_node_policies(
            object_filter=object_filter,
            return_mo=return_mo,
            sriov_network_info=sriov_network_info,
            cache_enabled=cache_enabled
        )
        if sriov_network_node_policies is None:
            return None

        if len(sriov_network_node_policies) == 1:
            return sriov_network_node_policies[0]

        return None

    def get_sriov_network_node_policies_with_interface(self, interface_name, return_mo=False, sriov_network_info=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'interface:%s' % (interface_name)
        )
        sriov_network_node_policies = self.get_sriov_network_node_policies(
            object_filter=object_filter,
            return_mo=return_mo,
            sriov_network_info=sriov_network_info,
            cache_enabled=cache_enabled
        )
        return sriov_network_node_policies
