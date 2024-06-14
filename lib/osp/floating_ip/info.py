from lib import filter_helper
from lib import ip_helper


class OspFloatingIpInfo():
    def __init__(self):
        self.floating_ip = None

    def get_floating_ip_info(self, floating_ip_mo):
        if floating_ip_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'tenant_id',
            'floating_ip_address',
            'floating_network_id',
            'router_id',
            'port_id',
            'fixed_ip_address',
            'status',
            'description',
            'port_details',
            'tags',
            'created_at',
            'updated_at',
            'revision_number',
            'project_id'
        ]
        for key in keys:
            info[key] = floating_ip_mo[key]

        if info['status'] == 'ACTIVE':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        return info

    def get_floating_ips_info(self, cache_enabled=True):
        if cache_enabled:
            if self.floating_ip is not None:
                return self.floating_ip

        managed_objects = self.get_floating_ip_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.floating_ip = []
        for managed_object in managed_objects:
            floating_ip_info = self.get_floating_ip_info(
                managed_object
            )
            self.floating_ip.append(
                floating_ip_info
            )

        self.log.osp_mo(
            'floating_ips',
            self.floating_ip
        )

        return self.floating_ip

    def match_floating_ip(self, floating_ip_info, floating_ip_filter):
        if floating_ip_filter is None or len(floating_ip_filter) == 0:
            return True

        for ap_rule in floating_ip_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'floating-ip':
                key_found = True
                if ip_helper.is_valid_ipv4_cidr(value):
                    if not ip_helper.is_ipv4_in_cidr(floating_ip_info['floating_ip_address'], value):
                        return False

                if ip_helper.is_valid_ipv4_address(value):
                    if not filter_helper.match_string(floating_ip_info['floating_ip_address'], value):
                        return False

            if key == 'fixed-ip':
                key_found = True
                if ip_helper.is_valid_ipv4_cidr(value):
                    if not ip_helper.is_ipv4_in_cidr(floating_ip_info['fixed_ip_address'], value):
                        return False

                if ip_helper.is_valid_ipv4_address(value):
                    if not filter_helper.match_string(floating_ip_info['fixed_ip_address'], value):
                        return False

            if key == 'router':
                key_found = True
                if 'router_name' in floating_ip_info:
                    if not filter_helper.match_string(value, floating_ip_info['router_name']):
                        return False

            if key == 'floating-network':
                key_found = True
                if 'floating_network_name' in floating_ip_info:
                    if not filter_helper.match_string(value, floating_ip_info['floating_network_name']):
                        return False

            if key == 'tenant':
                key_found = True
                if 'tenant_name' in floating_ip_info:
                    if not filter_helper.match_string(value, floating_ip_info['tenant_name']):
                        return False

            if key == 'fixed-network':
                key_found = True
                if 'port_details' in floating_ip_info and floating_ip_info['port_details'] is not None:
                    if 'network_name' in floating_ip_info['port_details']:
                        if not filter_helper.match_string(value, floating_ip_info['port_details']['network_name']):
                            return False

            if key == 'vm':
                key_found = True
                if 'port_details' in floating_ip_info and floating_ip_info['port_details'] is not None:
                    if 'vm_name' in floating_ip_info['port_details']:
                        if not filter_helper.match_tenant_name(value, floating_ip_info['port_details']['vm_name']):
                            return False

            if key == 'mac':
                key_found = True
                if 'port_details' in floating_ip_info and floating_ip_info['port_details'] is not None:
                    if 'mac_address' in floating_ip_info['port_details']:
                        if not ip_helper.is_mac_match(value, floating_ip_info['port_details']['mac_address']):
                            return False

            if not key_found:
                self.log.error(
                    'match_floating_ip',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_floating_ips(self, object_filter=None, tenant_info=False, network_info=False, router_info=False, port_info=False, cache_enabled=True):
        all_floating_ips = self.get_floating_ips_info(cache_enabled=cache_enabled)
        if all_floating_ips is None:
            return None

        floating_ips = []

        for floating_ip_info in all_floating_ips:
            if not self.match_floating_ip(floating_ip_info, object_filter):
                continue

            if tenant_info:
                floating_ip_info['tenant_name'] = self.get_tenant_name(
                    floating_ip_info['tenant_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_floating_ip(floating_ip_info, object_filter):
                    continue

            if network_info:
                floating_ip_info['floating_network_name'] = self.get_network_name(
                    floating_ip_info['floating_network_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_floating_ip(floating_ip_info, object_filter):
                    continue

            if router_info:
                floating_ip_info['router_name'] = self.get_router_name(
                    floating_ip_info['router_id'],
                    cache_enabled=cache_enabled
                )
                if not self.match_floating_ip(floating_ip_info, object_filter):
                    continue

            if port_info:
                if 'port_details' in floating_ip_info and floating_ip_info['port_details'] is not None:
                    floating_ip_info['port_details']['network_name'] = self.get_network_name(
                        floating_ip_info['port_details']['network_id'],
                        cache_enabled=cache_enabled
                    )

                    floating_ip_info['port_details']['vm_name'] = self.get_virtual_machine_tenant_name(
                        floating_ip_info['port_details']['device_id'],
                        cache_enabled=cache_enabled
                    )

                if not self.match_floating_ip(floating_ip_info, object_filter):
                    continue

            floating_ips.append(
                floating_ip_info
            )

        floating_ips = sorted(
            floating_ips,
            key=lambda i: i['floating_ip_address']
        )

        return floating_ips

    def get_floating_ip(self, floating_id=None, floating_ip=None, fixed_ip=None, tenant_info=False, network_info=False, router_info=False, port_info=False, cache_enabled=True):
        object_filter = []

        if floating_id is not None:
            object_filter.append('id:%s' % (floating_id))

        if floating_ip is not None:
            object_filter.append('floating-ip:%s' % (floating_ip))

        if fixed_ip is not None:
            object_filter.append('fixed-ip:%s' % (fixed_ip))

        floating_ips = self.get_floating_ips(
            object_filter=object_filter,
            tenant_info=tenant_info,
            network_info=network_info,
            router_info=router_info,
            port_info=port_info,
            cache_enabled=cache_enabled
        )
        if floating_ips is None or len(floating_ips) != 1:
            return None

        return floating_ips[0]

    def is_floating_ip(self, floating_ip, cache_enabled=True):
        if self.get_floating_ip(floating_ip=floating_ip, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_floating_ip_port(self, floating_id=None, floating_ip=None, fixed_ip=None, cache_enabled=True):
        floating_ip_info = self.get_floating_ip(
            floating_id=floating_id,
            floating_ip=floating_ip,
            fixed_ip=fixed_ip,
            port_info=True,
            cache_enabled=cache_enabled
        )
        if floating_ip_info is None:
            return None

        return floating_ip_info['port_details']

    def get_floating_ip_virtual_machine_name(self, floating_id=None, floating_ip=None, fixed_ip=None, cache_enabled=True):
        floating_ip_port_details = self.get_floating_ip_port_details(
            floating_id=floating_id,
            floating_ip=floating_ip,
            fixed_ip=fixed_ip,
            cache_enabled=cache_enabled
        )
        if floating_ip_port_details is None:
            return None

        return floating_ip_port_details['vm_name']
