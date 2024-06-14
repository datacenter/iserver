from lib import filter_helper
from lib import ip_helper


class OspVirtualMachineInfo():
    def __init__(self):
        self.virtual_machine = None

    def get_virtual_machines_properties(self, managed_objects):
        properties = []
        for managed_object in managed_objects:
            properties.append(
                managed_object.to_dict()
            )
        return properties

    def get_virtual_machine_info(self, virtual_machine_mo):
        if virtual_machine_mo is None:
            return None

        info = virtual_machine_mo.to_dict()
        info['__Output'] = {}

        if info['status'] == 'ACTIVE':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        if isinstance(info['image'], str):
            info['bootFrom'] = 'Volume'
        else:
            info['bootFrom'] = 'Image'

        info['power_state'] = None
        if info['OS-EXT-STS:power_state'] == 0:
            info['power_state'] = 'powered-down'
        if info['OS-EXT-STS:power_state'] == 1:
            info['power_state'] = 'powered-up'
        if info['OS-EXT-STS:power_state'] == 4:
            info['power_state'] = 'shutdown'

        info['task_state'] = info['OS-EXT-STS:task_state']

        info['hypervisor'] = info['OS-EXT-SRV-ATTR:hypervisor_hostname']

        info['interface'] = []
        if info['addresses'] is not None:
            for network_name in info['addresses']:
                for ip_network_info in info['addresses'][network_name]:
                    interface_info = {}
                    interface_info['network'] = network_name
                    interface_info['ip'] = ip_network_info['addr']
                    interface_info['type'] = ip_network_info['OS-EXT-IPS:type']
                    interface_info['ip_type'] = '%s (%s)' % (
                        interface_info['ip'],
                        interface_info['type']
                    )
                    interface_info['mac'] = ip_network_info['OS-EXT-IPS-MAC:mac_addr']
                    interface_info['network_ip'] = '%s=%s' % (
                        interface_info['network'],
                        interface_info['ip']
                    )
                    info['interface'].append(interface_info)

        info['age'] = self.convert_timestamp_to_age(
            info['created'],
            on_error='--'
        )

        return info

    def get_virtual_machines_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine is not None:
                return self.virtual_machine

        managed_objects = self.get_virtual_machine_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'virtual_machines',
            self.get_virtual_machines_properties(managed_objects)
        )

        self.virtual_machine = []
        for managed_object in managed_objects:
            virtual_machine_info = self.get_virtual_machine_info(
                managed_object
            )
            self.virtual_machine.append(
                virtual_machine_info
            )

        self.log.osp_mo(
            'virtual_machines.info',
            self.virtual_machine
        )

        return self.virtual_machine

    def match_virtual_machine(self, virtual_machine_info, virtual_machine_filter):
        if virtual_machine_filter is None or len(virtual_machine_filter) == 0:
            return True

        for ap_rule in virtual_machine_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['name']):
                    return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in virtual_machine_info:
                    if not filter_helper.match_string(value, virtual_machine_info['tenant_name']):
                        return False

            if key == 'image_id':
                key_found = True
                if not isinstance(virtual_machine_info['image'], dict):
                    return False

                if not filter_helper.match_string(value, virtual_machine_info['image']['id']):
                    return False

            if key == 'image_name':
                key_found = True
                if 'image_info' in virtual_machine_info:
                    if virtual_machine_info['image_info'] is None:
                        return False

                    if not filter_helper.match_string(value, virtual_machine_info['image_info']['name']):
                        return False

            if key == 'flavor_id':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['flavor']['id']):
                    return False

            if key == 'flavor_name':
                key_found = True
                if 'flavor_info' in virtual_machine_info:
                    if not filter_helper.match_string(value, virtual_machine_info['flavor_info']['name']):
                        return False

            if key == 'network_id':
                key_found = True
                found = False
                for interface_info in virtual_machine_info['interface']:
                    if filter_helper.match_string(value, interface_info['id']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'network_name':
                key_found = True
                found = False
                for interface_info in virtual_machine_info['interface']:
                    if filter_helper.match_string(value, interface_info['network']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'address':
                key_found = True
                found = False
                for interface_info in virtual_machine_info['interface']:
                    if ip_helper.is_valid_ipv4_address(value):
                        if filter_helper.match_string(value, interface_info['ip']):
                            found = True
                            break

                    if ip_helper.is_valid_ipv4_cidr(value):
                        if ip_helper.is_ipv4_in_cidr(interface_info['ip'], value):
                            found = True
                            break

                if not found:
                    return False

            if key == 'mac':
                key_found = True
                found = False
                for interface_info in virtual_machine_info['interface']:
                    if ip_helper.is_mac_match(value, interface_info['mac']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'hypervisor':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['hypervisor']):
                    return False

            if key == 'port_id':
                key_found = True
                found = False
                port_ready = True
                for interface_info in virtual_machine_info['interface']:
                    if 'port_info' not in interface_info:
                        port_ready = False
                        break

                    if interface_info['port_info'] is not None:
                        if filter_helper.match_string(value, interface_info['port_info']['id']):
                            found = True
                            break

                if port_ready and not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_virtual_machine',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machines(
            self,
            object_filter=None,
            flavor_info=False,
            tenant_info=False,
            image_info=False,
            volume_info=False,
            network_info=False,
            subnet_info=False,
            port_info=False,
            security_info=False,
            console_info=False,
            logs_info=False,
            cache_enabled=True
        ):
        all_virtual_machines = self.get_virtual_machines_info(cache_enabled=cache_enabled)
        if all_virtual_machines is None:
            return None

        virtual_machines = []

        for virtual_machine_info in all_virtual_machines:
            if not self.match_virtual_machine(virtual_machine_info, object_filter):
                continue

            if tenant_info:
                virtual_machine_info['tenant_name'] = None
                tenant_info = self.get_tenant(
                    tenant_id=virtual_machine_info['tenant_id']
                )
                if tenant_info is not None:
                    virtual_machine_info['tenant_name'] = tenant_info['name']

                if not self.match_virtual_machine(virtual_machine_info, object_filter):
                    continue

            if flavor_info:
                virtual_machine_info['flavor_info'] = self.get_flavor(
                    flavor_id=virtual_machine_info['flavor']['id']
                )
                if virtual_machine_info['flavor_info'] is None:
                    self.log.error(
                        'get_virtual_machines',
                        'Flavor info not found: %s' % (virtual_machine_info['id'])
                    )

                if not self.match_virtual_machine(virtual_machine_info, object_filter):
                    continue

            if volume_info:
                virtual_machine_info['volumes'] = []
                if 'os-extended-volumes:volumes_attached' in virtual_machine_info:
                    for volume_ref in virtual_machine_info['os-extended-volumes:volumes_attached']:
                        volume_info = self.get_volume(volume_id=volume_ref['id'])
                        if volume_info is None:
                            self.log.error(
                                'get_virtual_machines',
                                'VM %s volume %s info failed' % (
                                    virtual_machine_info['id'],
                                    volume_ref['id']
                                )
                            )
                        else:
                            virtual_machine_info['volumes'].append(
                                volume_info
                            )

            if image_info:
                virtual_machine_info['image_info'] = None
                if virtual_machine_info['bootFrom'] == 'Image':
                    virtual_machine_info['image_info'] = self.get_image(
                        image_id=virtual_machine_info['image']['id']
                    )
                    virtual_machine_info['bootSource'] = None
                    if virtual_machine_info['image_info'] is not None:
                        virtual_machine_info['bootSource'] = virtual_machine_info['image_info']['name']
                        virtual_machine_info['bootSourceT'] = '(img) %s' % (virtual_machine_info['bootSource'])

                if virtual_machine_info['bootFrom'] == 'Volume':
                    virtual_machine_info['bootSource'] = None
                    if volume_info:
                        if len(virtual_machine_info['volumes']) > 0:
                            virtual_machine_info['bootSource'] = virtual_machine_info['volumes'][0]['name']
                            virtual_machine_info['bootSourceT'] = '(vol) %s' % (virtual_machine_info['bootSource'])

                if not self.match_virtual_machine(virtual_machine_info, object_filter):
                    continue

            if network_info:
                for interface_info in virtual_machine_info['interface']:
                    interface_info['network_info'] = self.get_network(
                        network_name=interface_info['network'],
                        subnet_info=subnet_info
                    )
                    if subnet_info:
                        if interface_info['network_info'] is not None:
                            for interface_subnet_info in interface_info['network_info']['subnet_info']:
                                if ip_helper.is_ipv4_in_cidr(interface_info['ip'], interface_subnet_info['cidr']):
                                    interface_info['subnet'] = interface_subnet_info['cidr']

            if port_info:
                for interface_info in virtual_machine_info['interface']:
                    interface_info['port_info'] = None

                    port_object_filter = []
                    port_object_filter.append(
                        'mac:%s' % (interface_info['mac'])
                    )
                    port_object_filter.append(
                        'vm_id:%s' % (virtual_machine_info['id'])
                    )
                    port_infos = self.get_ports(
                        object_filter=port_object_filter,
                        security_info=security_info
                    )
                    if port_infos is None or len(port_infos) == 0:
                        self.log.error(
                            'get_virtual_machines',
                            'Failed to find port by mac %s for virtual machine %s' % (interface_info['mac'], virtual_machine_info['id'])
                        )

                    if port_infos is not None and len(port_infos) > 1:
                        self.log.error(
                            'get_virtual_machines',
                            'Multiple ports found for mac %s and virtual machine %s' % (interface_info['mac'], virtual_machine_info['id'])
                        )

                    if port_infos is not None and len(port_infos) == 1:
                        interface_info['port_info'] = port_infos[0]

                if not self.match_virtual_machine(virtual_machine_info, object_filter):
                    continue

            if console_info:
                virtual_machine_info['console'] = self.get_virtual_machine_console(
                    virtual_machine_info['id']
                )

            if logs_info:
                virtual_machine_info['logs'] = str(
                    self.get_virtual_machine_logs(
                        virtual_machine_info['id']
                    )
                )

            virtual_machines.append(
                virtual_machine_info
            )

        if tenant_info:
            virtual_machines = sorted(
                virtual_machines,
                key=lambda i: (
                    i['tenant_name'].lower(),
                    i['name'].lower()
                )
            )
        else:
            virtual_machines = sorted(
                virtual_machines,
                key=lambda i: i['name'].lower()
            )

        self.log.osp_mo(
            'virtual_machines.extended',
            virtual_machines
        )

        return virtual_machines

    def get_virtual_machine(self, virtual_machine_id, flavor_info=False, tenant_info=False, image_info=False, volume_info=False, network_info=False, subnet_info=False, cache_enabled=True):
        virtual_machines = self.get_virtual_machines(
            object_filter=[
                'id:%s' % (virtual_machine_id)
            ],
            tenant_info=tenant_info,
            flavor_info=flavor_info,
            image_info=image_info,
            volume_info=volume_info,
            network_info=network_info,
            subnet_info=subnet_info,
            cache_enabled=cache_enabled
        )
        if virtual_machines is None or len(virtual_machines) != 1:
            return None
        return virtual_machines[0]

    def get_virtual_machine_tenant_name(self, virtual_machine_id, cache_enabled=True):
        vm_info = self.get_virtual_machine(
            virtual_machine_id=virtual_machine_id,
            tenant_info=True,
            cache_enabled=cache_enabled
        )
        if vm_info is None:
            return None

        tenant_name = '%s/%s' % (
            vm_info['tenant_name'],
            vm_info['name']
        )
        return tenant_name

    def is_virtual_machine_up(self, virtual_machine_id, cache_enabled=True):
        virtual_machine_info = self.get_virtual_machine(virtual_machine_id, cache_enabled=cache_enabled)
        if virtual_machine_info is None:
            self.log.error(
                'is_virtual_machine_up',
                'Virtual machine not found: %s' % (virtual_machine_id)
            )
            return False

        if virtual_machine_info['status'] == 'SHUTOFF':
            return False

        return True

    def is_virtual_machine(self, virtual_machine_id, cache_enabled=True):
        virtual_machine_info = self.get_virtual_machine(virtual_machine_id, cache_enabled=cache_enabled)
        if virtual_machine_info is None:
            return False
        return True

    def get_virtual_machine_by_name(self, virtual_machine_name, tenant_id=None, tenant_name=None, flavor_info=False, tenant_info=False, image_info=False, volume_info=False, network_info=False, subnet_info=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (virtual_machine_name)
        )
        if tenant_id is not None:
            object_filter.append(
                'tenant_id:%s' % (tenant_id)
            )
        if tenant_name is not None:
            object_filter.append(
                'tenant_name:%s' % (tenant_name)
            )

        virtual_machines = self.get_virtual_machines(
            object_filter=object_filter,
            tenant_info=tenant_info,
            flavor_info=flavor_info,
            image_info=image_info,
            volume_info=volume_info,
            network_info=network_info,
            subnet_info=subnet_info,
            cache_enabled=cache_enabled
        )
        if virtual_machines is None or len(virtual_machines) != 1:
            return None

        return virtual_machines[0]

    def is_virtual_machine_by_name(self, virtual_machine_name, tenant_id=None, tenant_name=None, cache_enabled=True):
        if self.get_virtual_machine_by_name(virtual_machine_name, tenant_id=tenant_id, tenant_name=tenant_name, cache_enabled=cache_enabled) is None:
            return False
        return True
