from lib import filter_helper


class K8sVirtualMachineInstanceInfo():
    def __init__(self):
        self.virtual_machine_instance = None

    def get_virtual_machine_instance_info(self, virtual_machine_instance_mo):
        if virtual_machine_instance_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_instance_mo
        )
        info.update(metadata_info)

        info['cores'] = self.get(virtual_machine_instance_mo, 'spec:domain:cpu:cores')
        info['sockets'] = self.get(virtual_machine_instance_mo, 'spec:domain:cpu:sockets')
        info['threads'] = self.get(virtual_machine_instance_mo, 'spec:domain:cpu:threads')
        info['memory'] = self.get(virtual_machine_instance_mo, 'spec:domain:resources:requests:memory')

        info['node_name'] = self.get(virtual_machine_instance_mo, 'status:nodeName')

        info['phase'] = self.get(virtual_machine_instance_mo, 'status:phase', on_error='Unknown', on_none='Unknown')
        info['phaseT'] = info['phase']
        if info['phaseT'] == 'Succeeded':
            info['phaseT'] = 'Completed'

        if info['phaseT'] in ['Running', 'Completed']:
            info['__Output']['phaseT'] = 'Green'

        if info['phaseT'] in ['Failed', 'Unknown']:
            info['__Output']['phaseT'] = 'Red'

        if info['phaseT'] in ['Pending']:
            info['__Output']['phaseT'] = 'Yellow'

        info['running'] = False
        if info['phase'] == 'Running':
            info['running'] = True

        info['phase_transitions'] = self.get(virtual_machine_instance_mo, 'status:phaseTransitionTimestamps', on_error=[], on_none=[])
        for item in info['phase_transitions']:
            item['timestamp'] = self.convert_timestamp(
                item['phaseTransitionTimestamp']
            )
        info['phase_transitions'] = sorted(
            info['phase_transitions'],
            key=lambda i: i['timestamp']
        )

        info['runtimeUser'] = self.get(virtual_machine_instance_mo, 'status:runtimeUser')

        info['interface'] = self.get(virtual_machine_instance_mo, 'spec:domain:devices:interfaces', on_error=[], on_none=[])
        interfaces_state = self.get(virtual_machine_instance_mo, 'status:interfaces', on_error=[], on_none=[])
        for interface in info['interface']:
            interface['info'] = '--'

            for interface_state in interfaces_state:
                if interface['name'] == interface_state['name']:
                    interface['ip_address'] = self.get(interface_state, 'ipAddress')
                    interface['ip_addresses'] = self.get(interface_state, 'ipAddresses', on_error=[], on_none=[])
                    interface['mac'] = self.get(interface_state, 'mac')

            if interface['name'] == 'default':
                if 'ip_address' in interface and interface['ip_address'] is not None:
                    if 'masquerade' in interface and interface['masquerade'] is not None:
                        interface['info'] = '%s (masq)' % (interface['ip_address'])
                    else:
                        interface['info'] = interface['ip_address']
                continue

            if 'ip_address' in interface and interface['ip_address'] is not None:
                if 'sriov' in interface and interface['sriov'] is not None:
                    interface['info'] = '%s (sriov)' % (interface['ip_address'])
                else:
                    interface['info'] = interface['ip_address']
                continue

            if 'sriov' in interface and interface['sriov'] is not None:
                interface['info'] = '%s (sriov)' % (interface['name'])
            else:
                interface['info'] = interface['name']

        networks_mo = self.get(virtual_machine_instance_mo, 'spec:networks', on_error=[], on_none=[])
        for network_mo in networks_mo:
            for interface_info in info['interface']:
                if network_mo['name'] == interface_info['name']:
                    interface_info['type'] = None
                    if 'sriov' in interface_info:
                        interface_info['type'] = 'sriov'
                    if 'masquerade' in interface_info:
                        interface_info['type'] = 'pod'

                    if interface_info['type'] == 'sriov':
                        sriov_network_info = self.get_sriov_network(network_mo['multus']['networkName'])
                        if sriov_network_info is not None:
                            interface_info['network_name'] = network_mo['multus']['networkName']
                            interface_info['resource_name'] = sriov_network_info['resource_name']
                            interface_info['vlanT'] = sriov_network_info['vlanT']
                            interface_info['ipamT'] = sriov_network_info['ipamT']

        info['disk'] = self.get(virtual_machine_instance_mo, 'spec:domain:devices:disks', on_error=[], on_none=[])

        volumes_spec = self.get(virtual_machine_instance_mo, 'spec:volumes', on_error=[], on_none=[])
        volumes_state = self.get(virtual_machine_instance_mo, 'status:volumeStatus', on_error=[], on_none=[])
        for disk in info['disk']:
            disk['info'] = '--'
            disk['target'] = None
            disk['storage'] = None
            disk['pvc_namespace'] = None
            disk['pvc_name'] = None
            disk['pvc_namespace_name'] = None

            for volume_spec in volumes_spec:
                if disk['name'] == volume_spec['name']:
                    if 'dataVolume' in volume_spec:
                        disk['pvc_namespace'] = info['namespace']
                        disk['pvc_name'] = volume_spec['dataVolume']['name']
                        disk['pvc_namespace_name'] = '%s/%s' % (
                            disk['pvc_namespace'],
                            disk['pvc_name']
                        )

                    if 'persistentVolumeClaim' in volume_spec:
                        disk['pvc_namespace'] = info['namespace']
                        disk['pvc_name'] = volume_spec['persistentVolumeClaim']['claimName']
                        disk['pvc_namespace_name'] = '%s/%s' % (
                            disk['pvc_namespace'],
                            disk['pvc_name']
                        )

            for volume_state in volumes_state:
                if disk['name'] == volume_state['name']:
                    disk['target'] = self.get(volume_state, 'target')
                    if 'persistentVolumeClaimInfo' in volume_state:

                        disk['storage'] = self.get(volume_state, 'persistentVolumeClaimInfo:capacity:storage')
                        disk['info'] = '%s/%s - %s' % (
                            disk['name'],
                            disk['target'],
                            disk['storage']
                        )

        return info

    def get_virtual_machine_instances_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_instance is not None:
                return self.virtual_machine_instance

        managed_objects = self.get_virtual_machine_instance_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_instance = []
        for managed_object in managed_objects:
            virtual_machine_instance_info = {}
            virtual_machine_instance_info['info'] = self.get_virtual_machine_instance_info(
                managed_object
            )
            virtual_machine_instance_info['mo'] = managed_object
            self.virtual_machine_instance.append(
                virtual_machine_instance_info
            )

        return self.virtual_machine_instance

    def match_virtual_machine_instance(self, virtual_machine_instance_info, virtual_machine_instance_filter):
        if virtual_machine_instance_filter is None or len(virtual_machine_instance_filter) == 0:
            return True

        for ap_rule in virtual_machine_instance_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (virtual_machine_instance_info['namespace'], virtual_machine_instance_info['name'])):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_instance_info['namespace']):
                    return False

            if key == 'pvc':
                key_found = True
                found = False
                for disk_info in virtual_machine_instance_info['disk']:
                    if disk_info['pvc_namespace_name'] is not None:
                        if filter_helper.match_namespace_name(value, disk_info['pvc_namespace_name']):
                            found = True
                            break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_instance',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_instances(self, object_filter=None, return_mo=False, vm_info=False, service_info=False, cache_enabled=True):
        all_virtual_machine_instances = self.get_virtual_machine_instances_info(cache_enabled=cache_enabled)
        if all_virtual_machine_instances is None:
            return None

        virtual_machine_instances = []

        for virtual_machine_instance_info in all_virtual_machine_instances:
            if not self.match_virtual_machine_instance(virtual_machine_instance_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_instances.append(
                    virtual_machine_instance_info['mo']
                )
                continue

            if service_info:
                virtual_machine_instance_info['info']['service'] = []
                vmi_services = []
                for label_key in virtual_machine_instance_info['info']['label']:
                    service_filter = [
                        'selector:%s:%s' % (
                            label_key,
                            virtual_machine_instance_info['info']['label'][label_key]
                        )
                    ]
                    services = self.get_services(
                        object_filter=service_filter
                    )
                    if services is not None:
                        for vmi_service_info in services:
                            service_match = True
                            for key in vmi_service_info['selector']:
                                if key not in virtual_machine_instance_info['info']['label']:
                                    service_match = False
                                    break

                                if virtual_machine_instance_info['info']['label'][key] != vmi_service_info['selector'][key]:
                                    service_match = False
                                    break

                            if service_match:
                                if vmi_service_info['namespace_name'] not in vmi_services:
                                    virtual_machine_instance_info['info']['service'].append(
                                        vmi_service_info
                                    )
                                    vmi_services.append(
                                        vmi_service_info['namespace_name']
                                    )

                virtual_machine_instance_info['info']['serviceCount'] = len(
                    virtual_machine_instance_info['info']['service']
                )

            if vm_info:
                if self.is_virtual_machine(virtual_machine_instance_info['info']['namespace'], virtual_machine_instance_info['info']['name'], cache_enabled=cache_enabled):
                    virtual_machine_instance_info['info']['vmTick'] = '\u2713'
                    virtual_machine_instance_info['info']['__Output']['vmTick'] = 'Green'
                else:
                    virtual_machine_instance_info['info']['vmTick'] = '\u2717'
                    virtual_machine_instance_info['info']['__Output']['vmTick'] = 'Red'

            virtual_machine_instances.append(
                virtual_machine_instance_info['info']
            )

        return virtual_machine_instances

    def get_virtual_machine_instance(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append('namespace:%s' % (namespace))
        object_filter.append('name:%s' % (name))
        instances = self.get_virtual_machine_instances(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if instances is None or len(instances) != 1:
            return None
        return instances[0]

    def is_virtual_machine_instance(self, namespace, name, cache_enabled=True):
        if self.get_virtual_machine_instance(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
