import traceback

from lib import info_helper

from lib.intersight import cache as intersight_cache
from lib.intersight import adapter_unit
from lib.intersight import adapter_ext_eth_interface
from lib.intersight import adapter_host_eth_interface
from lib.intersight import adapter_host_fc_interface
from lib.intersight import asset_device_registration
from lib.intersight import asset_device_contract_information
from lib.intersight import bios_boot_mode
from lib.intersight import boot_cdd_device
from lib.intersight import boot_device_boot_mode
from lib.intersight import boot_device_boot_security
from lib.intersight import boot_hdd_device
from lib.intersight import boot_iscsi_device
from lib.intersight import boot_nvme_device
from lib.intersight import boot_pxe_device
from lib.intersight import boot_san_device
from lib.intersight import boot_sd_device
from lib.intersight import boot_uefi_device
from lib.intersight import boot_usb_device
from lib.intersight import boot_vmedia_device
from lib.intersight import cond_alarm
from lib.intersight import cond_hclstatus
from lib.intersight import cond_hclstatus_detail
from lib.intersight import compute_board
from lib.intersight import compute_server_setting
from lib.intersight import equipment_chassis
from lib.intersight import equipment_fan_module
from lib.intersight import equipment_led
from lib.intersight import equipment_psu
from lib.intersight import equipment_tpm
from lib.intersight import memory_unit
from lib.intersight import pci_device
from lib.intersight import processor_unit
from lib.intersight import running_firmware
from lib.intersight import search_item
from lib.intersight import server_profile
from lib.intersight import storage_physical_disk
from lib.intersight import storage_virtual_drive
from lib.intersight import storage_controller
from lib.intersight import tam_advisory_instance
from lib.intersight import tam_security_advisory
from lib.intersight import workflow

from lib.redfish import endpoint_settings as redfish_endpoint_settings
from lib.ucsm import endpoint_settings as ucsm_endpoint_settings
from lib import my_servers_helper
from lib import log_helper


