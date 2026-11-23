# pylint: disable=no-name-in-module
from pyVmomi import vim


class VcVirtualMachineLcm():
    def __init__(self):
        pass

    def create_vm_config_spec(self, vm_definition, devices):
        config = vim.vm.ConfigSpec()
        config.name = vm_definition['name']
        config.numCPUs = int(vm_definition['cpu'])
        config.memoryMB = int(vm_definition['memory'])
        config.guestId = 'otherGuest'

        files = vim.vm.FileInfo()
        files.vmPathName = '[%s]' % (vm_definition['datastore_name'])
        config.files = files

        config.deviceChange = devices

        return config

    def update_network_device(self, vm_name, device_name, target_network):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            return False

        device_obj = self.get_network_device_obj(
            vm_name,
            device_name
        )
        if device_obj is None:
            return False

        nicspec = vim.vm.device.VirtualDeviceSpec()
        nicspec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
        nicspec.device = device_obj
        nicspec.device.key = device_obj.key
        nicspec.device.macAddress = device_obj.macAddress
        nicspec.device.backing = device_obj.backing
        nicspec.device.backing.deviceName = target_network

        connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        connectable.connected = True
        connectable.startConnected = True
        nicspec.device.connectable = connectable

        config_spec = vim.vm.ConfigSpec(deviceChange=[nicspec])
        task = vm_obj.Reconfigure(config_spec)
        self.wait_for_tasks([task], exception_on_task_failure=False)

        self.my_output.info('VM %s network device %s connected to network %s' % (vm_name, device_name, target_network))

        return True

    def create_network_devices(self, vm_definition):
        devices = []

        for network in vm_definition['network']:
            net_obj = self.get_network_object(network['name'])
            if net_obj is None:
                self.my_output.error('Network %s not found' % (network['name']))
                self.print_network_names(
                    title='Available networks'
                )
                return None

            if network['type'] not in ['vmxnet3']:
                self.my_output.error('Unsupported network type: %s' % (network['type']))
                return None

            nicspec = vim.vm.device.VirtualDeviceSpec()
            nicspec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add

            if network['type'] == 'vmxnet3':
                nic_type = vim.vm.device.VirtualVmxnet3()

            nicspec.device = nic_type
            nicspec.device.deviceInfo = vim.Description()
            nicspec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
            nicspec.device.connectable.startConnected = True
            nicspec.device.connectable.allowGuestControl = True

            if self.is_network_distributed(net_obj):
                dv_net_obj = self.get_distributed_network_object(network['name'])
                if dv_net_obj is None:
                    self.my_output.error('DV Network %s not found' % (network['name']))
                    return False

                dswitch_port_connection = vim.dvs.PortConnection(
                    portgroupKey=dv_net_obj['key'],
                    switchUuid=dv_net_obj['config'].distributedVirtualSwitch.uuid
                )

                nicspec.device.backing = vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo()
                nicspec.device.backing.port = dswitch_port_connection
            else:
                nicspec.device.backing = vim.vm.device.VirtualEthernetCard.NetworkBackingInfo()
                nicspec.device.backing.network = net_obj
                nicspec.device.backing.deviceName = net_obj.name

            devices.append(nicspec)

        return devices

    def add_network_devices(self, vm_obj, vm_definition):
        if len(vm_definition['network']) == 0:
            return True

        for network in vm_definition['network']:
            net_obj = self.get_network_object(network['name'])
            if net_obj is None:
                self.my_output.error('Network %s not found' % (network['name']))
                self.print_network_names(
                    title='Available networks'
                )
                return False

            if network['type'] not in ['vmxnet3']:
                self.my_output.error('Unsupported network type: %s' % (network['type']))
                return False

            nicspec = vim.vm.device.VirtualDeviceSpec()
            nicspec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add

            if network['type'] == 'vmxnet3':
                nic_type = vim.vm.device.VirtualVmxnet3()

            nicspec.device = nic_type
            nicspec.device.deviceInfo = vim.Description()
            nicspec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
            nicspec.device.connectable.startConnected = True
            nicspec.device.connectable.allowGuestControl = True

            if self.is_network_distributed(net_obj):
                dv_net_obj = self.get_distributed_network_object(network['name'])
                if dv_net_obj is None:
                    self.my_output.error('DV Network %s not found' % (network['name']))
                    return False

                dswitch_port_connection = vim.dvs.PortConnection(
                    portgroupKey=dv_net_obj.key,
                    switchUuid=dv_net_obj.config.distributedVirtualSwitch.uuid
                )

                nicspec.device.backing = vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo()
                nicspec.device.backing.port = dswitch_port_connection
            else:
                nicspec.device.backing = vim.vm.device.VirtualEthernetCard.NetworkBackingInfo()
                nicspec.device.backing.network = net_obj
                nicspec.device.backing.deviceName = net_obj.name

            config_spec = vim.vm.ConfigSpec(deviceChange=[nicspec])
            task = vm_obj.Reconfigure(config_spec)
            self.wait_for_tasks([task], exception_on_task_failure=False)

            if task.info.state == 'error':
                self.my_output.error('Virtual Machine update with network devices failed')
                self.my_output.default(task.info.error)
                return False

            self.my_output.default('Network device added to virtual machine')

        return True

    def create_cdrom_devices(self, vm_definition):
        devices = []
        if len(vm_definition['cdrom']) == 0:
            return devices

        cdrom_id = 0
        for cdrom in vm_definition['cdrom']:
            cdrom_spec = vim.vm.device.VirtualDeviceSpec()
            cdrom_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
            cdrom_spec.device = vim.vm.device.VirtualCdrom()
            cdrom_spec.device.backing = vim.vm.device.VirtualCdrom.IsoBackingInfo()
            cdrom_spec.device.backing.fileName = '[%s] %s' % (cdrom['datastore_name'], cdrom['iso'])

            connectable = vim.vm.device.VirtualDevice.ConnectInfo()
            connectable.allowGuestControl = True
            connectable.startConnected = True
            cdrom_spec.device.connectable = connectable

            # I have no clue how to programmatically get the IDE controller value...
            # https://stackoverflow.com/questions/33223262/listing-valid-controllerkey-values-with-pyvmomi
            cdrom_spec.device.controllerKey = 200

            devices.append(cdrom_spec)

            cdrom_id = cdrom_id + 1

        return devices

    def add_cdrom_devices(self, vm_obj, controller, vm_definition):
        if len(vm_definition['cdrom']) == 0:
            self.my_output.default('No cdrom device defined')
            return True

        for cdrom in vm_definition['cdrom']:
            cdrom_spec = vim.vm.device.VirtualDeviceSpec()
            cdrom_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
            cdrom_spec.device = vim.vm.device.VirtualCdrom()
            cdrom_spec.device.backing = vim.vm.device.VirtualCdrom.IsoBackingInfo()
            cdrom_spec.device.backing.fileName = '[%s] %s' % (cdrom['datastore_name'], cdrom['iso'])

            connectable = vim.vm.device.VirtualDevice.ConnectInfo()
            connectable.allowGuestControl = True
            connectable.startConnected = True
            cdrom_spec.device.connectable = connectable

            cdrom_spec.device.controllerKey = controller.key

            config_spec = vim.vm.ConfigSpec(deviceChange=[cdrom_spec])
            task = vm_obj.Reconfigure(config_spec)
            self.wait_for_tasks([task], exception_on_task_failure=False)

            if task.info.state == 'error':
                self.my_output.error('Virtual Machine update with cdrom devices failed')
                self.my_output.default(task.info.error)
                return False

            self.my_output.default('Cdrom added to virtual machine')

        return True

    def create_disk_devices(self, vm_definition):
        devices = []

        scsi_ctr = vim.vm.device.VirtualDeviceSpec()
        scsi_ctr.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        scsi_ctr.device = vim.vm.device.ParaVirtualSCSIController()
        scsi_ctr.device.deviceInfo = vim.Description()
        scsi_ctr.device.slotInfo = vim.vm.device.VirtualDevice.PciBusSlotInfo()
        scsi_ctr.device.slotInfo.pciSlotNumber = 16
        scsi_ctr.device.controllerKey = 100
        scsi_ctr.device.unitNumber = 3
        scsi_ctr.device.busNumber = 0
        scsi_ctr.device.hotAddRemove = True
        scsi_ctr.device.sharedBus = 'noSharing'
        scsi_ctr.device.scsiCtlrUnitNumber = 7
        devices.append(scsi_ctr)

        disk_id = 0
        for disk in vm_definition['disk']:
            disk_spec = vim.vm.device.VirtualDeviceSpec()
            disk_spec.fileOperation = "create"
            disk_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
            disk_spec.device = vim.vm.device.VirtualDisk()
            disk_spec.device.backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
            disk_spec.device.backing.diskMode = 'persistent'
            disk_spec.device.backing.fileName = '[%s] %s/%s-disk%s.vmdk' % (
                vm_definition['datastore_name'],
                vm_definition['name'],
                vm_definition['name'],
                disk_id
            )
            disk_spec.device.backing.thinProvisioned = True
            disk_spec.device.unitNumber = disk_id
            disk_spec.device.capacityInKB = disk['size'] * 1024 * 1024
            disk_spec.device.controllerKey = scsi_ctr.device.key
            devices.append(disk_spec)

            disk_id = disk_id + 1

        return devices

    def create_vm(self, vm_definition, dry_run=False):
        if not self.vc_connect():
            self.my_output.error('VM folder not found')
            return False

        devices = []

        new_device = self.create_disk_devices(vm_definition)
        if new_device is None:
            return False

        devices = devices + new_device

        new_device = self.create_network_devices(vm_definition)
        if new_device is None:
            return False

        devices = devices + new_device

        vm_config_spec = self.create_vm_config_spec(vm_definition, devices)

        content = self.vc_service_instance.RetrieveContent()
        vm_folder = None
        for child in content.rootFolder.childEntity:
            if child.name == vm_definition['datacenter_name']:
                vm_folder = child.vmFolder
                break

        if vm_folder is None:
            self.my_output.error('VM folder not found')
            return False

        host_obj = self.get_host_object(vm_definition['host_ip'])
        if host_obj is None:
            return False

        source_pool = host_obj.parent.resourcePool

        if dry_run:
            self.my_output.default(vm_config_spec)
            return True

        task = vm_folder.CreateVm(
            vm_config_spec,
            pool=source_pool,
            host=host_obj
        )
        self.wait_for_tasks([task], exception_on_task_failure=False)

        if task.info.state == 'error':
            self.my_output.error('Virtual Machine create failed')
            self.my_output.default(task.info.error)
            return False

        self.my_output.default('Virtual Machine created: %s' % (vm_definition['name']))

        vm_obj = self.get_vm_object(vm_definition['name'])
        if vm_obj is None:
            self.my_output.error('Virtual Machine not found: %s' % (vm_definition['name']))
            return False

        controller = None
        for dev in vm_obj.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualIDEController):
                # If there are less than 2 devices attached, we can use it.
                if len(dev.device) < 2:
                    controller = dev

        if controller is None:
            self.my_output.error('Virtual IDE controller not found')
            return False

        if not self.add_cdrom_devices(vm_obj, controller, vm_definition):
            return False

        return True

    def power_on_vm(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.my_output.error('Virtual Machine not found: %s' % (vm_name))
            return False

        current_power_state = vm_obj.runtime.powerState
        if current_power_state == 'poweredOn':
            self.my_output.default('Virtual Machine already powered on: %s' % (vm_name))
            return True
        self.my_output.default('The current powerState is: %s' % (current_power_state))

        task = vm_obj.PowerOnVM_Task()
        self.wait_for_tasks([task], exception_on_task_failure=False)

        if task.info.state == 'error':
            self.my_output.error('Virtual Machine power on failed')
            self.my_output.default(task.info.error)
            return False

        self.my_output.default('Virtual Machine powered on: %s' % (vm_name))

        return True

    def power_off_vm(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.my_output.error('Virtual Machine not found: %s' % (vm_name))
            return False

        current_power_state = vm_obj.runtime.powerState
        if current_power_state == 'poweredOff':
            self.my_output.default('Virtual Machine already powered off: %s' % (vm_name))
            return True
        self.my_output.default('The current powerState is: %s' % (current_power_state))

        task = vm_obj.PowerOffVM_Task()
        self.wait_for_tasks([task], exception_on_task_failure=False)

        if task.info.state == 'error':
            self.my_output.error('Virtual Machine power off failed')
            self.my_output.default(task.info.error)
            return False

        self.my_output.default('Virtual Machine powered off: %s' % (vm_name))

        return True

    def destroy_vm(self, vm_name):
        vm_obj = self.get_vm_object(vm_name)
        if vm_obj is None:
            self.my_output.error('Virtual Machine not found: %s' % (vm_name))
            return False

        current_power_state = vm_obj.runtime.powerState
        if current_power_state != 'poweredOff':
            self.my_output.default('Virtual Machine must be powered off: %s' % (vm_name))
            return True
        self.my_output.default('The current powerState is: %s' % (current_power_state))

        task = vm_obj.Destroy_Task()
        self.wait_for_tasks([task], exception_on_task_failure=False)

        if task.info.state == 'error':
            self.my_output.error('Virtual Machine destroy failed')
            self.my_output.default(task.info.error)
            return False

        self.my_output.default('Virtual Machine destroyed: %s' % (vm_name))

        return True

    def delete_vm(self, name):
        if not self.is_vm(name):
            self.my_output.default('Virtual machine does not exist: %s' % (name))
            return True

        if not self.power_off_vm(name):
            return False

        if not self.destroy_vm(name):
            return False

        return True
