from lib import filter_helper


class K8sEndpointInfo():
    def __init__(self):
        self.endpoint = None

    def get_endpoint_info(self, endpoint_mo):
        if endpoint_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            endpoint_mo
        )
        info.update(metadata_info)

        info['headless'] = False
        info['headlessTick'] = '\u2717'
        if 'service.kubernetes.io/headless' in info['label']:
            info['headless'] = True
            info['headlessTick'] = '\u2713'

        info['podT'] = []
        info['address'] = []
        info['addressT'] = []
        info['portT'] = []

        subsets_mo = filter_helper.get(endpoint_mo, 'subsets')
        if subsets_mo is not None:
            for subset_mo in subsets_mo:
                addresses_mo = filter_helper.get(subset_mo, 'addresses')
                if addresses_mo is None:
                    continue

                ports_mo = filter_helper.get(subset_mo, 'ports')
                if ports_mo is None:
                    continue

                for address_mo in addresses_mo:
                    if address_mo['ip'] not in info['address']:
                        info['address'].append(
                            address_mo['ip']
                        )

                    info['addressT'].append(
                        '%s [%s]' % (
                            address_mo['ip'], 
                            filter_helper.get(address_mo, 'node_name')
                        )
                    )

                    target_ref = filter_helper.get(address_mo, 'target_ref')
                    if target_ref is not None:
                        if target_ref['kind'] == 'Pod':
                            info['podT'].append(
                                '%s/%s' % (
                                    target_ref['namespace'],
                                    target_ref['name']
                                )
                            )

                    for port_mo in ports_mo:
                        port_value = '%s/%s [%s]' % (
                            port_mo['protocol'],
                            port_mo['port'],
                            filter_helper.get(port_mo, 'name')
                        )

                        if port_value not in info['portT']:
                            info['portT'].append(
                                port_value
                            )

        return info

    def get_endpoints_info(self, cache_enabled=True):
        if cache_enabled:
            if self.endpoint is not None:
                return self.endpoint

        managed_objects = self.get_endpoint_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.endpoint = []
        for managed_object in managed_objects:
            endpoint_info = {}
            endpoint_info['info'] = self.get_endpoint_info(
                managed_object
            )
            endpoint_info['mo'] = managed_object
            self.endpoint.append(
                endpoint_info
            )

        return self.endpoint

    def match_endpoint(self, endpoint_info, endpoint_filter):
        if endpoint_filter is None or len(endpoint_filter) == 0:
            return True

        for ap_rule in endpoint_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, endpoint_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (endpoint_info['namespace'], endpoint_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_endpoint',
                    'Unsupported key: %s' % (key)
                )

        return True

    def check_endpoint_with_label(self, endpoint_info, labels):
        if 'label' not in endpoint_info:
            return False
        
        for label in labels:
            if label not in endpoint_info['label']:
                return False
            
            if endpoint_info['label'][label] != labels[label]:
                return False
            
        return True

    def get_endpoints(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_endpoints = self.get_endpoints_info(cache_enabled=cache_enabled)
        if all_endpoints is None:
            return None

        endpoints = []

        for endpoint_info in all_endpoints:
            if not self.match_endpoint(endpoint_info['info'], object_filter):
                continue

            if return_mo:
                endpoints.append(
                    endpoint_info['mo']
                )
                continue

            endpoints.append(
                endpoint_info['info']
            )

        endpoints = sorted(
            endpoints,
            key=lambda i: (
                i['namespace'],
                i['name']
            )
        )

        return endpoints

    def get_endpoint(self, namespace, name, cache_enabled=True):
        endpoint_filter = []
        endpoint_filter.append('namespace:%s' % (namespace))
        endpoint_filter.append('name:%s' % (name))

        endpoints = self.get_endpoints(
            object_filter=endpoint_filter,
            cache_enabled=cache_enabled
        )

        if endpoints is None or len(endpoints) != 1:
            return None

        return endpoints[0]
