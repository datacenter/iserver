from lib import filter_helper


class K8sEndpointInfo():
    def __init__(self):
        self.endpoint = None

    def get_endpoint_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['headless'] = False
        info['headlessTick'] = '\u2717'
        if 'service.kubernetes.io/headless' in info['label']:
            info['headless'] = True
            info['headlessTick'] = '\u2713'

        info['podT'] = []
        info['address'] = []
        info['addressT'] = []
        info['portT'] = []

        subsets_mo = filter_helper.get(managed_object, 'subsets')
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
        infos = self.get_infos(
            'endpoint', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_endpoint(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'endpoint', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