class ComputeExtraAttributes():
    """Class for rack/blade compute object extra attributes
    """
    def __init__(self, iaccount, settings, log_id=None):
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.settings = settings
        self.my_servers_handler = my_servers_helper.MyServers()
        self.my_servers_serials = self.my_servers_handler.get_serials()
        self.info_handler = info_helper.InfoHelper(
            log_id=log_id
        )

        self.cache_handler = intersight_cache.IntersightCache(
            log_id=log_id
        )
        self.cache_enabled = False
        self.state_enabled = True

        self.adapter_ext_eth_interface_handler = adapter_ext_eth_interface.AdapterExtEthInterface(
            iaccount,
            log_id=log_id
        )
        self.adapter_host_eth_interface_handler = adapter_host_eth_interface.AdapterHostEthInterface(
            iaccount,
            log_id=log_id
        )
        self.adapter_host_fc_interface_handler = adapter_host_fc_interface.AdapterHostFcInterface(
            iaccount,
            log_id=log_id
        )
        self.adapter_unit_handler = adapter_unit.AdapterUnit(
            iaccount,
            log_id=log_id
        )
        self.asset_device_contract_information_handler = asset_device_contract_information.AssetDeviceContractInformation(
            iaccount,
            log_id=log_id
        )
        self.asset_device_registration_handler = asset_device_registration.AssetDeviceRegistration(
            iaccount,
            log_id=log_id
        )
        self.bios_boot_mode_handler = bios_boot_mode.BiosBootMode(
            iaccount,
            log_id=log_id
        )
        self.boot_cdd_device_handler = boot_cdd_device.BootCddDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_device_boot_mode_handler = boot_device_boot_mode.BootDeviceBootMode(
            iaccount,
            log_id=log_id
        )
        self.boot_device_boot_security_handler = boot_device_boot_security.BootDeviceBootSecurity(
            iaccount,
            log_id=log_id
        )
        self.boot_hdd_device_handler = boot_hdd_device.BootHddDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_iscsi_device_handler = boot_iscsi_device.BootIscsiDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_nvme_device_handler = boot_nvme_device.BootNvmeDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_pxe_device_handler = boot_pxe_device.BootPxeDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_san_device_handler = boot_san_device.BootSanDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_sd_device_handler = boot_sd_device.BootSdDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_uefi_device_handler = boot_uefi_device.BootUefiDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_usb_device_handler = boot_usb_device.BootUsbDevice(
            iaccount,
            log_id=log_id
        )
        self.boot_vmedia_device_handler = boot_vmedia_device.BootVmediaDevice(
            iaccount,
            log_id=log_id
        )
        self.cond_alarm_handler = cond_alarm.CondAlarm(
            iaccount,
            log_id=log_id
        )
        self.cond_hclstatus_handler = cond_hclstatus.CondHclStatus(
            iaccount,
            log_id=log_id
        )
        self.cond_hclstatus_detail_handler = cond_hclstatus_detail.CondHclStatusDetail(
            iaccount,
            log_id=log_id
        )
        self.compute_board_handler = compute_board.ComputeBoard(
            iaccount,
            log_id=log_id
        )
        self.compute_server_setting_handler = compute_server_setting.ComputeServerSetting(
            iaccount,
            log_id=log_id
        )
        self.equipment_chassis_handler = equipment_chassis.EquipmentChassis(
            iaccount,
            log_id=log_id
        )
        self.equipment_tpm_handler = equipment_tpm.EquipmentTpm(
            iaccount,
            log_id=log_id
        )
        self.fan_handler = equipment_fan_module.EquipmentFanModule(
            iaccount,
            log_id=log_id
        )
        self.locator_handler = equipment_led.EquipmentLed(
            iaccount,
            log_id=log_id
        )
        self.memory_unit_handler = memory_unit.MemoryUnit(
            iaccount,
            log_id=log_id
        )
        self.processor_unit_handler = processor_unit.ProcessorUnit(
            iaccount,
            log_id=log_id
        )
        self.psu_handler = equipment_psu.EquipmentPsu(
            iaccount,
            log_id=log_id
        )
        self.pci_handler = pci_device.PciDevice(
            iaccount,
            log_id=log_id
        )
        running_firmware_filter = '"Component eq \'system\' and Type eq \'blade-controller\'"'
        self.running_firmware_handler = running_firmware.RunningFirmware(
            iaccount,
            get_filter=running_firmware_filter,
            log_id=log_id
        )
        self.search_item_handler = search_item.SearchItem(
            iaccount,
            log_id=log_id
        )
        self.server_profile_handler = server_profile.ServerProfile(
            iaccount,
            log_id=log_id
        )
        self.server_profile_handler.set_get_expand('ConfigChangeDetails')
        self.storage_controller_handler = storage_controller.StorageController(
            iaccount,
            log_id=log_id
        )
        self.storage_physical_disk_handler = storage_physical_disk.StoragePhysicalDisk(
            iaccount,
            log_id=log_id
        )
        self.storage_virtual_drive_handler = storage_virtual_drive.StorageVirtualDrive(
            iaccount,
            log_id=log_id
        )
        self.tam_advisory_instance_handler = tam_advisory_instance.TamAdvisoryInstance(
            iaccount,
            log_id=log_id
        )
        self.tam_security_advisory_handler = tam_security_advisory.TamSecurityAdvisory(
            iaccount,
            log_id=log_id
        )
        self.workflow = workflow.Workflow(
            iaccount,
            log_id=log_id
        )
        self.last_workflows = None

        self.redfish_endpoint_settings_handler = redfish_endpoint_settings.RedfishEndpointSettings(
            log_id=log_id
        )
        self.ucsm_endpoint_settings_handler = ucsm_endpoint_settings.UcsmEndpointSettings(
            log_id=log_id
        )

        self.server_info = {}
        self.chassis = None

    def set_cache(self, key, moids, device_moids, registration_moids, board_moids, filter_length_threshold=20):
        moids_list = []
        for moid in moids:
            moids_list.append('\'%s\'' % (moid))
        moids_filter = ', '.join(moids_list)

        device_moids_list = []
        for device_moid in device_moids:
            device_moids_list.append('\'%s\'' % (device_moid))
        device_moids_filter = ', '.join(device_moids_list)

        registration_moids_list = []
        for registration_moid in registration_moids:
            registration_moids_list.append('\'%s\'' % (registration_moid))
        registration_moids_filter = ', '.join(registration_moids_list)

        board_moids_list = []
        for board_moid in board_moids:
            board_moids_list.append('\'%s\'' % (board_moid))
        board_moids_filter = ', '.join(board_moids_list)

        if key == 'asset_device_registration':
            if self.settings['registration']:
                if len(registration_moids_list) < filter_length_threshold:
                    self.asset_device_registration_handler.set_get_filter(
                        "Moid in (%s)" % (registration_moids_filter)
                    )
                cache = self.asset_device_registration_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'locator_led':
            if self.settings['locator']:
                cache = self.locator_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'workflow':
            if self.settings['workflow'] is not None:
                cache = self.workflow.get_last(
                    seconds=self.settings['workflow']
                )
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'fanmodule':
            if self.settings['fan']:
                if len(moids) < filter_length_threshold:
                    self.fan_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (moids_filter)
                    )
                cache = self.fan_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'pci':
            if self.settings['pci']:
                if len(moids) < filter_length_threshold:
                    self.pci_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (moids_filter)
                    )
                cache = self.pci_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'psu':
            if self.settings['psu']:
                if len(moids) < filter_length_threshold:
                    self.psu_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (moids_filter)
                    )
                cache = self.psu_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'firmware':
            if self.settings['fw']:
                if len(device_moids) < filter_length_threshold:
                    self.running_firmware_handler.set_get_filter(
                        "RegisteredDevice/Moid in (%s)" % (device_moids_filter)
                    )
                cache = self.running_firmware_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'storage_controller':
            if self.settings['storage']:
                if len(board_moids_list) < filter_length_threshold:
                    self.storage_controller_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (board_moids_filter)
                    )
                cache = self.storage_controller_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'virtual_drive':
            if self.settings['storage']:
                if len(registration_moids) < filter_length_threshold:
                    self.storage_virtual_drive_handler.set_get_filter(
                        "RegisteredDevice/Moid in (%s)" % (registration_moids_filter)
                    )
                cache = self.storage_virtual_drive_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'physical_disk':
            if self.settings['storage']:
                if len(registration_moids) < filter_length_threshold:
                    self.storage_physical_disk_handler.set_get_filter(
                        "RegisteredDevice/Moid in (%s)" % (registration_moids_filter)
                    )
                cache = self.storage_physical_disk_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        return True

    def set_filter(self, server):
        self.asset_device_contract_information_handler.set_get_filter(
            "DeviceId eq '%s'" % (server['Serial'])
        )
        self.boot_cdd_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_device_boot_security_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_hdd_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_iscsi_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_nvme_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_pxe_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_san_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_sd_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_uefi_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_usb_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.boot_vmedia_device_handler.set_get_filter(
            "ComputePhysical/Moid eq '%s'" % (server['Moid'])
        )
        self.cond_hclstatus_handler.set_get_filter(
            "ManagedObject/Moid eq '%s'" % (server['Moid'])
        )
        self.pci_handler.set_get_filter(
            "Parent/Moid eq '%s'" % (server['Moid'])
        )
        self.processor_unit_handler.set_get_filter(
            "ComputeBoard/Moid eq '%s'" % (server['Board']['Moid'])
        )
        self.running_firmware_handler.set_get_filter(
            "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
        )
        self.server_profile_handler.set_get_filter(
            "AssignedServer/Moid eq '%s'" % (server['Moid'])
        )
        self.storage_controller_handler.set_get_filter(
            "Parent/Moid eq '%s'" % (server['Board']['Moid'])
        )
        self.storage_physical_disk_handler.set_get_filter(
            "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
        )
        self.storage_virtual_drive_handler.set_get_filter(
            "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
        )
        self.tam_advisory_instance_handler.set_get_filter(
            "AffectedObject/Moid eq '%s'" % (server['Moid'])
        )

        adapter_moids = []
        for adapter in server['Adapters']:
            if adapter['ObjectType'] == 'adapter.Unit':
                adapter_moids.append(
                    adapter['Moid']
                )

        if len(adapter_moids) > 0:
            adapter_moids_list = []
            for adapter_moid in adapter_moids:
                adapter_moids_list.append('\'%s\'' % (adapter_moid))
            adapter_moids_filter = ', '.join(adapter_moids_list)

            self.adapter_unit_handler.set_get_filter(
                "Moid in (%s)" % (adapter_moids_filter)
            )

            self.adapter_ext_eth_interface_handler.set_get_filter(
                "AdapterUnit/Moid in (%s)" % (adapter_moids_filter)
            )

            self.adapter_host_eth_interface_handler.set_get_filter(
                "AdapterUnit/Moid in (%s)" % (adapter_moids_filter)
            )

            self.adapter_host_fc_interface_handler.set_get_filter(
                "AdapterUnit/Moid in (%s)" % (adapter_moids_filter)
            )

        if server['ObjectType'] == 'compute.RackUnit':
            self.bios_boot_mode_handler.set_get_filter(
                "ComputeRackUnit/Moid eq '%s'" % (server['Moid'])
            )
            self.boot_device_boot_mode_handler.set_get_filter(
                "ComputeRackUnit/Moid eq '%s'" % (server['Moid'])
            )
            self.cond_alarm_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
            )
            self.compute_board_handler.set_get_filter(
                "ComputeRackUnit/Moid eq '%s'" % (server['Moid'])
            )
            self.fan_handler.set_get_filter(
                "Parent/Moid eq '%s'" % (server['Moid'])
            )
            self.locator_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
            )
            self.memory_unit_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
            )
            self.psu_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
            )

        if server['ObjectType'] == 'compute.Blade':
            if self.settings['psu'] or self.settings['fan'] or self.settings['chassis']:
                self.add_chassis_object(server)

            self.bios_boot_mode_handler.set_get_filter(
                "ComputeBlade/Moid eq '%s'" % (server['Moid'])
            )
            self.boot_device_boot_mode_handler.set_get_filter(
                "ComputeBlade/Moid eq '%s'" % (server['Moid'])
            )
            self.cond_alarm_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s' and AffectedMo/Moid eq '%s'" % (
                    server['RegisteredDevice']['Moid'],
                    server['Moid']
                )
            )
            self.compute_board_handler.set_get_filter(
                "ComputeBlade/Moid eq '%s'" % (server['Moid'])
            )
            self.locator_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
            )
            self.memory_unit_handler.set_get_filter(
                "RegisteredDevice/Moid eq '%s' and Ancestors/any(a:a/Moid eq '%s')" % (
                    server['RegisteredDevice']['Moid'],
                    server['Moid']
                )
            )

            if self.chassis is None:
                self.psu_handler.set_get_filter(
                    "RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid'])
                )
                self.fan_handler.set_get_filter(
                    "Parent/Moid eq '%s'" % (server['Moid'])
                )

            else:
                self.psu_handler.set_get_filter(
                    "EquipmentChassis/Moid eq '%s'" % (self.chassis['Moid'])
                )
                self.fan_handler.set_get_filter(
                    "EquipmentChassis/Moid eq '%s'" % (self.chassis['Moid'])
                )

    def add_advisory_info(self):
        if not self.settings['advisory']:
            return

        self.server_info['AdvisorySummary'] = {}
        self.server_info['AdvisorySummary']['__Output'] = {}
        self.server_info['AdvisorySummary']['__Output']['High'] = 'Red'
        self.server_info['AdvisorySummary']['__Output']['Info'] = 'Blue'
        self.server_info['AdvisorySummary']['High'] = 0
        self.server_info['AdvisorySummary']['Info'] = 0

        self.server_info['AdvisoryInfo'] = []

        advisories = self.tam_advisory_instance_handler.get_all()
        for advisory in advisories:
            if advisory['Advisory']['ObjectType'] == 'tam.SecurityAdvisory':
                advisory_info = self.tam_security_advisory_handler.get_info(
                    advisory['Advisory']['Moid']
                )

                self.server_info['AdvisoryInfo'].append(
                    advisory_info
                )

                if advisory_info['Severity'] == 'high':
                    self.server_info['AdvisorySummary']['High'] = self.server_info['AdvisorySummary']['High'] + 1
                else:
                    self.server_info['AdvisorySummary']['Info'] = self.server_info['AdvisorySummary']['Info'] + 1

                continue

            self.log.error(
                'add_advisory_info',
                'Unsupported advisory: %s' % (advisory['Advisory']['ObjectType'])
            )

    def add_alarm_info(self, server, include_cleared=False):
        if not self.settings['alarm']:
            return

        self.server_info['AlarmInfo'] = []

        alarms = self.cond_alarm_handler.get_all()
        for alarm in alarms:
            alarm_info = self.cond_alarm_handler.get_info(
                alarm['Moid']
            )
            if alarm_info['Severity'] == 'Cleared' and not include_cleared:
                continue
            self.server_info['AlarmInfo'].append(
                alarm_info
            )

    def add_bios_info(self, server):
        return

    def add_board_info(self):
        if not self.settings['board'] and not self.settings['tpm']:
            return

        boards = self.compute_board_handler.get_all()
        if len(boards) == 0:
            self.server_info['BoardInfo'] = None

        if len(boards) > 1:
            self.log.error(
                'add_board_info',
                'Multiple board info objects found'
            )
            return

        board_id = boards[0]['Moid']
        self.server_info['BoardInfo'] = self.compute_board_handler.get_info(
            board_id
        )

        if not self.settings['board']:
            return

    def add_boot_info(self, server):
        if not self.settings['boot']:
            return

        self.server_info['BootInfo'] = {}
        self.server_info['BootInfo']['ConfiguredBootMode'] = None
        self.server_info['BootInfo']['ActualBootMode'] = None
        self.server_info['BootInfo']['SecureBoot'] = None
        self.server_info['BootInfo']['Order'] = []

        managed_objects = self.boot_device_boot_mode_handler.get_all()
        if len(managed_objects) != 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of boot device boot mode objects'
            )
        else:
            self.server_info['BootInfo']['ConfiguredBootMode'] = self.boot_device_boot_mode_handler.get_info(
                managed_objects[0]['Moid']
            )['ConfiguredBootMode']

        managed_objects = self.bios_boot_mode_handler.get_all()
        if len(managed_objects) != 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of bios boot mode objects'
            )
        else:
            self.server_info['BootInfo']['ActualBootMode'] = self.bios_boot_mode_handler.get_info(
                managed_objects[0]['Moid']
            )['ActualBootMode']

        managed_objects = self.boot_device_boot_security_handler.get_all()
        if len(managed_objects) != 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of boot device security mode objects'
            )
        else:
            self.server_info['BootInfo']['SecureBoot'] = self.boot_device_boot_security_handler.get_info(
                managed_objects[0]['Moid']
            )['SecureBoot']

        if len(server['BootCddDevices']) > 0:
            managed_objects = self.boot_cdd_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_cdd_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootCddDevices']) > 0:
            managed_objects = self.boot_cdd_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_cdd_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootHddDevices']) > 0:
            managed_objects = self.boot_hdd_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_hdd_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootIscsiDevices']) > 0:
            managed_objects = self.boot_iscsi_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_iscsi_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootNvmeDevices']) > 0:
            managed_objects = self.boot_nvme_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_nvme_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootPxeDevices']) > 0:
            managed_objects = self.boot_pxe_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_pxe_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootSanDevices']) > 0:
            managed_objects = self.boot_san_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_san_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootSdDevices']) > 0:
            managed_objects = self.boot_sd_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_sd_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootUefiShellDevices']) > 0:
            managed_objects = self.boot_uefi_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_uefi_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootUsbDevices']) > 0:
            managed_objects = self.boot_usb_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_usb_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        if len(server['BootVmediaDevices']) > 0:
            managed_objects = self.boot_vmedia_device_handler.get_all()
            for managed_object in managed_objects:
                self.server_info['BootInfo']['Order'].append(
                    self.boot_vmedia_device_handler.get_info(
                        managed_object['Moid']
                    )
                )

        self.server_info['BootInfo']['Order'] = sorted(
            self.server_info['BootInfo']['Order'],
            key=lambda i: i['Order']
        )

    def add_chassis_object(self, server):
        if self.chassis is not None:
            return

        self.chassis = self.equipment_chassis_handler.get(
            server['EquipmentChassis']['Moid']
        )

    def add_chassis_info(self):
        if self.chassis is None:
            return

        if not self.settings['chassis']:
            return

        self.server_info['ChassisInfo'] = self.equipment_chassis_handler.get_summary(
            self.chassis
        )

    def add_connector_info(self, server):
        if not self.settings['connector']:
            return

        self.server_info['ConnectorInfo'] = self.asset_device_registration_handler.get_info(
            server['RegisteredDevice']['Moid'],
            cache=False
        )

    def add_contract_info(self):
        if not self.settings['contract']:
            return

        managed_objects = self.asset_device_contract_information_handler.get_all()
        if len(managed_objects) != 1:
            self.log.error(
                'add_contract_info',
                'Unexpected number of device contract objects'
            )
        else:
            self.server_info['ContractInfo'] = self.asset_device_contract_information_handler.get_info(
                managed_objects[0]['Moid']
            )

    def add_kvm_info(self, server):
        if not self.settings['kvm']:
            return

        self.server_info['KvmInfo'] = {}
        self.server_info['KvmInfo']['KvmIpAddresses'] = server['KvmIpAddresses']
        self.server_info['KvmInfo']['KvmServerStateEnabled'] = server['KvmServerStateEnabled']
        self.server_info['KvmInfo']['KvmVendor'] = server['KvmVendor']
        self.server_info['KvmInfo']['TunneledKvm'] = server['TunneledKvm']

    def add_cpu_info(self, server):
        keys = [
            'NumCpus',
            'NumCpuCores',
            'NumThreads'
        ]
        for key in keys:
            if key in keys:
                self.server_info[key] = server[key]
        self.server_info['Cpu'] = '%sS %sC %sT' % (
            server['NumCpus'],
            server['NumCpuCores'],
            server['NumThreads']
        )

        if self.settings['cpu']:
            self.server_info['CpuInfo'] = self.processor_unit_handler.get_processor_units_info()

    def add_fan_info(self, server):
        if not self.settings['fan']:
            return

        if self.server_info['Type'] == 'Blade':
            if self.chassis is None:
                self.server_info['FanSummary'] = ''
                self.server_info['FanHealthy'] = True
                self.server_info['FanInfo'] = None
                return

            self.server_info['FanInfo'] = []

            for fan_module in self.chassis['Fanmodules']:
                self.server_info['FanInfo'].append(
                    self.fan_handler.get_fan_info(
                        fan_module['Moid']
                    )
                )

            self.server_info['FanInfo'] = sorted(
                self.server_info['FanInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['FanOn'] = 0
            for fan_module in self.chassis['Fanmodules']:
                if self.fan_handler.get_fan_state(fan_module['Moid']):
                    self.server_info['FanOn'] = self.server_info['FanOn'] + 1

            self.server_info['FanCount'] = len(self.chassis['Fanmodules'])
            self.server_info['FanSummary'] = '%s/%s' % (
                self.server_info['FanOn'],
                self.server_info['FanCount']
            )
            self.server_info['FanHealthy'] = True
            if self.server_info['FanOn'] < self.server_info['FanCount']:
                self.server_info['FanHealthy'] = False

        if self.server_info['Type'] == 'Rack':
            self.server_info['FanInfo'] = []

            for fan_module in server['Fanmodules']:
                self.server_info['FanInfo'].append(
                    self.fan_handler.get_fan_info(
                        fan_module['Moid']
                    )
                )

            self.server_info['FanInfo'] = sorted(
                self.server_info['FanInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['FanOn'] = 0
            for fan_module in server['Fanmodules']:
                if self.fan_handler.get_fan_state(fan_module['Moid']):
                    self.server_info['FanOn'] = self.server_info['FanOn'] + 1

            self.server_info['FanCount'] = len(server['Fanmodules'])
            self.server_info['FanSummary'] = '%s/%s' % (
                self.server_info['FanOn'],
                self.server_info['FanCount']
            )
            self.server_info['FanHealthy'] = True
            if self.server_info['FanOn'] < self.server_info['FanCount']:
                self.server_info['FanHealthy'] = False

    def add_firmware_info(self, server):
        if not self.settings['fw']:
            return

        self.server_info['FirmwarewComponents'] = self.running_firmware_handler.add_info(
            self.info_handler.get_objects_with_ancestor(
                self.running_firmware_handler.get_all(),
                server['ObjectType'],
                self.server_info['Moid'],
                sort_by='Dn'
            )
        )

        self.server_info['FirmwareVersion'] = self.running_firmware_handler.get_firmware_version(
            self.server_info['FirmwarewComponents']
        )

    def add_gpu_info(self, server):
        if not self.settings['gpu']:
            return

        self.server_info['GpuInfo'] = []

        for pci_device_info in self.server_info['PciDevicesInfo']:
            if '-GPU-' in pci_device_info['Pid']:
                self.server_info['GpuInfo'].append(
                    pci_device_info
                )

        if not self.settings['pci']:
            del self.server_info['PciDevicesInfo']

    def add_group_info(self):
        self.server_info['Groups'] = ''
        if self.my_servers_serials is not None:
            if self.server_info['Serial'] in self.my_servers_serials:
                self.server_info['Groups'] = ','.join(
                    self.my_servers_serials[self.server_info['Serial']]
                )

    def add_hcl_info(self):
        if not self.settings['hcl']:
            return

        hcl_infos = self.cond_hclstatus_handler.get_all()
        if len(hcl_infos) == 0:
            self.server_info['HclInfo'] = None

        if len(hcl_infos) > 1:
            self.log.error(
                'add_hcl_info',
                'Multiple hcl info objects found'
            )
            return

        hcl_info_id = hcl_infos[0]['Moid']
        self.server_info['HclInfo'] = self.cond_hclstatus_handler.get_info(
            hcl_info_id
        )

        self.cond_hclstatus_detail_handler.set_get_filter(
            "HclStatus/Moid eq '%s'" % (hcl_info_id)
        )
        hcl_details = self.cond_hclstatus_detail_handler.get_all()
        self.server_info['HclInfo']['Details'] = []
        for hcl_detail in hcl_details:
            self.server_info['HclInfo']['Details'].append(
                self.cond_hclstatus_detail_handler.get_info(
                    hcl_detail['Moid']
                )
            )

    def add_health_info(self, server):
        # Rack
        #
        # "AlarmSummary": {
        #     "ClassId": "compute.AlarmSummary",
        #     "Critical": 0,
        #     "ObjectType": "compute.AlarmSummary",
        #     "Warning": 1
        # },
        #
        # Blade
        #
        # "AlarmSummary": {
        #     "ClassId": "compute.AlarmSummary",
        #     "Critical": 9,
        #     "Health": "Critical",
        #     "Info": 0,
        #     "ObjectType": "compute.AlarmSummary",
        #     "Warning": 0
        # },
        self.server_info['AlarmSummary'] = {}
        self.server_info['AlarmSummary']['__Output'] = {}
        self.server_info['AlarmSummary']['__Output']['Critical'] = 'Red'
        self.server_info['AlarmSummary']['__Output']['Warning'] = 'Yellow'
        self.server_info['AlarmSummary']['__Output']['Info'] = 'Blue'
        self.server_info['AlarmSummary']['__Output']['Cleared'] = 'Green'

        for key in ['Critical', 'Warning', 'Info', 'Cleared']:
            if key in server['AlarmSummary']:
                self.server_info['AlarmSummary'][key] = server['AlarmSummary'][key]

        self.server_info['Health'] = 'Healthy'

        if self.server_info['AlarmSummary']['Warning'] == 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            if 'Info' in self.server_info['AlarmSummary'] and self.server_info['AlarmSummary']['Info'] > 0:
                self.server_info['Health'] = 'Healthy (%s)' % (
                    self.server_info['AlarmSummary']['Info']
                )

        if self.server_info['AlarmSummary']['Warning'] > 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            self.server_info['Health'] = 'Warnings (%s)' % (
                self.server_info['AlarmSummary']['Warning']
            )

        if self.server_info['AlarmSummary']['Critical'] > 0:
            self.server_info['Health'] = 'Critical (%s)' % (
                self.server_info['AlarmSummary']['Critical']
            )

    def add_license_info(self, server):
        if not self.settings['license']:
            return

        for tag in server['Tags']:
            if tag['Key'] == 'Intersight.LicenseTier':
                self.server_info['LicenseInfo'] = {}
                self.server_info['LicenseInfo']['Tier'] = tag['Value']

    def add_locator_info(self, server):
        if self.state_enabled:
            self.server_info['LocatorLedOn'] = False

            if not self.settings['locator']:
                return

            if self.server_info['Type'] == 'Rack':
                try:
                    self.server_info['LocatorLedOn'] = self.locator_handler.get_locator_led(
                        server['LocatorLed']['Moid']
                    )
                except BaseException:
                    pass

    def get_management_ip(self, server):
        try:
            if 'KvmIpAddresses' in server:
                for kvm_ip in server['KvmIpAddresses']:
                    if kvm_ip['ClassId'] == 'compute.IpAddress':
                        return kvm_ip['Address']
        except BaseException:
            print(traceback.format_exc())
        return None

    def add_management_ip(self, server):
        self.server_info['ManagementIp'] = self.get_management_ip(server)

    def add_management_options(self):
        self.server_info['Redfish'] = {}
        self.server_info['UCSM'] = {}
        self.server_info['IMC'] = {}

        if self.server_info['ManagementMode'] == 'UCSM':
            self.server_info['Redfish']['Capable'] = False
            self.server_info['Redfish']['Enabled'] = False
            self.server_info['UCSM']['Capable'] = True
            self.server_info['UCSM']['Enabled'] = self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(
                self.server_info['Serial']
            )
            self.server_info['IMC']['Capable'] = False
            self.server_info['IMC']['Enabled'] = False

        else:
            self.server_info['Redfish']['Capable'] = True
            self.server_info['Redfish']['Enabled'] = self.redfish_endpoint_settings_handler.is_redfish_endpoint(
                self.server_info['Serial']
            )
            self.server_info['UCSM']['Capable'] = False
            self.server_info['UCSM']['Enabled'] = False
            self.server_info['IMC']['Capable'] = True
            self.server_info['IMC']['Enabled'] = False

    def add_memory_info(self, server):
        keys = [
            'AvailableMemory',
            'TotalMemory'
        ]
        for key in keys:
            if key in keys:
                self.server_info[key] = server[key]

        self.server_info['UsedMemory'] = self.server_info['TotalMemory'] - self.server_info['AvailableMemory']

        self.server_info['TotalMemoryUnit'] = self.info_handler.convert_memory(
            self.server_info['TotalMemory'] * 1024 * 1024,
            precision=0
        )

        self.server_info['TotalMemoryGB'] = int(
            self.server_info['TotalMemory'] / 1024
        )

        self.server_info['AvailableMemoryUnit'] = self.info_handler.convert_memory(
            self.server_info['AvailableMemory'] * 1024 * 1024,
            precision=0
        )

        self.server_info['AvailableMemoryGB'] = int(
            self.server_info['AvailableMemory'] / 1024
        )

        self.server_info['UsedMemoryUnit'] = self.info_handler.convert_memory(
            self.server_info['UsedMemory'] * 1024 * 1024,
            precision=0
        )

        self.server_info['UsedMemoryGB'] = int(
            self.server_info['UsedMemory'] / 1024
        )

        usage = int(self.server_info['UsedMemory'] * 100 / self.server_info['TotalMemory'])
        self.server_info['UsedMemoryPct'] = usage
        self.server_info['UsedMemoryPctUnit'] = '%s%%' % (usage)

        if self.settings['memory'] and self.server_info['Type'] == 'Rack':
            self.server_info['MemoryInfo'] = self.memory_unit_handler.get_memory_units_info()

        if self.settings['memory'] and self.server_info['Type'] == 'Blade':
            chassis_memory_info = self.memory_unit_handler.get_memory_units_info()
            memory_info = []

            for item in chassis_memory_info:
                if item['ServerId'] == server['Moid']:
                    memory_info.append(item)

            self.server_info['MemoryInfo'] = memory_info

    def add_ext_eth_info(self):
        if not self.settings['net'] and not self.settings['mac']:
            return

        if self.cache_enabled:
            if not self.settings['net']:
                if 'MacAddressInfo' in self.server_info['Cache']:
                    return

        self.server_info['ExtEthInfo'] = []

        interfaces = self.adapter_ext_eth_interface_handler.get_all()
        self.log.set_log(
            'server_info.%s.adapter_ext_eth_interface' % (self.server_info['Moid']),
            interfaces,
            json_conversion=True
        )

        for interface in interfaces:
            interface_info = self.adapter_ext_eth_interface_handler.get_info(
                interface['Moid']
            )

            if self.settings['mac']:
                mac_info = {}
                mac_info['InterfaceDn'] = interface_info['Dn']
                mac_info['InterfaceName'] = interface_info['Dn'].split('/')[-1]
                mac_info['MacAddress'] = interface_info['MacAddress'].lower()
                mac_info['AdapterModel'] = None
                mac_info['AdapterPciSlot'] = None

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if interface['Moid'] in adapter_info['ExtEthIfsIds']:
                    interface_info['AdapterName'] = adapter_info['Name']
                    interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    if self.settings['mac']:
                        mac_info['AdapterModel'] = adapter_info['Model']
                        mac_info['AdapterPciSlot'] = adapter_info['PciSlot']

            self.server_info['ExtEthInfo'].append(
                interface_info
            )

            if self.settings['mac']:
                self.server_info['MacAddressInfo'].append(
                    mac_info
                )

        self.server_info['ExtEthInfo'] = sorted(
            self.server_info['ExtEthInfo'],
            key=lambda i: (
                i['Dn'],
                i['InterfaceId']
            )
        )

    def add_host_eth_info(self):
        if not self.settings['net'] and not self.settings['mac']:
            return

        if self.cache_enabled:
            if not self.settings['net']:
                if 'MacAddressInfo' in self.server_info['Cache']:
                    return

        self.server_info['HostEthInfo'] = []

        interfaces = self.adapter_host_eth_interface_handler.get_all()
        self.log.set_log(
            'server_info.%s.adapter_host_eth_interface' % (self.server_info['Moid']),
            interfaces,
            json_conversion=True
        )

        for interface in interfaces:
            interface_info = self.adapter_host_eth_interface_handler.get_info(
                interface['Moid']
            )

            if self.settings['mac']:
                mac_info = {}
                mac_info['InterfaceDn'] = interface_info['Dn']
                mac_info['InterfaceName'] = interface_info['Dn'].split('/')[-1]
                mac_info['MacAddress'] = interface_info['MacAddress'].lower()
                mac_info['AdapterModel'] = None
                mac_info['AdapterPciSlot'] = None

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if interface['Moid'] in adapter_info['HostEthIfsIds']:
                    interface_info['AdapterName'] = adapter_info['Name']
                    interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    if self.settings['mac']:
                        mac_info['AdapterModel'] = adapter_info['Model']
                        mac_info['AdapterPciSlot'] = adapter_info['PciSlot']

            self.server_info['HostEthInfo'].append(
                interface_info
            )

            if self.settings['mac']:
                self.server_info['MacAddressInfo'].append(
                    mac_info
                )

        self.server_info['HostEthInfo'] = sorted(
            self.server_info['HostEthInfo'],
            key=lambda i: (
                i['AdapterName'],
                i['Name']
            )
        )

    def add_host_fc_info(self):
        if not self.settings['net']:
            return

        self.server_info['HostFcInfo'] = []

        interfaces = self.adapter_host_fc_interface_handler.get_all()
        for interface in interfaces:
            interface_info = self.adapter_host_fc_interface_handler.get_info(
                interface['Moid']
            )

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if interface['Moid'] in adapter_info['HostFcIfsIds']:
                    interface_info['AdapterName'] = adapter_info['Name']
                    interface_info['AdapterPciSlot'] = adapter_info['PciSlot']

            self.server_info['HostFcInfo'].append(
                interface_info
            )

        self.server_info['HostFcInfo'] = sorted(
            self.server_info['HostFcInfo'],
            key=lambda i: (
                i['AdapterName'],
                i['Name']
            )
        )

    def add_adapters_info(self):
        if not self.settings['net'] and not self.settings['mac']:
            return

        if self.settings['mac']:
            self.server_info['MacAddressInfo'] = []

        if self.cache_enabled:
            if not self.settings['net']:
                mac_address_info = self.cache_handler.get_intersight_cache_entry_property(
                    self.server_info['Serial'],
                    'MacAddressInfo'
                )
                if mac_address_info is None:
                    self.log.error(
                        'add_adapters_info',
                        'MacAddressInfo cache miss'
                    )
                if mac_address_info is not None:
                    self.server_info['MacAddressInfo'] = mac_address_info
                    self.server_info['Cache'].append('MacAddressInfo')
                    return

        self.server_info['AdaptersInfo'] = []

        adapters = self.adapter_unit_handler.get_all()
        self.log.set_log(
            'server_info.%s.adapter_unit' % (self.server_info['Moid']),
            adapters,
            json_conversion=True
        )

        for adapter in adapters:
            self.server_info['AdaptersInfo'].append(
                self.adapter_unit_handler.get_info(
                    adapter['Moid']
                )
            )

        self.server_info['AdaptersInfo'] = sorted(
            self.server_info['AdaptersInfo'],
            key=lambda i: i['Name']
        )

    def add_pci_info(self, server):
        if not self.settings['pci'] and not self.settings['gpu']:
            return

        if self.cache_enabled:
            pci_devices_info = self.cache_handler.get_intersight_cache_entry_property(
                self.server_info['Serial'],
                'PciDevicesInfo'
            )

            pci_models = self.cache_handler.get_intersight_cache_entry_property(
                self.server_info['Serial'],
                'PciModels'
            )

            if pci_devices_info is not None and pci_models is not None:
                self.server_info['PciDevicesInfo'] = pci_devices_info
                self.server_info['PciModels'] = pci_models
                self.server_info['Cache'].append('PciDevicesInfo')
                self.server_info['Cache'].append('PciModels')
                return

        self.server_info['PciDevicesInfo'] = []
        for server_pci_device in server['PciDevices']:
            self.server_info['PciDevicesInfo'].append(
                self.pci_handler.get_pci_info(
                    server_pci_device['Moid']
                )
            )
        self.server_info['PciDevicesInfo'] = sorted(
            self.server_info['PciDevicesInfo'],
            key=lambda i: i['Dn']
        )

        self.server_info['PciModels'] = []
        for server_pci_device in server['PciDevices']:
            self.server_info['PciModels'].append(
                self.pci_handler.get_pci_model(
                    server_pci_device['Moid']
                )
            )

    def add_power_info(self):
        if not self.settings['power']:
            return

        self.server_info['Power'] = None

        if self.server_info['Redfish']['Enabled']:
            self.server_info['Power'] = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
                self.server_info['Serial'],
                'power'
            )

        if self.server_info['UCSM']['Enabled']:
            self.server_info['Power'] = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
                self.server_info['Serial'],
                'power'
            )

    def add_profile_info(self, server):
        if not self.settings['profile']:
            return

        managed_objects = self.server_profile_handler.get_all()
        if len(managed_objects) != 1:
            return

        profile_id = managed_objects[0]['Moid']
        self.server_info['ProfileInfo'] = self.server_profile_handler.get_info(
            profile_id
        )

        self.search_item_handler.set_get_filter(
            "IndexMotypes eq 'policy.AbstractPolicy' and Profiles/any(a:a/Moid eq '%s')" % (profile_id)
        )
        policies = self.search_item_handler.get_all()
        self.server_info['ProfileInfo']['Policies'] = []
        for policy in policies:
            policy_info = {}
            policy_info['__Output'] = {}
            policy_info['Moid'] = policy['Moid']
            policy_info['Name'] = policy['Name']
            policy_info['ModTime'] = policy['ModTime']
            policy_info['ClassId'] = policy['ClassId']
            policy_info['Shared'] = False
            if len(policy['Profiles']) > 1:
                policy_info['Shared'] = True

            policy_info['InSync'] = True
            policy_info['__Output']['InSync'] = 'Green'
            for config_change_info in self.server_info['ProfileInfo']['ConfigChangeDetails']:
                if config_change_info['EntityMoid'] == policy_info['Moid']:
                    if config_change_info['EntityType'] == policy_info['ClassId']:
                        policy_info['InSync'] = False
                        policy_info['__Output']['InSync'] = 'Red'

            self.server_info['ProfileInfo']['Policies'].append(
                policy_info
            )

    def add_psu_info(self, server):
        if not self.settings['psu']:
            return

        if self.server_info['Type'] == 'Blade':
            if self.chassis is None:
                self.server_info['PsuSummary'] = ''
                self.server_info['PsuHealthy'] = True
                self.server_info['PsuInfo'] = None
                return

            self.server_info['PsuInfo'] = []

            for psu in self.chassis['Psus']:
                self.server_info['PsuInfo'].append(
                    self.psu_handler.get_psu_info(
                        psu['Moid']
                    )
                )

            self.server_info['PsuInfo'] = sorted(
                self.server_info['PsuInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['PsuOn'] = 0
            for psu in self.chassis['Psus']:
                if self.psu_handler.get_psu_state(psu['Moid']):
                    self.server_info['PsuOn'] = self.server_info['PsuOn'] + 1

            self.server_info['PsuCount'] = len(self.chassis['Psus'])
            self.server_info['PsuSummary'] = '%s/%s' % (
                self.server_info['PsuOn'],
                self.server_info['PsuCount']
            )
            self.server_info['PsuHealthy'] = True
            if self.server_info['PsuOn'] < self.server_info['PsuCount']:
                self.server_info['PsuHealthy'] = False

        if self.server_info['Type'] == 'Rack':
            self.server_info['PsuInfo'] = []

            for psu in server['Psus']:
                self.server_info['PsuInfo'].append(
                    self.psu_handler.get_psu_info(
                        psu['Moid']
                    )
                )

            self.server_info['PsuInfo'] = sorted(
                self.server_info['PsuInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['PsuOn'] = 0
            for psu in server['Psus']:
                if self.psu_handler.get_psu_state(psu['Moid']):
                    self.server_info['PsuOn'] = self.server_info['PsuOn'] + 1

            self.server_info['PsuCount'] = len(server['Psus'])
            self.server_info['PsuSummary'] = '%s/%s' % (
                self.server_info['PsuOn'],
                self.server_info['PsuCount']
            )
            self.server_info['PsuHealthy'] = True
            if self.server_info['PsuOn'] < self.server_info['PsuCount']:
                self.server_info['PsuHealthy'] = False

    def add_registration_info(self, server):
        if not self.settings['registration']:
            self.server_info['Connected'] = False
            return

        self.server_info['Connected'] = False
        device_registration_info = self.asset_device_registration_handler.get_info(
            server['RegisteredDevice']['Moid'],
            cache=False
        )
        if device_registration_info is not None:
            self.server_info['Connected'] = device_registration_info['Connected']

    def add_setting_id(self):
        if self.settings['server_setting_id']:
            self.server_info['ServerSettingId'] = self.compute_server_setting_handler.get_id_by_device_moid(
                self.server_info['DeviceMoId']
            )

    def add_storage_virtual_disk_info(self, server_id):
        self.server_info['VirtualDisks'] = self.storage_virtual_drive_handler.get_virtual_drives_info(
            server_id,
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )

        self.server_info['VirtualDiskCount'] = self.storage_virtual_drive_handler.get_virtual_drives_count(
            server_id
        )

        self.server_info['VirtualDiskCapacity'] = self.storage_virtual_drive_handler.get_virtual_drives_size(
            server_id
        )
        self.server_info['VirtualDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['VirtualDiskCapacity']
        )

    def add_storage_hdd_info(self, server_id):
        self.server_info['HddDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            server_id,
            disk_type='HDD',
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['HddDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
            server_id,
            disk_type='HDD'
        )
        self.server_info['HddDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            server_id,
            disk_type='HDD'
        )
        self.server_info['HddDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['HddDiskCapacity']
        )

    def add_storage_ssd_info(self, server_id):
        self.server_info['SsdDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            server_id,
            disk_type='SSD',
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['SsdDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
            server_id,
            disk_type='SSD'
        )
        self.server_info['SsdDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            server_id,
            disk_type='SSD'
        )
        self.server_info['SsdDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['SsdDiskCapacity']
        )

    def add_storage_physical_disk_info(self, server_id):
        self.server_info['PhysicalDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            server_id,
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['PhysicalDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
            server_id
        )
        self.server_info['PhysicalDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            server_id
        )
        self.server_info['PhysicalDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['PhysicalDiskCapacity']
        )

    def add_storage_info(self, server):
        if not self.settings['storage']:
            return

        if self.server_info['Type'] == 'Rack':
            storage_server_id = server['Board']['Moid']
            self.server_info['StorageControllersInfo'] = self.storage_controller_handler.get_board_storage_controllers_info(
                server['Board']['Moid']
            )

            if self.server_info['StorageControllersInfo'] is None:
                self.server_info['StorageControllersCount'] = 0
            else:
                self.server_info['StorageControllersCount'] = len(self.server_info['StorageControllersInfo'])

        if self.server_info['Type'] == 'Blade':
            storage_server_id = server['Moid']
            self.server_info['StorageControllersInfo'] = self.storage_controller_handler.get_blade_storage_controllers_info(
                self.server_info['Moid']
            )
            if self.server_info['StorageControllersInfo'] is None:
                self.server_info['StorageControllersCount'] = 0
            else:
                self.server_info['StorageControllersCount'] = len(self.server_info['StorageControllersInfo'])

        self.add_storage_virtual_disk_info(storage_server_id)
        self.add_storage_hdd_info(storage_server_id)
        self.add_storage_ssd_info(storage_server_id)
        self.add_storage_physical_disk_info(storage_server_id)

        self.server_info['StorageDrives'] = '%sC %sH %sS %sVD' % (
            self.server_info['StorageControllersCount'],
            self.server_info['HddDiskCount'],
            self.server_info['SsdDiskCount'],
            self.server_info['VirtualDiskCount']
        )

        self.server_info['StorageCapacity'] = 'R %s , VD %s' % (
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

        self.server_info['StorageSummary'] = '%sC %sH %sS %sVD R%s L%s' % (
            self.server_info['StorageControllersCount'],
            self.server_info['HddDiskCount'],
            self.server_info['SsdDiskCount'],
            self.server_info['VirtualDiskCount'],
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

    def add_thermal_info(self):
        if not self.settings['thermal']:
            return

        self.server_info['Thermal'] = None

        if self.server_info['Redfish']['Enabled']:
            if self.server_info['OperPowerState'] == 'on':
                self.server_info['Thermal'] = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
                    self.server_info['Serial'],
                    'thermal'
                )

        if self.server_info['UCSM']['Enabled']:
            self.server_info['Thermal'] = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
                self.server_info['Serial'],
                'thermal'
            )

    def add_tpm_info(self):
        if not self.settings['tpm']:
            return

        if 'BoardInfo' not in self.server_info:
            self.server_info['TpmInfo'] = None
            return

        if self.server_info['BoardInfo']['EquipmentTpmsCount'] == 0:
            self.server_info['TpmInfo'] = None
            return

        tpm_moids_list = []
        for tpm_moid in self.server_info['BoardInfo']['EquipmentTpmsIds']:
            tpm_moids_list.append('\'%s\'' % (tpm_moid))
        tpm_moids_filter = ', '.join(tpm_moids_list)

        self.equipment_tpm_handler.set_get_filter(
            "Moid in (%s)" % (tpm_moids_filter)
        )

        tpms = self.equipment_tpm_handler.get_all()
        self.server_info['TpmInfo'] = []
        for tpm in tpms:
            self.server_info['TpmInfo'].append(
                self.equipment_tpm_handler.get_info(
                    tpm['Moid']
                )
            )

        if not self.settings['board']:
            del self.server_info['BoardInfo']

    def add_workflow_info(self):
        if self.settings['workflow'] is None:
            return

        self.server_info['Workflow'] = {}
        self.server_info['Workflow']['Days'] = int(self.settings['workflow'] / 86400)
        self.server_info['Workflow']['Running'] = None
        self.server_info['Workflow']['LatestMoid'] = None
        self.server_info['Workflow']['Last'] = []

        if self.last_workflows is None:
            self.last_workflows = self.workflow.get_last(
                seconds=self.settings['workflow']
            )
            if self.last_workflows is None:
                return

        latest_create_time = None
        for last_workflow in self.last_workflows:
            if self.workflow.is_server_workflow(self.server_info['Moid'], last_workflow):
                workflow_info = self.workflow.get_workflow_info(
                    last_workflow
                )
                if workflow_info['Running']:
                    self.server_info['Workflow']['Running'] = workflow_info
                    continue

                if latest_create_time is None or latest_create_time < workflow_info['CreateTimeEpoch']:
                    self.server_info['Workflow']['LatestMoid'] = workflow_info['Moid']
                    latest_create_time = workflow_info['CreateTimeEpoch']

                self.server_info['Workflow']['Last'].append(
                    workflow_info
                )

        self.server_info['Workflow']['Last'] = sorted(
            self.server_info['Workflow']['Last'],
            key=lambda i: i['CreateTimeEpoch'], reverse=True
        )

    def add_state_flag(self):
        color = ':'
        if self.server_info['OperPowerState'] == 'on':
            state = 'P+'
            color = '%sGG' % (color)
        else:
            state = 'P-'
            color = '%sRR' % (color)

        if self.server_info['AlarmSummary']['Warning'] == 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            alarm_state = 'H'
            alarm_color = 'G'.rjust(len(alarm_state), 'G')
            state = '%s %s' % (state, alarm_state)
            color = '%s.%s' % (color, alarm_color)
        if self.server_info['AlarmSummary']['Warning'] > 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            alarm_state = 'W(%s)' % (self.server_info['AlarmSummary']['Warning'])
            alarm_color = 'Y'.rjust(len(alarm_state), 'Y')
            state = '%s %s' % (state, alarm_state)
            color = '%s.%s' % (color, alarm_color)
        if self.server_info['AlarmSummary']['Critical'] > 0:
            alarm_state = 'C(%s)' % (self.server_info['AlarmSummary']['Critical'])
            alarm_color = 'R'.rjust(len(alarm_state), 'R')
            state = '%s %s' % (state, alarm_state)
            color = '%s.%s' % (color, alarm_color)

        if self.server_info['LocatorLedOn']:
            state = '%s L' % (state)
            color = '%s..' % (color)

        self.server_info['FlagState'] = state
        self.server_info['__Output']['FlagState'] = color

    def add_management_flag(self):
        color = ':'
        state = ''

        if self.server_info['Connected']:
            state = '%sC' % (state)
            color = '%sG' % (color)
        else:
            state = '%sc' % (state)
            color = '%sR' % (color)

        if self.server_info['UCSM']['Capable']:
            if self.server_info['UCSM']['Enabled']:
                state = '%sU' % (state)
                color = '%sG' % (color)
            else:
                state = '%su' % (state)
                color = '%sY' % (color)

        if self.server_info['Redfish']['Capable']:
            if self.server_info['Redfish']['Enabled']:
                state = '%sR' % (state)
                color = '%sG' % (color)
            else:
                state = '%sr' % (state)
                color = '%sY' % (color)

        if self.server_info['IMC']['Capable']:
            if self.server_info['IMC']['Enabled']:
                state = '%sI' % (state)
                color = '%sG' % (color)
            else:
                state = '%si' % (state)
                color = '%sY' % (color)

        self.server_info['FlagManagement'] = state
        self.server_info['__Output']['FlagManagement'] = color

    def add_workflow_flag(self):
        state = ''
        color = ':'
        if self.settings['workflow'] is not None:
            if self.server_info['Workflow']['Running'] is not None:
                state = '%sR' % (state)
                color = '%sY' % (color)

            if len(self.server_info['Workflow']['Last']) > 0:
                completed = 0
                failed = 0
                latest_completed = True

                for workflow_info in self.server_info['Workflow']['Last']:
                    if workflow_info['Moid'] == self.server_info['Workflow']['LatestMoid']:
                        latest_completed = workflow_info['Completed']

                    if workflow_info['Completed']:
                        completed = completed + 1
                    else:
                        failed = failed + 1

                if completed > 0:
                    completed_color = ''.join(['G' * len(str(completed))])
                    if state == '':
                        state = '%sC%s' % (state, completed)
                        color = '%sG%s' % (color, completed_color)
                    else:
                        state = '%s C%s' % (state, completed)
                        color = '%s.G%s' % (color, completed_color)

                if failed > 0:
                    failed_color = ''.join(['R' * len(str(failed))])
                    if state == '':
                        state = '%sF%s' % (state, failed)
                        color = '%sR%s' % (color, failed_color)
                    else:
                        state = '%s F%s' % (state, failed)
                        color = '%s.R%s' % (color, failed_color)

                if not latest_completed:
                    state = '%s!' % (state)
                    color = '%sR' % (color)

        self.server_info['FlagWorkflow'] = state
        self.server_info['__Output']['FlagWorkflow'] = color

    def add_flags(self):
        if self.state_enabled:
            self.add_state_flag()
            self.add_management_flag()
            self.add_workflow_flag()

    def set_server_info_cache(self):
        if 'MacAddressInfo' in self.server_info:
            self.log.debug(
                'set_server_info_cache',
                'Server %s MacAddressInfo' % (self.server_info['Serial'])
            )
            self.cache_handler.set_intersight_cache_entry_property(
                self.server_info['Serial'],
                'MacAddressInfo',
                self.server_info['MacAddressInfo']
            )

        if 'PciDevicesInfo' in self.server_info:
            self.log.debug(
                'set_server_info_cache',
                'Server %s PciDevicesInfo' % (self.server_info['Serial'])
            )
            self.cache_handler.set_intersight_cache_entry_property(
                self.server_info['Serial'],
                'PciDevicesInfo',
                self.server_info['PciDevicesInfo']
            )

        if 'PciModels' in self.server_info:
            self.log.debug(
                'set_server_info_cache',
                'Server %s PciModels' % (self.server_info['Serial'])
            )
            self.cache_handler.set_intersight_cache_entry_property(
                self.server_info['Serial'],
                'PciModels',
                self.server_info['PciModels']
            )

    def get_server_info(self, server, include_object=False, state_enabled=True, cache_enabled=False):
        if server is None:
            return None

        self.state_enabled = state_enabled
        self.cache_enabled = cache_enabled

        self.log.set_log(
            'server.%s' % (server['Moid']),
            server,
            json_conversion=True
        )

        self.server_info = {}
        self.server_info['__Output'] = {}
        self.server_info['StateEnabled'] = self.state_enabled
        self.server_info['Cache'] = []
        if include_object:
            self.server_info['IntersightObject'] = server

        keys = [
            'Moid',
            'DeviceMoId',
            'Name',
            'Model',
            'Serial',
            'ManagementMode',
            'OperPowerState'
        ]
        for key in keys:
            self.server_info[key] = server[key]

        if server['ObjectType'] == 'compute.RackUnit':
            self.server_info['Type'] = 'Rack'
            self.server_info['TypeModel'] = '(R) %s' % (self.server_info['Model'])

        if server['ObjectType'] == 'compute.Blade':
            self.server_info['Type'] = 'Blade'
            self.server_info['TypeModel'] = '(B) %s' % (server['Model'])

        self.set_filter(server)

        self.add_advisory_info()
        self.add_alarm_info(server)
        self.add_bios_info(server)
        self.add_board_info()
        self.add_boot_info(server)
        self.add_chassis_info()
        self.add_connector_info(server)
        self.add_contract_info()
        self.add_cpu_info(server)
        self.add_fan_info(server)
        self.add_firmware_info(server)
        self.add_group_info()
        self.add_health_info(server)
        self.add_hcl_info()
        self.add_kvm_info(server)
        self.add_license_info(server)
        self.add_locator_info(server)
        self.add_management_ip(server)
        self.add_management_options()
        self.add_memory_info(server)
        self.add_pci_info(server)
        self.add_gpu_info(server)
        self.add_adapters_info()
        self.add_ext_eth_info()
        self.add_host_eth_info()
        self.add_host_fc_info()
        self.add_power_info()
        self.add_profile_info(server)
        self.add_psu_info(server)
        self.add_registration_info(server)
        self.add_setting_id()
        self.add_storage_info(server)
        self.add_thermal_info()
        self.add_workflow_info()
        self.add_tpm_info()
        self.add_flags()

        self.log.set_log(
            'server_info.%s' % (server['Moid']),
            self.server_info,
            json_conversion=True
        )

        self.set_server_info_cache()

        return self.server_info
