from lib import filter_helper
from lib import ip_helper


class OspPortInfo():
    def __init__(self):
        self.port = None

    def get_port_info(self, port_mo):
        if port_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'network_id',
            'tenant_id',
            'mac_address',
            'admin_state_up',
            'status',
            'device_id',
            'device_owner',
            'fixed_ips',
            'allowed_address_pairs',
            'extra_dhcp_opts',
            'security_groups',
            'port_security_enabled',
            'propagate_uplink_status',
            'tags',
            'created_at',
            'updated_at',
        ]
        for key in keys:
            info[key] = None
            if key in port_mo:
                info[key] = port_mo[key]

        ips = []
        for fixed_ip in info['fixed_ips']:
            ips.append(
                fixed_ip['ip_address']
            )
        info['ips'] = ','.join(ips)

        keys = [
            'binding:vnic_type',
            'binding:profile',
            'binding:host_id',
            'binding:vif_type',
            'binding:vif_details'
        ]
        for key in keys:
            new_key_name = key.replace(':', '_')
            info[new_key_name] = None
            if key in port_mo:
                info[new_key_name] = port_mo[key]

        if info['admin_state_up']:
            info['adminTick'] = '\u2713'
            info['__Output']['adminTick'] = 'Green'
        else:
            info['adminTick'] = '\u2717'
            info['__Output']['adminTick'] = 'Red'

        info['port_security_enabledTick'] = ''
        if info['port_security_enabled']:
            info['port_security_enabledTick'] = '\u2713'

        info['statusT'] = info['status']
        if info['status'] == 'N/A':
            info['statusT'] = '--'
        else:
            if info['statusT'] == 'ACTIVE':
                info['__Output']['statusT'] = 'Green'
            else:
                info['__Output']['statusT'] = 'Red'

        info['type'] = None
        if info['device_owner'] == 'compute:ALL':
            info['type'] = 'Compute'
        if info['device_owner'] == 'network:dhcp':
            info['type'] = 'DHCP'
        if info['device_owner'] == 'network:floatingip':
            info['type'] = 'Floating'
        if info['device_owner'] == 'network:router_gateway':
            info['type'] = 'Gateway'
        if info['device_owner'] == 'network:router_ha_interface':
            info['type'] = 'HA'
        if info['device_owner'] == 'network:ha_router_replicated_interface':
            info['type'] = 'HA'

        if info['type'] is None:
            if len(info['device_owner']) > 0:
                self.log.error(
                    'get_port_info',
                    'Unsupported device owner: %s' % (info['id'])
                )

        info['age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        return info

    def get_ports_info(self, cache_enabled=True):
        if cache_enabled:
            if self.port is not None:
                return self.port

        managed_objects = self.get_port_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'ports',
            managed_objects
        )

        self.port = []
        for managed_object in managed_objects:
            port_info = self.get_port_info(
                managed_object
            )
            self.port.append(
                port_info
            )

        self.log.osp_mo(
            'ports.info',
            self.port
        )

        return self.port

    def match_port(self, port_info, port_filter):
        if port_filter is None or len(port_filter) == 0:
            return True

        for ap_rule in port_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, port_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, port_info['name']):
                    return False

            if key == 'state':
                key_found = True
                if not filter_helper.match_string(value, port_info['status']):
                    return False

            if key == 'type':
                key_found = True
                if not filter_helper.match_string(value, port_info['type']):
                    return False

            if key == 'mac':
                key_found = True
                if not ip_helper.is_mac_match(value, port_info['mac_address']):
                    return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, port_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in port_info:
                    if not filter_helper.match_string(value, port_info['tenant_name']):
                        return False

            if key == 'network_id':
                key_found = True
                if not filter_helper.match_string(value, port_info['network_id']):
                    return False

            if key == 'network_name':
                key_found = True
                if 'network_name' in port_info:
                    if not filter_helper.match_string(value, port_info['network_name']):
                        return False

            if key == 'subnet_id':
                key_found = True
                found = False
                for fixed_ip in port_info['fixed_ips']:
                    if filter_helper.match_string(value, fixed_ip['subnet_id']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'subnet_name':
                key_found = True
                found = False
                subnet_ready = True
                for fixed_ip in port_info['fixed_ips']:
                    if 'subnet_name' not in fixed_ip:
                        subnet_ready = False
                        break

                    if filter_helper.match_string(value, fixed_ip['subnet_name']):
                        found = True
                        break

                if subnet_ready and not found:
                    return False

            if key == 'vm_id':
                key_found = True
                if port_info['device_owner'] != 'compute:ALL':
                    return False
                if not filter_helper.match_string(value, port_info['device_id']):
                    return False

            if key == 'vm_name':
                key_found = True
                if 'vm_tenant_name' in port_info:
                    if not filter_helper.match_tenant_name(value, port_info['vm_tenant_name']):
                        return False

            if key == 'address':
                key_found = True
                if ip_helper.is_valid_ipv4_address(value):
                    found = False
                    for fixed_ip in port_info['fixed_ips']:
                        if filter_helper.match_string(value, fixed_ip['ip_address']):
                            found = True
                            break

                    if not found:
                        return False

                if ip_helper.is_valid_ipv4_cidr(value):
                    found = False
                    for fixed_ip in port_info['fixed_ips']:
                        if ip_helper.is_ipv4_in_cidr(fixed_ip['ip_address'], value):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'hv':
                key_found = True
                if not filter_helper.match_string(value, port_info['binding_host_id']):
                    return False

            if key == 'sg':
                key_found = True
                if 'security_group_names' in port_info:
                    found = False
                    for security_group_name in port_info['security_group_names']:
                        if filter_helper.match_tenant_name(value, security_group_name):
                            found = True
                            break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_port',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ports(self, object_filter=None, tenant_info=False, network_info=False, subnet_info=False, security_info=False, vm_info=False, fip_info=False, cache_enabled=True):
        all_ports = self.get_ports_info(cache_enabled=cache_enabled)
        if all_ports is None:
            return None

        ports = []

        for port_info in all_ports:
            if not self.match_port(port_info, object_filter):
                continue

            if tenant_info:
                port_info['tenant_name'] = None
                if len(port_info['tenant_id']) > 0:
                    port_info['tenant_name'] = self.get_tenant_name(
                        port_info['tenant_id']
                    )

                if not self.match_port(port_info, object_filter):
                    continue

            if network_info:
                port_info['network_name'] = self.get_network_name(
                    port_info['network_id']
                )

                if not self.match_port(port_info, object_filter):
                    continue

            if subnet_info:
                for fixed_ip_mo in port_info['fixed_ips']:
                    fixed_ip_mo['subnet_name'] = self.get_subnet_name(
                        fixed_ip_mo['subnet_id']
                    )

                if not self.match_port(port_info, object_filter):
                    continue

            if security_info:
                port_info['security_group_names'] = []
                for security_group_id in port_info['security_groups']:
                    security_group_name = self.get_security_group_tenant_name(
                        security_group_id,
                        cache_enabled=cache_enabled
                    )
                    if security_group_id is None:
                        self.log.error(
                            'get_ports',
                            'Failed to get security group details: %s' % (security_group_id)
                        )
                    else:
                        port_info['security_group_names'].append(
                            security_group_name
                        )

                port_info['security_group_names_value'] = ','.join(
                    port_info['security_group_names']
                )

            if vm_info:
                port_info['vm_tenant_name'] = None
                if port_info['device_owner'] == 'compute:ALL':
                    port_info['vm_tenant_name'] = self.get_virtual_machine_tenant_name(
                        port_info['device_id']
                    )

                if not self.match_port(port_info, object_filter):
                    continue

            if fip_info:
                port_info['floating_ip'] = None
                floating_filter = []
                floating_filter.append('mac:%s' % (port_info['mac_address']))
                port_floating_ips = self.get_floating_ips(
                    object_filter=floating_filter
                )
                if port_floating_ips is not None and len(port_floating_ips) > 0:
                    if len(port_floating_ips) > 1:
                        self.log.error(
                            'get_ports',
                            'Unexpected fip count for port id: %s' % (port_info['id'])
                        )
                    else:
                        port_info['floating_ip'] = port_floating_ips[0]

                for fixed_ip_mo in port_info['fixed_ips']:
                    fixed_ip_mo['floating_ip'] = None
                    if port_info['floating_ip'] is not None:
                        if port_info['floating_ip']['fixed_ip_address'] == fixed_ip_mo['ip_address']:
                            fixed_ip_mo['floating_ip'] = port_info['floating_ip']['floating_ip_address']

            ports.append(
                port_info
            )

        ports = sorted(
            ports,
            key=lambda i: i['ips']
        )

        return ports
