from lib import filter_helper
from lib import ip_helper


class OspSubnetInfo():
    def __init__(self):
        self.subnet = None

    def get_subnet_info(self, subnet_mo):
        if subnet_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'tenant_id',
            'network_id',
            'ip_version',
            'subnetpool_id',
            'enable_dhcp',
            'ipv6_ra_mode',
            'ipv6_address_mode',
            'gateway_ip',
            'cidr',
            'allocation_pools',
            'host_routes',
            'dns_nameservers',
            'created_at',
            'updated_at'
        ]
        for key in keys:
            info[key] = None
            if key in subnet_mo:
                info[key] = subnet_mo[key]

        if info['enable_dhcp']:
            info['dhcpTick'] = '\u2713'
        else:
            info['dhcpTick'] = '\u2717'

        info['created_age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        info['updated_age'] = self.convert_timestamp_to_age(
            info['updated_at'],
            on_error='--'
        )

        return info

    def get_subnets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.subnet is not None:
                return self.subnet

        managed_objects = self.get_subnet_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'subnets',
            managed_objects
        )

        self.subnet = []
        for managed_object in managed_objects:
            subnet_info = self.get_subnet_info(
                managed_object
            )
            self.subnet.append(
                subnet_info
            )

        self.log.osp_mo(
            'subnets.info',
            self.subnet
        )

        return self.subnet

    def match_subnet(self, subnet_info, subnet_filter):
        if subnet_filter is None or len(subnet_filter) == 0:
            return True

        for ap_rule in subnet_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, subnet_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, subnet_info['name']):
                    return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, subnet_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in subnet_info:
                    if not filter_helper.match_string(value, subnet_info['tenant_name']):
                        return False

            if key == 'network_id':
                key_found = True
                if not filter_helper.match_string(value, subnet_info['network_id']):
                    return False

            if key == 'network_name':
                key_found = True
                if 'network_name' in subnet_info:
                    if not filter_helper.match_string(value, subnet_info['network_name']):
                        return False

            if key == 'address':
                key_found = True
                if not ip_helper.is_ipv4_in_cidr(value, subnet_info['cidr']):
                    return False

            if key == 'mac':
                key_found = True
                if 'port_info' in subnet_info:
                    found = False
                    for port_info in subnet_info['port_info']:
                        if ip_helper.is_mac_match(value, port_info['mac_address']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'vm_name':
                key_found = True
                if 'port_info' in subnet_info:
                    found = False
                    for port_info in subnet_info['port_info']:
                        if filter_helper.match_tenant_name(value, port_info['vm_tenant_name']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'hv':
                key_found = True
                if 'port_info' in subnet_info:
                    found = False
                    for port_info in subnet_info['port_info']:
                        if port_info['binding_host_id'] is not None:
                            if filter_helper.match_string(value, port_info['binding_host_id']):
                                found = True
                                break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_subnet',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_subnets(self, object_filter=None, tenant_info=False, network_info=False, port_info=False, cache_enabled=True):
        all_subnets = self.get_subnets_info(cache_enabled=cache_enabled)
        if all_subnets is None:
            return None

        subnets = []

        for subnet_info in all_subnets:
            if not self.match_subnet(subnet_info, object_filter):
                continue

            if tenant_info:
                subnet_info['tenant_name'] = self.get_tenant_name(
                    subnet_info['tenant_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_subnet(subnet_info, object_filter):
                    continue

            if network_info:
                subnet_info['network_name'] = self.get_network_name(
                    subnet_info['network_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_subnet(subnet_info, object_filter):
                    continue

            if port_info:
                network_port_filter = []
                network_port_filter.append(
                    'subnet_id:%s' % (subnet_info['id'])
                )
                subnet_info['port_info'] = self.get_ports(
                    object_filter=network_port_filter,
                    vm_info=True
                )

                if not self.match_subnet(subnet_info, object_filter):
                    continue

            subnets.append(
                subnet_info
            )

        return subnets

    def get_subnet(self, subnet_id=None, subnet_name=None, network_info=False, tenant_info=False, port_info=False, cache_enabled=True):
        object_filter = []
        if subnet_id is not None:
            object_filter.append(
                'id:%s' % (subnet_id)
            )
        if subnet_name is not None:
            object_filter.append(
                'name:%s' % (subnet_name)
            )

        subnets = self.get_subnets(
            object_filter=object_filter,
            tenant_info=tenant_info,
            network_info=network_info,
            port_info=port_info
        )
        if subnets is None or len(subnets) != 1:
            return None

        return subnets[0]

    def get_subnet_name(self, subnet_id, cache_enabled=True):
        subnet_info = self.get_subnet(
            subnet_id=subnet_id,
            cache_enabled=cache_enabled
        )
        if subnet_info is None:
            return None
        return subnet_info['name']

    def get_subnet_network_name(self, subnet_id, cache_enabled=True):
        subnet_info = self.get_subnet(
            subnet_id=subnet_id,
            network_info=True,
            cache_enabled=cache_enabled
        )
        if subnet_info is None:
            return None
        return subnet_info['network_name']

    def is_subnet_name(self, subnet_name, cache_enabled=True):
        subnet_info = self.get_subnet(
            subnet_name=subnet_name,
            cache_enabled=cache_enabled
        )
        if subnet_info is None:
            return False
        return True
