import json

from lib import filter_helper


class K8sSriovNetworkInfo():
    def __init__(self):
        self.sriov_network = None

    def get_sriov_network_info(self, sriov_network_mo):
        if sriov_network_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            sriov_network_mo
        )
        info.update(metadata_info)

        info['network_namespace'] = self.get(sriov_network_mo, 'spec:networkNamespace')
        info['resource_name'] = self.get(sriov_network_mo, 'spec:resourceName')
        info['vlan'] = self.get(sriov_network_mo, 'spec:vlan')
        info['vlanT'] = info['vlan']
        if info['vlan'] is None:
            info['vlanT'] = '--'

        info['spoof'] = self.get(sriov_network_mo, 'spec:spoofChk', on_none="on (*)", on_error=None)
        info['trust'] = self.get(sriov_network_mo, 'spec:trust', on_none="off (*)", on_error=None)

        info['capabilities'] = self.get(sriov_network_mo, 'spec:capabilities', on_none=None, on_error=None)
        info['capabilitiesT'] = ['--']
        if info['capabilities'] is not None:
            info['capabilitiesT'] = []
            capabilities = json.loads(info['capabilities'])
            for key in capabilities:
                info['capabilitiesT'].append(
                    '%s: %s' % (
                        key,
                        capabilities[key]
                    )
                )

        info['ipam'] = self.get(sriov_network_mo, 'spec:ipam')
        info['ipamT'] = ['--']
        if info['ipam'] is not None:
            info['ipamT'] = json.dumps(json.loads(info['ipam']), indent=4).split('\n')

        return info

    def get_sriov_networks_info(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_network is not None:
                return self.sriov_network

        managed_objects = self.get_sriov_network_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.sriov_network = []
        for managed_object in managed_objects:
            sriov_network_info = {}
            sriov_network_info['info'] = self.get_sriov_network_info(
                managed_object
            )
            sriov_network_info['mo'] = managed_object
            self.sriov_network.append(
                sriov_network_info
            )

        return self.sriov_network

    def match_sriov_network(self, sriov_network_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (sriov_network_info['namespace'], sriov_network_info['name'])):
                    return False

            if key == 'resource':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_info['resource_name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_sriov_network',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_sriov_networks(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_sriov_networks = self.get_sriov_networks_info(cache_enabled=cache_enabled)
        if all_sriov_networks is None:
            return None

        sriov_networks = []

        for sriov_network_info in all_sriov_networks:
            if not self.match_sriov_network(sriov_network_info['info'], object_filter):
                continue

            if return_mo:
                sriov_networks.append(
                    sriov_network_info['mo']
                )
                continue

            sriov_networks.append(
                sriov_network_info['info']
            )

        return sriov_networks

    def is_sriov_network(self, name, namespace='openshift-sriov-network-operator', cache_enabled=True):
        if self.get_sriov_network(name, namespace=namespace, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_sriov_network(self, name, namespace='openshift-sriov-network-operator', return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        sriov_networks = self.get_sriov_networks(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if sriov_networks is None:
            return None

        if len(sriov_networks) == 1:
            return sriov_networks[0]

        return None

    def get_sriov_networks_with_resource_name(self, resource_name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'resource:%s' % (resource_name)
        )
        sriov_networks = self.get_sriov_networks(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        return sriov_networks
