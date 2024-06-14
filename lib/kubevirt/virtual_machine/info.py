import time

from lib import filter_helper


class KubevirtVirtualMachineInfo():
    def __init__(self):
        self.virtual_machine = None

    def get_virtual_machine_disk_type(self, disk_mo):
        if disk_mo is None:
            return 'n/a'

        if 'cdrom' in disk_mo and disk_mo['cdrom'] is not None:
            return 'cdrom'

        if 'disk' in disk_mo and disk_mo['disk'] is not None:
            return 'disk'

        if 'lun' in disk_mo and disk_mo['lun'] is not None:
            return 'lun'

        return 'unknown'

    def get_virtual_machine_disk_volume_spec_info(self, volume_spec_mo):
        info = {}
        info['name'] = volume_spec_mo['name']
        info['type'] = 'unknown'
        info['attributes'] = {}
        info['info'] = info['name']

        if 'cloud_init_config_drive' in volume_spec_mo and volume_spec_mo['cloud_init_config_drive'] is not None:
            info['type'] = 'cloudInitConfigDrive'
            for key in volume_spec_mo['cloud_init_config_drive']:
                info['attributes'][key] = volume_spec_mo['cloud_init_config_drive'][key]

            info['info'] = '%s (cloud-init-config-drive)' % (
                info['name']
            )

        if 'cloud_init_no_cloud' in volume_spec_mo and volume_spec_mo['cloud_init_no_cloud'] is not None:
            info['type'] = 'cloudInitNoCloud'
            for key in volume_spec_mo['cloud_init_no_cloud']:
                info['attributes'][key] = volume_spec_mo['cloud_init_no_cloud'][key]

            info['info'] = '%s (cloud-init-no-cloud)' % (
                info['name']
            )

        if 'config_map' in volume_spec_mo and volume_spec_mo['config_map'] is not None:
            info['type'] = 'configMap'
            for key in volume_spec_mo['config_map']:
                info['attributes'][key] = volume_spec_mo['config_map'][key]

            info['info'] = '%s (config-map)' % (
                info['name']
            )

        if 'container_disk' in volume_spec_mo and volume_spec_mo['container_disk'] is not None:
            info['type'] = 'containerDisk'
            for key in volume_spec_mo['container_disk']:
                info['attributes'][key] = volume_spec_mo['container_disk'][key]

            info['info'] = '%s (cont-disk)' % (
                info['name']
            )

        if 'data_volume' in volume_spec_mo and volume_spec_mo['data_volume'] is not None:
            info['type'] = 'dataVolume'
            for key in volume_spec_mo['data_volume']:
                info['attributes'][key] = volume_spec_mo['data_volume'][key]

            info['info'] = '%s - %s (dv)' % (
                info['name'],
                info['attributes']['name']
            )

        if 'empty_disk' in volume_spec_mo and volume_spec_mo['empty_disk'] is not None:
            info['type'] = 'emptyDisk'
            for key in volume_spec_mo['empty_disk']:
                info['attributes'][key] = volume_spec_mo['empty_disk'][key]

            info['info'] = '%s (empty-disk)' % (
                info['name']
            )

        if 'host_disk' in volume_spec_mo and volume_spec_mo['host_disk'] is not None:
            info['type'] = 'hostDisk'
            for key in volume_spec_mo['host_disk']:
                info['attributes'][key] = volume_spec_mo['host_disk'][key]

            info['info'] = '%s (host-disk)' % (
                info['name']
            )

        if 'ephemeral' in volume_spec_mo and volume_spec_mo['ephemeral'] is not None:
            info['type'] = 'ephemeral'
            for key in volume_spec_mo['ephemeral']:
                info['attributes'][key] = volume_spec_mo['ephemeral'][key]

            info['info'] = '%s (ephemeral)' % (
                info['name']
            )

        if 'persistent_volume_claim' in volume_spec_mo and volume_spec_mo['persistent_volume_claim'] is not None:
            info['type'] = 'persistentVolumeClaim'
            for key in volume_spec_mo['persistent_volume_claim']:
                info['attributes'][key] = volume_spec_mo['persistent_volume_claim'][key]

            info['info'] = '%s - %s (pvc)' % (
                info['name'],
                info['attributes']['claim_name']
            )

        if 'secret' in volume_spec_mo and volume_spec_mo['secret'] is not None:
            info['type'] = 'secret'
            for key in volume_spec_mo['secret']:
                info['attributes'][key] = volume_spec_mo['secret'][key]

            info['info'] = '%s (secret)' % (
                info['name']
            )

        return info

    def get_virtual_machine_info(self, virtual_machine_mo):
        if virtual_machine_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['namespace'] = self.get(virtual_machine_mo, 'metadata:namespace')
        info['name'] = self.get(virtual_machine_mo, 'metadata:name')
        info['namespace_name'] = '%s/%s' % (
            info['namespace'],
            info['name']
        )

        info['vm_id'] = self.get(virtual_machine_mo, 'metadata:uid')
        info['special'] = self.get(virtual_machine_mo, 'spec:template:metadata:labels:special')
        info['cpu'] = self.get(virtual_machine_mo, 'spec:template:spec:domain:cpu')
        info['memory'] = self.get(virtual_machine_mo, 'spec:template:spec:domain:resources:requests:memory')
        info['state'] = self.get(virtual_machine_mo, 'status:printable_status')

        info['running'] = False
        info['provisioning'] = False
        info['stopped'] = False
        if info['state'] is not None and info['state'] == 'Running':
            info['running'] = True
        if info['state'] is not None and info['state'] == 'Stopped':
            info['stopped'] = True
        if info['state'] is not None and info['state'] == 'Provisioning':
            info['provisioning'] = True

        info['disks'] = self.get(virtual_machine_mo, 'spec:template:spec:domain:devices:disks')
        info['volumes'] = self.get(virtual_machine_mo, 'spec:template:spec:volumes')

        if info['disks'] is not None:
            for disk_mo in info['disks']:
                disk_mo['info'] = disk_mo['name']
                disk_mo['type'] = self.get_virtual_machine_disk_type(disk_mo)
                disk_mo['bus'] = ''
                if disk_mo['type'] == 'cdrom':
                    disk_mo['bus'] = self.get(disk_mo, 'cdrom:bus')
                if disk_mo['type'] == 'disk':
                    disk_mo['bus'] = self.get(disk_mo, 'disk:bus')
                if info['volumes'] is not None:
                    for volume_mo in info['volumes']:
                        if volume_mo['name'] == disk_mo['name']:
                            disk_mo['volume'] = self.get_virtual_machine_disk_volume_spec_info(volume_mo)

        info['networks'] = self.get(virtual_machine_mo, 'spec:template:spec:networks')
        info['interfaces'] = self.get(virtual_machine_mo, 'spec:template:spec:domain:devices:interfaces')
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

                if interface_info['sriov'] is not None:
                    interface_info['sriovTick'] = '\u2713'
                    interface_info['__Output']['sriovTick'] = 'Green'
                    interface_info['sriovEnabled'] = True

                if interface_info['masquerade'] is not None:
                    interface_info['masqueradeTick'] = '\u2713'
                    interface_info['__Output']['masqueradeTick'] = 'Green'

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        info['liveMigration'] = False
        info['liveMigrationTick'] = '\u2717'
        info['__Output']['liveMigrationTick'] = 'Red'

        info['failures'] = []
        info['failure'] = False
        info['failureTick'] = ''

        conditions = self.get(virtual_machine_mo, 'status:conditions')
        if conditions is not None:
            for condition in conditions:
                if condition['type'] == 'Ready':
                    if condition['status'] == 'True':
                        info['ready'] = True
                        info['readyTick'] = '\u2713'
                        info['__Output']['readyTick'] = 'Green'

                    continue

                if condition['type'] == 'LiveMigratable':
                    if condition['status'] == 'True':
                        info['ready'] = True
                        info['liveMigrationTick'] = '\u2713'
                        info['__Output']['liveMigrationTick'] = 'Green'

                    continue

                if condition['type'] == 'Initialized':
                    continue

                if condition['type'] == 'Paused':
                    continue

                if condition['type'] == 'AgentConnected':
                    continue

                if condition['type'] == 'Provisioning':
                    continue

                if condition['type'] == 'Synchronized':
                    continue

                if condition['type'] == 'PodScheduled':
                    if condition['status'] == 'False':
                        info['failures'].append(
                            condition['reason']
                        )
                        if 'message' in condition and condition['message'] is not None:
                            info['failures'] = info['failures'] + filter_helper.get_string_chunks(
                                filter_helper.sanitize_string(
                                    condition['message']
                                ),
                                30
                            )

                        info['failure'] = True
                        info['failureTick'] = '\u2713'
                        info['__Output']['failureTick'] = 'Red'
                        continue

                if condition['type'] == 'Failure':
                    info['failures'].append(condition)
                    info['failure'] = True
                    info['failureTick'] = '\u2713'
                    info['__Output']['failureTick'] = 'Red'
                    continue

                self.log.error(
                    'get_virtual_machine_info',
                    'Unsupported condition type: %s' % (condition)
                )

        return info

    def get_virtual_machines_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine is not None:
                return self.virtual_machine

        managed_objects = self.get_virtual_machine_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine = []
        virtual_machines_info = []
        for managed_object in managed_objects:
            virtual_machine_info = {}
            virtual_machine_info['info'] = self.get_virtual_machine_info(
                managed_object
            )
            virtual_machines_info.append(
                virtual_machine_info['info']
            )
            virtual_machine_info['mo'] = managed_object
            self.virtual_machine.append(
                virtual_machine_info
            )

        self.log.kubevirt_mo(
            'vm.info',
            virtual_machines_info
        )

        return self.virtual_machine

    def match_virtual_machine(self, virtual_machine_info, virtual_machine_filter):
        if virtual_machine_filter is None or len(virtual_machine_filter) == 0:
            return True

        for ap_rule in virtual_machine_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, virtual_machine_info['namespace_name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, virtual_machine_info['namespace']):
                    return False

            if not key_found:
                self.log.error(
                    'match_virtual_machine',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machines(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machines = self.get_virtual_machines_info(cache_enabled=cache_enabled)
        if all_virtual_machines is None:
            return None

        virtual_machines = []

        for virtual_machine_info in all_virtual_machines:
            if not self.match_virtual_machine(virtual_machine_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machines.append(
                    virtual_machine_info['mo']
                )
                continue

            virtual_machines.append(
                virtual_machine_info['info']
            )

        return virtual_machines

    def get_virtual_machine(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append('namespace:%s' % (namespace))
        object_filter.append('name:%s' % (name))
        instances = self.get_virtual_machines(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if instances is None or len(instances) != 1:
            return None
        return instances[0]

    def get_virtual_machine_state(self, namespace, name, cache_enabled=True):
        virtual_machine_info = self.get_virtual_machine(
            namespace,
            name,
            cache_enabled=cache_enabled
        )
        if virtual_machine_info is not None:
            return virtual_machine_info['state']
        return None

    def is_virtual_machine(self, namespace, name, cache_enabled=True):
        if self.get_virtual_machine(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_virtual_machine_running(self, namespace, name, cache_enabled=True):
        vm_info = self.get_virtual_machine(
            namespace,
            name,
            cache_enabled=cache_enabled
        )
        if vm_info is None:
            return False

        return vm_info['running']

    def wait_virtual_machine_running(self, namespace, vm_name, timeout=600, output_handler=None):
        start_time = int(time.time())
        initial_state = self.get_virtual_machine_state(
            namespace,
            vm_name,
            cache_enabled=False
        )
        if output_handler is not None:
            output_handler.default(
                'Initial virtual machine state: %s' % (
                    initial_state
                )
            )

        while True:
            if self.is_virtual_machine_running(namespace, vm_name, cache_enabled=False):
                return True

            if int(time.time()) - start_time > timeout:
                return False

            time.sleep(5)

            if output_handler is not None:
                current_state = self.get_virtual_machine_state(
                    namespace,
                    vm_name,
                    cache_enabled=False
                )
                if initial_state != current_state:
                    initial_state = current_state
                    output_handler.default(
                        'New virtual machine state: %s' % (
                            initial_state
                        )
                    )

                    if initial_state == 'ErrorUnschedulable':
                        return False

    def is_virtual_machine_stopped(self, namespace, name, cache_enabled=True):
        vm_info = self.get_virtual_machine(
            namespace,
            name,
            cache_enabled=cache_enabled
        )
        if vm_info is None:
            return False

        return vm_info['stopped']

    def is_virtual_machine_provisioning(self, namespace, name, cache_enabled=True):
        vm_info = self.get_virtual_machine(
            namespace,
            name,
            cache_enabled=cache_enabled
        )
        if vm_info is None:
            return False

        return vm_info['provisioning']

    def wait_virtual_machine_stopped(self, namespace, vm_name, timeout=300):
        start_time = int(time.time())
        while True:
            if self.is_virtual_machine_provisioning(namespace, vm_name, cache_enabled=False):
                return True

            if self.is_virtual_machine_stopped(namespace, vm_name, cache_enabled=False):
                return True

            if int(time.time()) - start_time > timeout:
                return False

            time.sleep(5)
