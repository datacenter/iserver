from lib import filter_helper
from lib import ip_helper


class OspNetworkInfo():
    def __init__(self):
        self.network = None

    def get_network_info(self, network_mo):
        if network_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'tenant_id',
            'admin_state_up',
            'mtu',
            'status',
            'subnets',
            'shared',
            'availability_zone_hints',
            'availability_zones',
            'ipv4_address_scope',
            'ipv6_address_scope',
            'port_security_enabled',
            'created_at',
            'updated_at'
        ]
        for key in keys:
            info[key] = None
            if key in network_mo:
                info[key] = network_mo[key]

        info['external'] = network_mo['router:external']
        info['provider_network_type'] = network_mo['provider:network_type']
        info['provider_physical_network'] = network_mo['provider:physical_network']
        info['provider_segmentation_id'] = network_mo['provider:segmentation_id']

        if info['status'] == 'ACTIVE':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        if info['admin_state_up']:
            info['adminTick'] = '\u2713'
            info['__Output']['adminTick'] = 'Green'
        else:
            info['adminTick'] = '\u2717'
            info['__Output']['adminTick'] = 'Green'

        if info['external']:
            info['externalTick'] = '\u2713'
        else:
            info['externalTick'] = '\u2717'

        if info['shared']:
            info['sharedTick'] = '\u2713'
        else:
            info['sharedTick'] = '\u2717'

        if info['port_security_enabled']:
            info['securityTick'] = '\u2713'
        else:
            info['securityTick'] = '\u2717'

        info['created_age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        info['updated_age'] = self.convert_timestamp_to_age(
            info['updated_at'],
            on_error='--'
        )

        return info

    def get_networks_info(self, cache_enabled=True):
        if cache_enabled:
            if self.network is not None:
                return self.network

        managed_objects = self.get_network_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'networks',
            managed_objects
        )

        self.network = []
        for managed_object in managed_objects:
            network_info = self.get_network_info(
                managed_object
            )
            self.network.append(
                network_info
            )

        self.log.osp_mo(
            'networks.info',
            self.network
        )

        return self.network

    def match_network(self, network_info, network_filter):
        if network_filter is None or len(network_filter) == 0:
            return True

        for ap_rule in network_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, network_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if len(value.split('/')) == 1:
                    if not filter_helper.match_string(value, network_info['name']):
                        return False
                if len(value.split('/')) == 2:
                    if not filter_helper.match_string(value.split('/')[1], network_info['name']):
                        return False

                    if 'tenant_name' in network_info:
                        if not filter_helper.match_string(value.split('/', maxsplit=1)[0], network_info['tenant_name']):
                            return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, network_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in network_info:
                    if not filter_helper.match_string(value, network_info['tenant_name']):
                        return False

            if key == 'external':
                key_found = True
                if value not in ['true', 'false']:
                    self.log.error(
                        'match_network',
                        'Unsupported external value: %s' % (value)
                    )
                    return False

                if value == 'true' and not network_info['external']:
                    return False

                if value == 'false' and network_info['external']:
                    return False

            if key == 'mac':
                key_found = True
                if 'port_info' in network_info:
                    found = False
                    for port_info in network_info['port_info']:
                        if ip_helper.is_mac_match(value, port_info['mac_address']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'address':
                key_found = True
                if 'subnet_info' in network_info:
                    found = False
                    for subnet_info in network_info['subnet_info']:
                        if ip_helper.is_ipv4_in_cidr(value, subnet_info['cidr']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'vm_name':
                key_found = True
                if 'port_info' in network_info:
                    found = False
                    for port_info in network_info['port_info']:
                        if filter_helper.match_tenant_name(value, port_info['vm_tenant_name']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'hv':
                key_found = True
                if 'port_info' in network_info:
                    found = False
                    for port_info in network_info['port_info']:
                        if port_info['binding_host_id'] is not None:
                            if filter_helper.match_string(value, port_info['binding_host_id']):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'vlan':
                key_found = True
                if network_info['provider_segmentation_id'] is None:
                    return False

                if not filter_helper.match_string(value, str(network_info['provider_segmentation_id'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_network',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_networks(self, object_filter=None, tenant_info=False, subnet_info=False, port_info=False, router_info=False, cache_enabled=True):
        all_networks = self.get_networks_info(cache_enabled=cache_enabled)
        if all_networks is None:
            return None

        networks = []

        for network_info in all_networks:
            if not self.match_network(network_info, object_filter):
                continue

            if tenant_info:
                network_info['tenant_name'] = self.get_tenant_name(
                    network_info['tenant_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_network(network_info, object_filter):
                    continue

            if subnet_info:
                network_info['subnet_info'] = []
                for subnet_id in network_info['subnets']:
                    network_subnet_info = self.get_subnet(subnet_id=subnet_id)
                    if network_subnet_info is None:
                        self.log.error(
                            'get_networks',
                            'Subnet info failed: %s' % (subnet_id)
                        )
                        continue

                    network_info['subnet_info'].append(
                        network_subnet_info
                    )

                if not self.match_network(network_info, object_filter):
                    continue

            if port_info or router_info:
                network_port_filter = []
                network_port_filter.append(
                    'network_id:%s' % (network_info['id'])
                )
                network_info['port_info'] = self.get_ports(
                    object_filter=network_port_filter,
                    vm_info=True
                )

                if not self.match_network(network_info, object_filter):
                    continue

                network_info['router_id'] = None
                network_info['router_tenant_name'] = None
                network_info['router_name'] = None

                routers = self.get_routers(tenant_info=True)
                if routers is not None:
                    for router in routers:
                        for port_info in network_info['port_info']:
                            if port_info['device_id'] == router['id']:
                                network_info['router_id'] = router['id']
                                network_info['router_tenant_name'] = router['tenant_name']
                                network_info['router_name'] = router['name']

            networks.append(
                network_info
            )

        networks = sorted(
            networks,
            key=lambda i: i['name'].lower()
        )

        return networks

    def get_network(self, network_id=None, network_name=None, tenant_info=False, subnet_info=False, port_info=False, cache_enabled=True):
        object_filter = []
        if network_id is not None:
            object_filter.append(
                'id:%s' % (network_id)
            )
        if network_name is not None:
            object_filter.append(
                'name:%s' % (network_name)
            )

        networks = self.get_networks(
            object_filter=object_filter,
            tenant_info=tenant_info,
            subnet_info=subnet_info,
            port_info=port_info,
            cache_enabled=cache_enabled
        )
        if networks is None or len(networks) != 1:
            return None

        return networks[0]

    def get_network_name(self, network_id, cache_enabled=True):
        network_info = self.get_network(
            network_id=network_id,
            cache_enabled=cache_enabled
        )
        if network_info is None:
            return None
        return network_info['name']

    def is_network_name(self, network_name, cache_enabled=True):
        network = self.get_network(network_name=network_name, cache_enabled=cache_enabled)
        if network is None:
            return False
        return True
