from lib import filter_helper


class KubevirtVirtualMachineInstanceInfo():
    def __init__(self):
        self.virtual_machine_instance = None

    def get_virtual_machine_instance_info(self, virtual_machine_instance_mo):
        if virtual_machine_instance_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['namespace'] = self.get(virtual_machine_instance_mo, 'metadata:namespace')
        info['name'] = self.get(virtual_machine_instance_mo, 'metadata:name')
        info['namespace_name'] = '%s/%s' % (
            info['namespace'],
            info['name']
        )

        info['vmi_id'] = self.get(virtual_machine_instance_mo, 'metadata:uid')
        info['cpu'] = self.get(virtual_machine_instance_mo, 'spec:domain:cpu')
        info['node_name'] = self.get(virtual_machine_instance_mo, 'status:node_name')
        info['guest_os_info'] = self.get(virtual_machine_instance_mo, 'status:guest_os_info')
        info['state_transitions'] = self.get(virtual_machine_instance_mo, 'status:phase_transition_timestamps')

        info['volume_spec'] = []
        volume_specs = self.get(virtual_machine_instance_mo, 'spec:volumes')
        if volume_specs is not None:
            for volume_spec in volume_specs:
                info['volume_spec'].append(
                    self.get_virtual_machine_disk_volume_spec_info(
                        volume_spec
                    )
                )

        info['volume_status'] = self.get(virtual_machine_instance_mo, 'status:volume_status')
        if info['volume_status'] is not None:
            for volume_status_mo in info['volume_status']:
                volume_status_mo['storage'] = self.get(volume_status_mo, 'persistent_volume_claim_info:capacity:storage')

                volume_status_mo['info'] = volume_status_mo['name']
                for volume_spec in info['volume_spec']:
                    if volume_spec['name'] == volume_status_mo['name']:
                        volume_status_mo['info'] = volume_spec['info']

        info['networks'] = self.get(virtual_machine_instance_mo, 'spec:networks')
        info['interface_spec'] = self.get(virtual_machine_instance_mo, 'spec:domain:devices:interfaces')
        info['interfaces'] = self.get(virtual_machine_instance_mo, 'status:interfaces')
        if info['interfaces'] is not None:
            for interface_info in info['interfaces']:
                interface_info['__Output'] = {}
                interface_info['podTick'] = ''
                interface_info['multusTick'] = ''
                interface_info['multusNetworkName'] = ''
                interface_info['sriovEnabled'] = False
                interface_info['sriovTick'] = ''
                interface_info['masqueradeTick'] = ''

                if info['networks'] is not None:
                    for network_info in info['networks']:
                        if interface_info['name'] == network_info['name']:
                            if 'multus' in network_info and network_info['multus'] is not None:
                                interface_info['multusTick'] = '\u2713'
                                interface_info['__Output']['multusTick'] = 'Green'
                                if network_info['multus']['network_name'] is not None:
                                    interface_info['multusNetworkName'] = network_info['multus']['network_name']

                            if 'multus' not in network_info or network_info['multus'] is None:
                                if network_info['pod'] is not None:
                                    interface_info['podTick'] = '\u2713'
                                    interface_info['__Output']['podTick'] = 'Green'

                for interface_spec in info['interface_spec']:
                    if interface_spec['name'] == interface_info['name']:
                        if interface_spec['sriov'] is not None:
                            interface_info['sriovTick'] = '\u2713'
                            interface_info['__Output']['sriovTick'] = 'Green'
                            interface_info['sriovEnabled'] = True

                        if interface_spec['masquerade'] is not None:
                            interface_info['masqueradeTick'] = '\u2713'
                            interface_info['__Output']['masqueradeTick'] = 'Green'

        info['age'] = '--'
        for step in info['state_transitions']:
            if step['phase'] == 'Running':
                info['age'] = self.convert_timestamp_to_age(
                    step['phase_transition_timestamp']
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
        virtual_machine_instances = []
        for managed_object in managed_objects:
            virtual_machine_instance_info = {}
            virtual_machine_instance_info['info'] = self.get_virtual_machine_instance_info(
                managed_object
            )
            virtual_machine_instances.append(
                virtual_machine_instance_info['info']
            )
            virtual_machine_instance_info['mo'] = managed_object
            self.virtual_machine_instance.append(
                virtual_machine_instance_info
            )

        self.log.kubevirt_mo(
            'vmi.info',
            virtual_machine_instances
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
                if not filter_helper.match_tenant_name(value, virtual_machine_instance_info['namespace_name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_instance_info['namespace']):
                    return False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_instance',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_instances(self, object_filter=None, return_mo=False, cache_enabled=True):
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
