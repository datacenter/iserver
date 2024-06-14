import time
import traceback
import requests

# pylint: disable=no-name-in-module
from pyVmomi import vim, vmodl


class VcVirtualMachine():
    def __init__(self):
        self.mo_virtual_machine = None

    def get_host_object_info(self, host_obj):
        info = {}
        info['name'] = host_obj.summary.config.name
        info['ip'] = host_obj.summary.managementServerIp
        info['status'] = host_obj.summary.overallStatus
        info['esxi_version'] = host_obj.summary.config.product.version
        info['server_vendor'] = host_obj.summary.hardware.vendor
        info['server_model'] = host_obj.summary.hardware.model
        info['server_uuid'] = host_obj.summary.hardware.uuid
        info['server_serial'] = None
        for other_identifying_info in host_obj.summary.hardware.otherIdentifyingInfo:
            if other_identifying_info.identifierType.key == 'SerialNumberTag':
                info['server_serial'] = other_identifying_info.identifierValue

        return info

    def get_device_class_name(self, device):
        try:
            class_name = device.__class__.__name__
            return class_name.split('.')[-1]
        except BaseException:
            return None

    def get_cdrom_device_objects(self, vm_obj):
        cdrom_objs = []
        for device in vm_obj.config.hardware.device:
            if self.get_device_class_name(device) == 'VirtualCdrom':
                cdrom_objs.append(device)
        return cdrom_objs

    def get_cdrom_devices(self, devices):
        cdrom_devices = []
        for device in devices:
            if self.get_device_class_name(device) == 'VirtualCdrom':
                cdrom_device = {}
                cdrom_device['label'] = device.deviceInfo.label
                cdrom_device['summary'] = device.deviceInfo.summary
                cdrom_device['backing'] = device.backing.fileName
                cdrom_device['connected'] = device.connectable.connected
                cdrom_device['key'] = device.key
                cdrom_device['controllerKey'] = device.controllerKey
                cdrom_device['unitNumber'] = device.unitNumber
                cdrom_devices.append(cdrom_device)

        return cdrom_devices

    def get_network_devices(self, devices):
        network_devices = []
        for device in devices:
            if self.get_device_class_name(device) == 'VirtualVmxnet3':
                network_device = {}
                network_device['type'] = 'vmxnet3'
                network_device['label'] = device.deviceInfo.label
                network_device['summary'] = device.deviceInfo.summary
                try:
                    network_device['backing'] = device.backing.deviceName
                except BaseException:
                    network_device['backing'] = None

                network_device['connected'] = device.connectable.connected
                network_device['key'] = device.key
                network_device['controllerKey'] = device.controllerKey
                network_device['unitNumber'] = device.unitNumber
                network_device['mac'] = device.macAddress
                network_devices.append(network_device)

        return network_devices

    def get_disk_devices(self, devices):
        disk_devices = []
        for device in devices:
            if self.get_device_class_name(device) == 'VirtualDisk':
                disk_device = {}
                disk_device['label'] = device.deviceInfo.label
                disk_device['summary'] = device.deviceInfo.summary
                disk_device['backing'] = device.backing.fileName
                disk_device['mode'] = device.backing.diskMode
                disk_device['writeThrough'] = device.backing.writeThrough
                disk_device['thinProvisioned'] = device.backing.thinProvisioned
                disk_device['key'] = device.key
                disk_device['controllerKey'] = device.controllerKey
                disk_device['unitNumber'] = device.unitNumber
                disk_device['capacity'] = device.capacityInBytes
                disk_device['capacity_unit'] = self.convert_storage(device.capacityInBytes)
                disk_devices.append(disk_device)

        return disk_devices

    def get_vm_nestedhv(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.log.error(
                'vc.get_vm_nestedhv',
                'virtual machine not found: %s' % (vm_name)
            )
            return False

        vm_config = vm_obj.config
        return vm_config.nestedHVEnabled

    def set_vm_nestedhv(self, vm_name, enabled=True):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.log.error(
                'vc.get_vm_nestedhv',
                'virtual machine not found: %s' % (vm_name)
            )
            return False

        vm_config_spec = vim.vm.ConfigSpec()
        vm_config_spec.nestedHVEnabled = enabled
        task = vm_obj.Reconfigure(vm_config_spec)
        self.wait_for_tasks([task], exception_on_task_failure=True)

        return True

    def get_vm_power_state(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.log.error(
                'vc.get_vm_power_state',
                'virtual machine not found: %s' % (vm_name)
            )
            return False

        vm_runtime = vm_obj.summary.runtime
        return vm_runtime.powerState

    def is_vm_powered_on(self, vm_name):
        power_state = self.get_vm_power_state(vm_name)
        if power_state == 'poweredOn':
            return True
        return False

    def is_vm_powered_off(self, vm_name):
        return not self.is_vm_powered_on(vm_name)

    def is_vm(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            return False
        return True

    def get_vm_config_device_virtual_vmxnet3_info(self, device):
        info = {}
        info['label'] = device.deviceInfo.label
        info['type'] = 'VMXNET 3'
        if isinstance(device.backing, vim.vm.device.VirtualEthernetCard.NetworkBackingInfo):
            info['networkName'] = self.get_network_name(
                device.backing.network
            )

        if isinstance(device.backing, vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo):
            info['networkName'] = self.get_distributed_network_name_by_key(
                device.backing.port.portgroupKey
            )
        info['macAddress'] = device.macAddress
        return info

    def get_vm_config_device_virtual_disk_info(self, device):
        info = {}
        info['label'] = device.deviceInfo.label
        info['backingFilename'] = device.backing.fileName
        info['backingDatastore'] = self.get_datastore_info(
            device.backing.datastore
        )
        info['thin'] = False
        if not isinstance(device.backing, vim.vm.device.VirtualDisk.SparseVer2BackingInfo):
            info['thin'] = device.backing.thinProvisioned
        info['capacity'] = device.capacityInBytes
        info['capacityUnit'] = self.convert_storage(info['capacity'])
        return info

    def get_vm_config_info(self, vm_config):
        # 'alternateGuestName', 'annotation', 'bootOptions', 'changeTrackingEnabled', 'changeVersion', 'consolePreferences', 'contentLibItemInfo', 'cpuAffinity', 'cpuAllocation',
        # 'cpuFeatureMask', 'cpuHotAddEnabled', 'cpuHotRemoveEnabled', 'createDate', 'datastoreUrl', 'defaultPowerOps', 'dynamicProperty', 'dynamicType', 'extraConfig',
        # 'files', 'firmware', 'flags', 'forkConfigInfo', 'ftEncryptionMode', 'ftInfo', 'guestAutoLockEnabled', 'guestFullName', 'guestId', 'guestIntegrityInfo',
        # 'guestMonitoringModeInfo', 'hardware', 'hotPlugMemoryIncrementSize', 'hotPlugMemoryLimit', 'initialOverhead', 'instanceUuid', 'keyId', 'latencySensitivity', 'locationId',
        # 'managedBy', 'maxMksConnections', 'memoryAffinity', 'memoryAllocation', 'memoryHotAddEnabled', 'memoryReservationLockedToMax', 'messageBusTunnelEnabled', 'migrateEncryption',
        # 'modified', 'name', 'nestedHVEnabled', 'networkShaper', 'npivDesiredNodeWwns', 'npivDesiredPortWwns', 'npivNodeWorldWideName', 'npivOnNonRdmDisks', 'npivPortWorldWideName',
        # 'npivTemporaryDisabled', 'npivWorldWideNameType', 'pmem', 'pmemFailoverEnabled', 'repConfig', 'scheduledHardwareUpgradeInfo', 'sevEnabled', 'sgxInfo', 'swapPlacement',
        # 'swapStorageObjectId', 'template', 'tools', 'uuid', 'vAppConfig', 'vAssertsEnabled', 'vFlashCacheReservation', 'vPMCEnabled', 'vcpuConfig', 'version',
        # 'vmOpNotificationToAppEnabled', 'vmStorageObjectId', 'vmxConfigChecksum']
        info = {}
        info['uuid'] = vm_config.uuid
        info['guestFullName'] = vm_config.guestFullName
        info['version'] = vm_config.version
        info['instanceUuid'] = vm_config.instanceUuid
        info['template'] = vm_config.template
        info['guestId'] = vm_config.guestId
        info['annotation'] = vm_config.annotation
        info['template'] = vm_config.template

        info['cpu'] = {}
        info['cpu']['flags'] = ''
        info['cpu']['count'] = vm_config.hardware.numCPU
        info['cpu']['coresPerSocket'] = vm_config.hardware.numCoresPerSocket
        info['cpu']['reservation'] = vm_config.cpuAllocation.reservation
        if info['cpu']['reservation'] > 0:
            info['cpu']['flags'] = '%sR' % (info['cpu']['flags'])
        info['cpu']['limit'] = vm_config.cpuAllocation.limit
        if info['cpu']['limit'] > 0:
            info['cpu']['flags'] = '%sL' % (info['cpu']['flags'])
        info['cpu']['cpuHotAddEnabled'] = vm_config.cpuHotAddEnabled
        info['cpu']['cpuHotRemoveEnabled'] = vm_config.cpuHotRemoveEnabled
        if info['cpu']['cpuHotAddEnabled'] or info['cpu']['cpuHotRemoveEnabled']:
            info['cpu']['flags'] = '%sH' % (info['cpu']['flags'])
        info['cpu']['cpuAffinity'] = vm_config.cpuAffinity
        if info['cpu']['cpuAffinity'] is not None:
            info['cpu']['flags'] = '%sA' % (info['cpu']['flags'])
        info['cpu']['virtualization'] = vm_config.nestedHVEnabled
        if info['cpu']['virtualization']:
            info['cpu']['flags'] = '%sV' % (info['cpu']['flags'])

        info['cpu']['info'] = info['cpu']['count']
        if len(info['cpu']['flags']) > 0:
            info['cpu']['info'] = '%s %s' % (
                info['cpu']['info'],
                info['cpu']['flags']
            )

        info['memory'] = {}
        info['memory']['memory'] = vm_config.hardware.memoryMB * 1024 * 1024
        info['memory']['memoryUnit'] = self.convert_memory(
            info['memory']['memory']
        )
        info['memory']['reservation'] = vm_config.memoryAllocation.reservation
        info['memory']['limit'] = vm_config.memoryAllocation.limit
        info['memory']['memoryHotAddEnabled'] = vm_config.memoryHotAddEnabled
        info['memory']['hotPlugMemoryLimit'] = vm_config.hotPlugMemoryLimit
        info['memory']['hotPlugMemoryIncrementSize'] = vm_config.hotPlugMemoryIncrementSize
        info['memory']['memoryAffinity'] = vm_config.memoryAffinity

        info['nic'] = []
        info['disk'] = []
        for device in vm_config.hardware.device:
            if isinstance(device, vim.vm.device.VirtualVmxnet3):
                info['nic'].append(
                    self.get_vm_config_device_virtual_vmxnet3_info(device)
                )

            if isinstance(device, vim.vm.device.VirtualDisk):
                info['disk'].append(
                    self.get_vm_config_device_virtual_disk_info(device)
                )

        return info

    def get_vm_summary_info(self, vm_object, vm_filter=None):
        info = {}
        info['__Output'] = {}

        vm_config = vm_object['summary'].config

        info['name'] = vm_config.name
        if vm_filter is not None:
            if not self.match_vm(info, vm_filter):
                return None

        info['uuid'] = vm_config.uuid
        info['guestId'] = vm_config.guestId
        info['guestFullName'] = vm_config.guestFullName
        info['annotation'] = vm_config.annotation

        info['template'] = vm_config.template
        info['vmPathName'] = vm_config.vmPathName

        info['cpu'] = vm_config.numCpu
        if vm_config.cpuReservation is None:
            info['cpuReservation'] = None
            info['cpuReservationUnit'] = None
        else:
            info['cpuReservation'] = vm_config.cpuReservation * 1000 * 1000
            info['cpuReservationUnit'] = self.convert_cpu_capacity(
                info['cpuReservation'],
                empty_for_zero=True
            )

        if vm_config.memorySizeMB is None:
            info['memory'] = None
            info['memoryUnit'] = None
        else:
            info['memory'] = vm_config.memorySizeMB * 1024 * 1024
            info['memoryUnit'] = self.convert_memory(
                info['memory']
            )

        if vm_config.memoryReservation is None:
            info['memoryReservation'] = None
            info['memoryReservationUnit'] = None
        else:
            info['memoryReservation'] = vm_config.memoryReservation * 1024 * 1024
            info['memoryReservationUnit'] = self.convert_memory(
                info['memoryReservation'],
                empty_for_zero=True
            )

        info['numEthernetCards'] = vm_config.numEthernetCards
        info['numVirtualDisks'] = vm_config.numVirtualDisks

        vm_runtime = vm_object['summary'].runtime
        info['host'] = self.get_host_name(
            vm_runtime.host
        )
        if vm_filter is not None:
            if not self.match_vm(info, vm_filter):
                return None

        info['connectionState'] = vm_runtime.connectionState
        info['powerState'] = vm_runtime.powerState

        storage = vm_object['summary'].storage
        if storage is None or storage.uncommitted is None and storage.committed is None:
            info['provisionedStorage'] = None
            info['provisionedStorageUnit'] = None
            info['usedStorage'] = None
            info['usedStorageUnit'] = None
            info['usedStoragePct'] = None
        else:
            info['provisionedStorage'] = storage.uncommitted + storage.committed
            info['provisionedStorageUnit'] = self.convert_storage(
                info['provisionedStorage']
            )
            info['usedStorage'] = storage.committed
            info['usedStorageUnit'] = self.convert_storage(
                info['usedStorage']
            )
            usage = info['usedStorage'] * 100 / info['provisionedStorage']
            info['usedStoragePct'] = self.convert_pct(
                usage,
                rounded=0
            )
            if 50 < usage <= 75:
                info['__Output']['usedStoragePct'] = 'Yellow'
            if usage > 75:
                info['__Output']['usedStoragePct'] = 'Red'

        stats = vm_object['summary'].quickStats
        info['cpuUsage'] = stats.overallCpuUsage * 1000 * 1000
        info['cpuUsageUnit'] = self.convert_cpu_capacity(
            info['cpuUsage']
        )

        info['guestMemoryUsage'] = stats.guestMemoryUsage
        info['hostMemoryUsage'] = stats.hostMemoryUsage * 1024 * 1024
        info['hostMemoryUsageUnit'] = self.convert_memory(
            info['hostMemoryUsage']
        )
        info['guestMemoryUsage'] = stats.guestMemoryUsage * 1024 * 1024
        info['guestMemoryUsageUnit'] = self.convert_memory(
            info['guestMemoryUsage']
        )

        if info['memory'] is None:
            info['guestMemoryUsagePct'] = None
        else:
            usage = info['guestMemoryUsage'] * 100 / int(info['memory'])
            info['guestMemoryUsagePct'] = self.convert_pct(
                usage,
                rounded=0
            )
            if 50 < usage <= 75:
                info['__Output']['guestMemoryUsagePct'] = 'Yellow'
            if usage > 75:
                info['__Output']['guestMemoryUsagePct'] = 'Red'

        info['status'] = vm_object['summary'].overallStatus

        color = ':'
        if info['powerState'] == 'poweredOn':
            state = 'P+'
            color = '%sGG' % (color)
        else:
            state = 'P-'
            color = '%sRR' % (color)

        if info['status'] == 'green':
            state = '%s H' % (state)
            color = '%s.G' % (color)
        else:
            state = '%s W' % (state)
            color = '%s.R' % (color)

        info['stateFlag'] = state
        info['__Output']['stateFlag'] = color

        return info

    def get_vm_info(self, vm_object, vm_filter=None):
        info = self.get_vm_summary_info(vm_object, vm_filter=vm_filter)
        if info is None:
            return None

        if 'config' in vm_object:
            config = self.get_vm_config_info(vm_object['config'])
            for key in config:
                info[key] = config[key]

        return info

    def get_vm_objects(self):
        if self.mo_virtual_machine is not None:
            return self.mo_virtual_machine

        if not self.vc_connect():
            return None

        start_time = int(time.time() * 1000)

        content = self.vc_service_instance.RetrieveContent()
        vm_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.VirtualMachine],
            True
        )

        filter_spec = self.get_filter_spec(
            vm_object_view,
            vim.VirtualMachine,
            ['config', 'summary']
        )
        options = vmodl.query.PropertyCollector.RetrieveOptions()
        result = self.vc_service_instance.content.propertyCollector.RetrievePropertiesEx([filter_spec], options)

        self.mo_virtual_machine = []
        while True:
            for oresult in result.objects:
                item = {}
                for prop in oresult.propSet:
                    item[prop.name] = prop.val
                self.mo_virtual_machine.append(item)

            if result.token is None:
                break

            result = self.vc_service_instance.content.propertyCollector.ContinueRetrievePropertiesEx(result.token)

        vm_object_view.Destroy()

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'vim.VirtualMachine',
            True,
            duration
        )

        return self.mo_virtual_machine

    def match_vm(self, vm_info, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        name_filtering = False
        name_match = False
        for vm_rule in vm_filter:
            if vm_rule.startswith('name:'):
                name_filtering = True
                name_value = vm_rule[5:]
                if name_value in vm_info['name']:
                    name_match = True

        if name_filtering and not name_match:
            return False

        for vm_rule in vm_filter:
            if vm_rule.startswith('host:'):
                if 'host' in vm_info:
                    host_value = vm_rule[5:]
                    if host_value not in vm_info['host']:
                        return False

        return True

    def get_vms(self, vm_filter=None):
        vm_objects = self.get_vm_objects()
        if vm_objects is None:
            return None

        start_time = int(time.time() * 1000)

        vms = []
        for vm_object in vm_objects:
            vm_info = self.get_vm_info(vm_object, vm_filter=vm_filter)
            if vm_info is not None:
                vms.append(vm_info)

        vms = sorted(
            vms,
            key=lambda i: i['name'].lower()
        )

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'get_vm_info',
            True,
            duration
        )

        return vms

    def get_vm_object(self, vm_name):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        vm_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.VirtualMachine],
            True
        )

        obj = None
        for vm_obj in vm_object_view.view:
            try:
                if vm_obj.name == vm_name:
                    obj = vm_obj
                    break
            except BaseException:
                pass

        vm_object_view.Destroy()

        return obj

    def get_host_object(self, host_ip):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        hosts_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.HostSystem],
            True
        )

        if len(hosts_object_view.view) == 0:
            self.my_output.error('No available host found')
            return None

        if host_ip is None:
            obj = hosts_object_view.view[0]
            self.my_output.default('Selecting the first available host: %s' % (obj.name))
            return obj

        obj = None
        for host_obj in hosts_object_view.view:
            if host_ip is not None:
                if host_obj.name == host_ip:
                    obj = host_obj
                    break

        hosts_object_view.Destroy()

        if obj is None:
            self.my_output.error('Host %s not found' % (host_ip))
            return None

        return obj

    def is_network_devices_connected(self, vm_name):
        network_devices = self.get_network_devices_info(vm_name)
        if network_devices is None:
            return False

        for network_device in network_devices:
            if not network_device['connected']:
                return False

        return True

    def get_network_device_obj(self, vm_name, device_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            return None

        for dev in vm_obj.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualVmxnet3):
                if dev.deviceInfo.label == device_name:
                    return dev

        return None

    def get_network_devices_info(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            return None

        devices = []

        for dev in vm_obj.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualVmxnet3):
                device_info = {}
                device_info['nic_name'] = dev.deviceInfo.label
                device_info['mac'] = dev.macAddress

                is_connected = False
                if isinstance(dev.connectable.connected, bool) and dev.connectable.connected:
                    is_connected = True
                if isinstance(dev.connectable.connected, str) and dev.connectable.connected == 'True':
                    is_connected = True

                if is_connected:
                    device_info['connected'] = True
                    device_info['network_name'] = dev.backing.port.portgroupKey
                else:
                    device_info['connected'] = False
                    device_info['network_name'] = dev.backing.deviceName

                devices.append(
                    device_info
                )

        return devices

    def get_screen(self, url, username, password, filename, timeout=30):
        try:
            with open(filename, "wb") as file_handler:
                response = requests.get(
                    url,
                    auth=(username, password),
                    verify=False,
                    timeout=timeout
                )
                file_handler.write(response.content)
        except BaseException:
            self.my_output.error('Screen download failed')
            self.my_output.default(traceback.format_exc())


    def get_state(self, vm_name, screen_filename=None):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.my_output.error('Virtual machine not found: %s' % (vm_name))
            return None

        vm_state = {}
        vm_state['name'] = vm_obj.summary.config.name
        # pylint: disable=protected-access
        vm_state['moid'] = vm_obj.summary.vm._moId

        vm_state['screen'] = {}
        vm_state['screen']['url'] = 'https://%s/screen?id=%s' % (
            self.vcenter_ip,
            vm_state['moid']
        )
        vm_state['screen']['username'] = self.vcenter_username
        vm_state['screen']['password'] = self.vcenter_password
        vm_state['screen']['filename'] = screen_filename
        if screen_filename is not None:
            self.get_screen(
                vm_state['screen']['url'],
                vm_state['screen']['username'],
                vm_state['screen']['password'],
                screen_filename
            )

        vm_state['vmPathName'] = vm_obj.summary.config.vmPathName
        vm_state['memorySizeMB'] = vm_obj.summary.config.memorySizeMB
        vm_state['memorySizeUnit'] = self.convert_memory(
            vm_obj.summary.config.memorySizeMB * 1024 * 1024
        )
        vm_state['numCpu'] = vm_obj.summary.config.numCpu
        vm_state['numEthernetCards'] = vm_obj.summary.config.numEthernetCards
        vm_state['numVirtualDisks'] = vm_obj.summary.config.numVirtualDisks
        vm_state['overallStatus'] = vm_obj.summary.overallStatus
        vm_state['connectionState'] = vm_obj.summary.runtime.connectionState
        vm_state['powerState'] = vm_obj.summary.runtime.powerState
        vm_state['bootTime'] = str(vm_obj.summary.runtime.bootTime)
        vm_state['cdrom'] = self.get_cdrom_devices(vm_obj.config.hardware.device)
        vm_state['numCdrom'] = len(vm_state['cdrom'])
        vm_state['disk'] = self.get_disk_devices(vm_obj.config.hardware.device)
        vm_state['network'] = self.get_network_devices(vm_obj.config.hardware.device)
        vm_state['host'] = self.get_host_object_info(vm_obj.summary.runtime.host)

        return vm_state

    def print_network_devices(self, info):
        order = [
            'nic_name',
            'network_name',
            'mac',
            'connected'
        ]

        headers = [
            'Name',
            'Network',
            'MAC Address',
            'Connected'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_vms(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'stateFlag',
            'name',
            'host',
            'cpu.count',
            'cpuUsageUnit',
            'cpuReservationUnit',
            'memoryUnit',
            'guestMemoryUsageUnit',
            'guestMemoryUsagePct',
            'memoryReservationUnit',
            'numEthernetCards',
            'numVirtualDisks',
            'provisionedStorageUnit',
            'usedStorageUnit',
            'usedStoragePct'
        ]

        headers = [
            'SF',
            'Name',
            'Host',
            'CPU',
            'Usage',
            'Rsvd',
            'Memory',
            'Usage',
            '[%]',
            'Rsvd',
            'NIC',
            'Disks',
            'Storage',
            'Usage',
            '[%]'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_vms_net(self, vms):
        order = [
            'stateFlag',
            'name',
            'host',
            'nic.label',
            'nic.type',
            'nic.networkName',
            'nic.macAddress'
        ]

        headers = [
            'SF',
            'Name',
            'Host',
            'Label',
            'Type',
            'Network',
            'MAC'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                vms,
                order,
                ['nic']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_vms_fabric(self, vms):
        order = [
            'stateFlag',
            'name',
            'host',
            'nic.label',
            'nic.type',
            'nic.networkName',
            'nic.macAddress',
            'nic.fabric',
            'nic.port'
        ]

        headers = [
            'SF',
            'Name',
            'Host',
            'Label',
            'Type',
            'Network',
            'MAC',
            'Fabric',
            'Port'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                vms,
                order,
                ['nic']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )
