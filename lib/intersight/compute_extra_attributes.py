import time

from lib import info_helper

from lib.intersight import cache as intersight_cache
from lib.intersight.adapter_unit import main as adapter_unit
from lib.intersight.adapter_ext_eth_interface import main as adapter_ext_eth_interface
from lib.intersight.adapter_host_eth_interface import main as adapter_host_eth_interface
from lib.intersight.adapter_host_fc_interface import main as adapter_host_fc_interface
from lib.intersight.asset_device_registration import main as asset_device_registration
from lib.intersight.asset_device_contract_information import main as asset_device_contract_information
from lib.intersight.bios_boot_mode import main as bios_boot_mode
from lib.intersight.boot_cdd_device import main as boot_cdd_device
from lib.intersight.boot_device_boot_mode import main as boot_device_boot_mode
from lib.intersight.boot_device_boot_security import main as boot_device_boot_security
from lib.intersight.boot_hdd_device import main as boot_hdd_device
from lib.intersight.boot_iscsi_device import main as boot_iscsi_device
from lib.intersight.boot_nvme_device import main as boot_nvme_device
from lib.intersight.boot_pxe_device import main as boot_pxe_device
from lib.intersight.boot_san_device import main as boot_san_device
from lib.intersight.boot_sd_device import main as boot_sd_device
from lib.intersight.boot_uefi_device import main as boot_uefi_device
from lib.intersight.boot_usb_device import main as boot_usb_device
from lib.intersight.boot_vmedia_device import main as boot_vmedia_device
from lib.intersight.cond_alarm import main as cond_alarm
from lib.intersight.cond_hclstatus import main as cond_hclstatus
from lib.intersight.cond_hclstatus_detail import main as cond_hclstatus_detail
from lib.intersight.compute_board import main as compute_board
from lib.intersight.compute_server_setting import main as compute_server_setting
from lib.intersight.equipment_fan_module import main as equipment_fan_module
from lib.intersight.equipment_fan import main as equipment_fan
from lib.intersight.equipment_led import main as equipment_led
from lib.intersight.equipment_psu import main as equipment_psu
from lib.intersight.equipment_tpm import main as equipment_tpm
from lib.intersight.graphics_card import main as graphics_card
from lib.intersight.graphics_controller import main as graphics_controller
from lib.intersight.management_interface import main as management_interface
from lib.intersight.memory_unit import main as memory_unit
from lib.intersight.pci_device import main as pci_device
from lib.intersight.pci_node import main as pci_node
from lib.intersight.processor_unit import main as processor_unit
from lib.intersight.running_firmware import main as running_firmware
from lib.intersight.search_item import main as search_item
from lib.intersight.server_profile import main as server_profile
from lib.intersight.storage_disk_group import main as storage_disk_group
from lib.intersight.storage_physical_disk import main as storage_physical_disk
from lib.intersight.storage_physical_disk_usage import main as storage_physical_disk_usage
from lib.intersight.storage_virtual_drive import main as storage_virtual_drive
from lib.intersight.storage_controller import main as storage_controller
from lib.intersight.tam_advisory_definition import main as tam_advisory_definition
from lib.intersight.tam_advisory_instance import main as tam_advisory_instance
from lib.intersight.tam_security_advisory import main as tam_security_advisory
from lib.intersight.workflow import main as workflow

from lib.redfish import endpoint_settings as redfish_endpoint_settings
from lib.ucsm import endpoint_settings as ucsm_endpoint_settings
from lib import my_servers_helper
from lib import log_helper


class ComputeExtraAttributes():
    """Class for rack/blade compute object extra attributes
    """
    def __init__(self, iaccount, log_id=None):
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.my_servers_handler = my_servers_helper.MyServers()
        self.my_servers_serials = self.my_servers_handler.get_serials()
        self.info_handler = info_helper.InfoHelper(
            log_id=log_id
        )

        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )

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
        self.equipment_tpm_handler = equipment_tpm.EquipmentTpm(
            iaccount,
            log_id=log_id
        )
        self.fan_module_handler = equipment_fan_module.EquipmentFanModule(
            iaccount,
            log_id=log_id
        )
        self.fan_handler = equipment_fan.EquipmentFan(
            iaccount,
            log_id=log_id
        )
        self.graphics_card_handler = graphics_card.GraphicsCard(
            iaccount,
            log_id=log_id
        )
        self.graphics_controller_handler = graphics_controller.GraphicsController(
            iaccount,
            log_id=log_id
        )
        self.locator_handler = equipment_led.EquipmentLed(
            iaccount,
            log_id=log_id
        )
        self.management_interface_handler = management_interface.ManagementInterface(
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
        self.pci_node_handler = pci_node.PciNode(
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
        self.storage_disk_group_handler = storage_disk_group.StorageDiskGroup(
            iaccount,
            log_id=log_id
        )
        self.storage_physical_disk_handler = storage_physical_disk.StoragePhysicalDisk(
            iaccount,
            log_id=log_id
        )
        self.storage_physical_disk_usage_handler = storage_physical_disk_usage.StoragePhysicalDiskUsage(
            iaccount,
            log_id=log_id
        )
        self.storage_virtual_drive_handler = storage_virtual_drive.StorageVirtualDrive(
            iaccount,
            log_id=log_id
        )
        self.tam_advisory_definition_handler = tam_advisory_definition.TamAdvisoryDefinition(
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
        self.workflow_handler = workflow.Workflow(
            iaccount,
            log_id=log_id
        )
        self.redfish_endpoint_settings_handler = redfish_endpoint_settings.RedfishEndpointSettings(
            log_id=log_id
        )
        self.ucsm_endpoint_settings_handler = ucsm_endpoint_settings.UcsmEndpointSettings(
            log_id=log_id
        )

        self.server_info = {}

    def add_advisory_info(self):
        self.server_info['AdvisorySummary'] = {}
        self.server_info['AdvisorySummary']['__Output'] = {}
        self.server_info['AdvisorySummary']['__Output']['High'] = 'Red'
        self.server_info['AdvisorySummary']['__Output']['Info'] = 'Blue'
        self.server_info['AdvisorySummary']['High'] = 0
        self.server_info['AdvisorySummary']['Info'] = 0

        self.server_info['AdvisoryInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'advisory',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_advisory_info',
                'No cache'
            )
            return

        security_advisories = self.cache_handler.get_intersight_cache_entry(
            'advisory_security',
            check_ttl=False
        )
        if security_advisories is None:
            self.log.error(
                'add_advisory_info',
                'No main security advisory cache'
            )
            return

        advisory_definitions = self.cache_handler.get_intersight_cache_entry(
            'advisory_definition',
            check_ttl=False
        )
        if advisory_definitions is None:
            self.log.error(
                'add_advisory_info',
                'No main advisory definitions cache'
            )
            return

        for managed_object in managed_objects:
            if managed_object['Advisory']['ObjectType'] == 'tam.SecurityAdvisory':
                for advisory_mo in security_advisories:
                    if managed_object['Advisory']['Moid'] == advisory_mo['Moid']:
                        advisory_info = self.tam_security_advisory_handler.get_info(
                            advisory_mo
                        )
                        self.server_info['AdvisoryInfo'].append(
                            advisory_info
                        )
                        if advisory_info['Severity'] == 'high':
                            self.server_info['AdvisorySummary']['High'] = self.server_info['AdvisorySummary']['High'] + 1
                        else:
                            self.server_info['AdvisorySummary']['Info'] = self.server_info['AdvisorySummary']['Info'] + 1

                        break

                continue

            if managed_object['Advisory']['ObjectType'] == 'tam.AdvisoryDefinition':
                for advisory_mo in advisory_definitions:
                    if managed_object['Advisory']['Moid'] == advisory_mo['Moid']:
                        advisory_info = self.tam_advisory_definition_handler.get_info(
                            advisory_mo
                        )
                        self.server_info['AdvisoryInfo'].append(
                            advisory_info
                        )
                        if advisory_info['Severity'] == 'high':
                            self.server_info['AdvisorySummary']['High'] = self.server_info['AdvisorySummary']['High'] + 1
                        else:
                            self.server_info['AdvisorySummary']['Info'] = self.server_info['AdvisorySummary']['Info'] + 1

                        break

                continue

            self.log.error(
                'add_advisory_info',
                'Unsupported advisory: %s' % (managed_object['Advisory']['ObjectType'])
            )

    def add_alarm_info(self, include_cleared=False, include_acknowledged=False):
        self.server_info['AlarmInfo'] = []
        self.server_info['AlarmExcludedInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'alarm',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_alarm_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        critical_count = 0
        warning_count = 0
        info_count = 0

        for managed_object in managed_objects:
            alarm_info = self.cond_alarm_handler.get_info(
                managed_object
            )
            if alarm_info['Severity'] == 'Cleared' and not include_cleared:
                continue

            if alarm_info['Acknowledge'] == 'Acknowledge' and not include_acknowledged:
                continue

            if alarm_info['AncestorMoId'] != self.server_info['Moid']:
                continue

            if alarm_info['Severity'] == 'Critical':
                critical_count = critical_count + 1

            if alarm_info['Severity'] == 'Warning':
                warning_count = warning_count + 1

            if alarm_info['Severity'] == 'Info':
                info_count = info_count + 1

            self.server_info['AlarmInfo'].append(
                alarm_info
            )

        if critical_count != self.server_info['AlarmSummary']['Critical']:
            self.log.error(
                'add_alarm_info',
                'Critical alarms do not match count: %s' % (self.server_info['Moid'])
            )

        if warning_count != self.server_info['AlarmSummary']['Warning']:
            self.log.error(
                'add_alarm_info',
                'Warning alarms do not match count: %s' % (self.server_info['Moid'])
            )

        if info_count != self.server_info['AlarmSummary']['Info']:
            self.log.error(
                'add_alarm_info',
                'Info alarms do not match count: %s' % (self.server_info['Moid'])
            )

    def add_cimc_info(self):
        self.server_info['CimcInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'cimc',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_cimc_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.server_info['CimcInfo'].append(
                    self.management_interface_handler.get_info(
                        managed_object
                    )
                )

    def add_adapters_info(self):
        self.server_info['AdaptersInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'adapter',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_adapters_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.server_info['AdaptersInfo'].append(
                    self.adapter_unit_handler.get_info(
                        managed_object
                    )
                )
        self.server_info['AdaptersInfo'] = sorted(
            self.server_info['AdaptersInfo'],
            key=lambda i: i['Name']
        )

        # create inventory if not yet created via associated pci device

        for adapter_info in self.server_info['AdaptersInfo']:
            found = False
            for inventory_info in self.server_info['Inventory']:
                if inventory_info['Type'] == 'PCI Adapter':
                    if inventory_info['Name'] == 'PCI Slot %s' % (adapter_info['PciSlot']):
                        found = True
                        break

            if not found:
                # assume it is mlom or mezz

                inventory_info = {}
                inventory_info['Order'] = 10
                inventory_info['SubOrder'] = 0
                inventory_info['Type'] = 'PCI Adapter'
                if adapter_info['PciSlot'].lower() in ['n/a', 'unknown', 'none', '']:
                    inventory_info['Name'] = 'PCI Slot MLOM'
                else:
                    inventory_info['Name'] = 'PCI Slot %s' % (adapter_info['PciSlot'])

                for key in ['Model', 'Vendor', 'Serial']:
                    inventory_info[key] = ''
                    if key in adapter_info:
                        inventory_info[key] = adapter_info[key]
                        if inventory_info[key] is None:
                            inventory_info[key] = ''

                inventory_info['Pid'] = inventory_info['Model']
                inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                inventory_info['ServerType'] = self.server_info['Type']
                inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                self.server_info['Inventory'].append(
                    inventory_info
                )

        # sync adapter to inventory

        for adapter_info in self.server_info['AdaptersInfo']:
            for inventory_info in self.server_info['Inventory']:
                if inventory_info['Type'] == 'PCI Adapter':
                    if inventory_info['Name'] == 'PCI Slot %s' % (adapter_info['PciSlot']):
                        for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                            if inventory_info[key] is None or len(inventory_info[key]) == 0:
                                if key in adapter_info:
                                    inventory_info[key] = adapter_info[key]
                                    if inventory_info[key] is None:
                                        inventory_info[key] = ''

        # sync inventory to adapter

        for adapter_info in self.server_info['AdaptersInfo']:
            for inventory_info in self.server_info['Inventory']:
                if inventory_info['Type'] == 'PCI Adapter':
                    if inventory_info['Name'] == 'PCI Slot %s' % (adapter_info['PciSlot']):
                        adapter_info['Pid'] = inventory_info['Pid']

    def add_board_info(self):
        self.server_info['BoardInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'board',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_board_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log.error(
                'add_board_info',
                'Multiple board info objects found'
            )
            return

        self.server_info['BoardInfo'] = self.compute_board_handler.get_info(
            managed_objects[0]
        )

        inventory_info = {}
        inventory_info['Order'] = 2
        inventory_info['SubOrder'] = 1
        inventory_info['Type'] = 'Board'
        inventory_info['Name'] = 'Mother Board'
        for key in ['Model', 'Vendor', 'Serial', 'Pid']:
            inventory_info[key] = ''
            if key in self.server_info['BoardInfo']:
                inventory_info[key] = self.server_info['BoardInfo'][key]
                if inventory_info[key] is None:
                    inventory_info[key] = ''

        if len(inventory_info['Pid']) == 0:
            inventory_info['Pid'] = inventory_info['Model']

        inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
        inventory_info['ServerType'] = self.server_info['Type']
        inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
        inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

        self.server_info['Inventory'].append(
            inventory_info
        )

    def add_boot_info(self):
        self.server_info['BootInfo'] = {}
        self.server_info['BootInfo']['ConfiguredBootMode'] = None
        self.server_info['BootInfo']['ActualBootMode'] = None
        self.server_info['BootInfo']['SecureBoot'] = None
        self.server_info['BootInfo']['Order'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_mode',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot mode cache'
            )
            return

        if len(managed_objects) == 0:
            self.log.debug(
                'add_boot_info',
                'No boot info: %s' % (self.server_info['Moid'])
            )
            return

        if len(managed_objects) > 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of boot device boot mode objects: %s' % (self.server_info['Moid'])
            )
            self.log.error(
                'add_boot_info',
                managed_objects
            )
            return

        self.server_info['BootInfo']['ConfiguredBootMode'] = self.boot_device_boot_mode_handler.get_info(
            managed_objects[0]
        )['ConfiguredBootMode']

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_bios',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot bios cache'
            )
            return

        if len(managed_objects) != 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of boot bios mode objects'
            )
            return

        self.server_info['BootInfo']['ActualBootMode'] = self.bios_boot_mode_handler.get_info(
            managed_objects[0]
        )['ActualBootMode']

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_security',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot security cache'
            )
            return

        if len(managed_objects) != 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of boot security mode objects'
            )
            return

        self.server_info['BootInfo']['SecureBoot'] = self.boot_device_boot_security_handler.get_info(
            managed_objects[0]
        )['SecureBoot']

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_cdd',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot cdd cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_cdd_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_hdd',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot hdd cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_hdd_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_iscsi',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot iscsi cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_iscsi_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_nvme',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot nvme cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_nvme_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_pxe',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot pxe cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_pxe_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_san',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot san cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_san_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_sd',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot sd cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_sd_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_uefi',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot uefi cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_uefi_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_usb',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot usb cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_usb_device_handler.get_info(
                    managed_object
                )
            )

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'boot_vmedia',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_boot_info',
                'No boot vmedia cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['BootInfo']['Order'].append(
                self.boot_vmedia_device_handler.get_info(
                    managed_object
                )
            )

        self.server_info['BootInfo']['Order'] = sorted(
            self.server_info['BootInfo']['Order'],
            key=lambda i: i['Order']
        )

    def add_connector_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'connector',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_connector_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        if len(managed_objects) > 1:
            self.log.error(
                'add_connector_info',
                'Unexpected number of device connector objects: %s' % (self.server_info['Moid'])
            )
            return

        self.server_info['ConnectorInfo'] = None
        if len(managed_objects) == 1:
            self.server_info['ConnectorInfo'] = self.asset_device_registration_handler.get_info(
                managed_objects[0]
            )
            self.server_info['Connected'] = self.server_info['ConnectorInfo']['Connected']

    def add_contract_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'contract',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_contract_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        if len(managed_objects) != 1:
            self.log.error(
                'add_contract_info',
                'Unexpected number of device contract objects: %s' % (self.server_info['Moid'])
            )
            return

        self.server_info['ContractInfo'] = self.asset_device_contract_information_handler.get_info(
            managed_objects[0]
        )

    def add_cpu_info(self):
        self.server_info['CpuInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'cpu',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_cpu_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
        else:
            for managed_object in managed_objects:
                cpu_info = self.processor_unit_handler.get_processor_unit_info(
                    managed_object
                )
                if cpu_info['Presence'] == 'equipped':
                    self.server_info['CpuInfo'].append(
                        cpu_info
                    )

        self.server_info['CpuInfo'] = sorted(
            self.server_info['CpuInfo'],
            key=lambda i: i['ProcessorId']
        )

        for cpu_info in self.server_info['CpuInfo']:
            inventory_info = {}
            inventory_info['Order'] = 3
            inventory_info['SubOrder'] = cpu_info['ProcessorId']
            inventory_info['Type'] = 'CPU'
            inventory_info['Name'] = 'CPU #%s' % (cpu_info['ProcessorId'])
            for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                inventory_info[key] = ''
                if key in cpu_info:
                    inventory_info[key] = cpu_info[key]
                    if inventory_info[key] is None:
                        inventory_info[key] = ''

            inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
            inventory_info['ServerType'] = self.server_info['Type']
            inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
            inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

            self.server_info['Inventory'].append(
                inventory_info
            )

    def add_ext_eth_info(self):
        self.server_info['MacAddressInfo'] = []
        self.server_info['ExtEthInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'adapter_ext_eth_interface',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_ext_eth_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        for managed_object in managed_objects:
            interface_info = self.adapter_ext_eth_interface_handler.get_info(
                managed_object
            )

            mac_info = {}
            mac_info['InterfaceDn'] = interface_info['Dn']
            mac_info['InterfaceName'] = interface_info['Dn'].split('/')[-1]
            mac_info['MacAddress'] = interface_info['MacAddress'].lower()
            mac_info['AdapterModel'] = None
            mac_info['AdapterPciSlot'] = None

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            interface_info['AdapterModel'] = None
            interface_info['AdapterPid'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if managed_object['Moid'] in adapter_info['ExtEthIfsIds']:
                    if 'Name' in adapter_info:
                        interface_info['AdapterName'] = adapter_info['Name']
                    if 'PciSlot' in adapter_info:
                        interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                        mac_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    if 'Model' in adapter_info:
                        interface_info['AdapterModel'] = adapter_info['Model']
                        mac_info['AdapterModel'] = adapter_info['Model']
                    if 'Pid' in adapter_info:
                        interface_info['Pid'] = adapter_info['Pid']

            self.server_info['ExtEthInfo'].append(
                interface_info
            )

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

    def add_fan_module_info(self):
        if self.server_info['Type'] == 'Blade':
            return

        if self.server_info['Type'] == 'Rack':
            self.server_info['FanModuleInfo'] = []

            managed_objects = self.cache_handler.get_intersight_cache_entry(
                'fanmodule',
                subdirectory=self.server_info['Moid'],
                check_ttl=False
            )
            if managed_objects is None:
                self.log.error(
                    'add_fan_module_info',
                    'No cache: %s' % (self.server_info['Moid'])
                )
            else:
                for managed_object in managed_objects:
                    self.server_info['FanModuleInfo'].append(
                        self.fan_module_handler.get_info(
                            managed_object
                        )
                    )

            self.server_info['FanModuleInfo'] = sorted(
                self.server_info['FanModuleInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['FanModuleOn'] = 0
            for fan_module_info in self.server_info['FanModuleInfo']:
                if fan_module_info['On']:
                    self.server_info['FanModuleOn'] = self.server_info['FanModuleOn'] + 1

            self.server_info['FanModuleCount'] = len(self.server_info['FanModuleInfo'])
            self.server_info['FanModuleSummary'] = '%s/%s' % (
                self.server_info['FanModuleOn'],
                self.server_info['FanModuleCount']
            )
            self.server_info['FanModuleHealthy'] = True
            if self.server_info['FanModuleOn'] < self.server_info['FanModuleCount']:
                self.server_info['FanModuleHealthy'] = False

    def add_fan_info(self):
        if self.server_info['Type'] == 'Blade':
            return

        if self.server_info['Type'] == 'Rack':
            self.server_info['FanInfo'] = []

            managed_objects = self.cache_handler.get_intersight_cache_entry(
                'fan',
                subdirectory=self.server_info['Moid'],
                check_ttl=False
            )
            if managed_objects is None:
                self.log.error(
                    'add_fan_info',
                    'No cache: %s' % (self.server_info['Moid'])
                )
            else:
                for managed_object in managed_objects:
                    self.server_info['FanInfo'].append(
                        self.fan_handler.get_info(
                            managed_object
                        )
                    )

            self.server_info['FanInfo'] = sorted(
                self.server_info['FanInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['FanOn'] = 0
            for fan_info in self.server_info['FanInfo']:
                if fan_info['On']:
                    self.server_info['FanOn'] = self.server_info['FanOn'] + 1

            self.server_info['FanCount'] = len(self.server_info['FanInfo'])
            self.server_info['FanSummary'] = '%s/%s' % (
                self.server_info['FanOn'],
                self.server_info['FanCount']
            )
            self.server_info['FanHealthy'] = True
            if self.server_info['FanOn'] < self.server_info['FanCount']:
                self.server_info['FanHealthy'] = False

            for fan_info in self.server_info['FanInfo']:
                if fan_info['Presence'] == 'equipped':
                    inventory_info = {}
                    inventory_info['Order'] = 11
                    inventory_info['SubOrder'] = (fan_info['FanModuleId'] + 1) * 10 + fan_info['FanId']
                    inventory_info['Type'] = 'Fan'
                    inventory_info['Name'] = fan_info['Name']
                    for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                        inventory_info[key] = ''
                        if key in fan_info:
                            inventory_info[key] = fan_info[key]
                            if inventory_info[key] is None:
                                inventory_info[key] = ''

                    inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                    inventory_info['ServerType'] = self.server_info['Type']
                    inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                    inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                    self.server_info['Inventory'].append(
                        inventory_info
                    )

    def add_firmware_info(self):
        self.server_info['FirmwarewComponents'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'firmware',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_firmware_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        for managed_object in managed_objects:
            self.server_info['FirmwarewComponents'].append(
                self.running_firmware_handler.get_info(
                    managed_object
                )
            )

        self.server_info['FirmwareVersion'] = self.running_firmware_handler.get_version(
            managed_objects
        )

        self.server_info['FirmwarewComponents'] = sorted(
            self.server_info['FirmwarewComponents'],
            key=lambda i: i['Dn']
        )

    def add_flags(self, workflow_days):
        self.add_state_flag()
        self.add_management_flag()
        self.add_workflow_flag(workflow_days)

    def add_gcard_info(self):
        self.server_info['GraphicsCardInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'gcard',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is not None:
            for managed_object in managed_objects:
                gcard_info = self.graphics_card_handler.get_info(
                    managed_object
                )

                gcard_info['PciNodeSlotId'] = None
                for pci_node_info in self.server_info['PciNodesInfo']:
                    if gcard_info['PciNodeId'] == pci_node_info['Moid']:
                        gcard_info['PciNodeSlotId'] = int(pci_node_info['SlotId'])

                gcard_info['GraphicsControllersInfo'] = []
                for gcontroller_mo in managed_object['GraphicsControllers']:
                    gcontroller_info = self.graphics_controller_handler.get_info(
                        gcontroller_mo
                    )

                    for key in ['GpuId', 'FirmwareVersion', 'PartNumber', 'SlotId']:
                        gcontroller_info[key] = gcard_info[key]


                    gcard_info['GraphicsControllersInfo'].append(
                        gcontroller_info
                    )

                    self.server_info['GpuInfo'].append(
                        gcontroller_info
                    )

                gcard_info['GraphicsControllersInfo'] = sorted(
                    gcard_info['GraphicsControllersInfo'],
                    key=lambda i: i['ControllerId']
                )

                if gcard_info['Presence'] == 'equipped':
                    self.server_info['GraphicsCardInfo'].append(
                        gcard_info
                    )

        self.server_info['GraphicsCardInfo'] = sorted(
            self.server_info['GraphicsCardInfo'],
            key=lambda i: i['CardId']
        )

        for pci_node_info in self.server_info['PciNodesInfo']:
            pci_node_info['GpuInfo'] = []
            for gcard_info in self.server_info['GraphicsCardInfo']:
                if gcard_info['PciNodeId'] == pci_node_info['Moid']:
                    for gpu_info in gcard_info['GraphicsControllersInfo']:
                        pci_node_info['GpuInfo'].append(
                            gpu_info
                        )

        for gcard_info in self.server_info['GraphicsCardInfo']:
            for gpu_info in gcard_info['GraphicsControllersInfo']:
                inventory_info = {}
                inventory_info['Order'] = 4
                inventory_info['SubOrder'] = gcard_info['PciNodeSlotId'] * 10 + gpu_info['ControllerId']
                inventory_info['Type'] = 'GPU @ Pci Node'
                inventory_info['Name'] = 'GPU #%s @ Pci Node #%s' % (gpu_info['ControllerId'], gcard_info['PciNodeSlotId'])
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in gpu_info:
                        inventory_info[key] = gpu_info[key]
                        if inventory_info[key] is None:
                            inventory_info[key] = ''

                inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                inventory_info['ServerType'] = self.server_info['Type']
                inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                self.server_info['Inventory'].append(
                    inventory_info
                )

    def add_gpu_info(self):
        self.server_info['GpuInfo'] = []
        for pci_device_info in self.server_info['PciDevicesInfo']:
            if pci_device_info['Pid'] is not None and '-GPU-' in pci_device_info['Pid']:
                self.server_info['GpuInfo'].append(
                    pci_device_info
                )

        for gpu_info in self.server_info['GpuInfo']:
            inventory_info = {}
            inventory_info['Order'] = 4
            inventory_info['SubOrder'] = gpu_info['SlotId']
            inventory_info['Type'] = 'GPU'
            inventory_info['Name'] = 'GPU #%s' % (gpu_info['SlotId'])
            for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                inventory_info[key] = ''
                if key in gpu_info:
                    inventory_info[key] = gpu_info[key]
                    if inventory_info[key] is None:
                        inventory_info[key] = ''

            inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
            inventory_info['ServerType'] = self.server_info['Type']
            inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
            inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

            self.server_info['Inventory'].append(
                inventory_info
            )

    def add_group_info(self):
        self.server_info['Groups'] = ''
        if self.my_servers_serials is not None:
            if self.server_info['Serial'] in self.my_servers_serials:
                self.server_info['Groups'] = ','.join(
                    self.my_servers_serials[self.server_info['Serial']]
                )

    def add_hcl_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'hcl',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_hcl_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        if len(managed_objects) == 0:
            self.server_info['HclInfo'] = None
            return

        if len(managed_objects) > 1:
            self.log.error(
                'add_hcl_info',
                'Multiple hcl info objects found: %s' % (self.server_info['Moid'])
            )
            return

        self.server_info['HclInfo'] = self.cond_hclstatus_handler.get_info(
            managed_objects[0]
        )
        self.server_info['HclInfo']['Details'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'hcl_detail',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_hcl_info',
                'No hcl detail cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['HclInfo']['Details'].append(
                self.cond_hclstatus_detail_handler.get_info(
                    managed_object
                )
            )

        return

    def add_health_info(self, server_mo):
        self.server_info['AlarmSummary'] = {}
        self.server_info['AlarmSummary']['__Output'] = {}
        self.server_info['AlarmSummary']['__Output']['Critical'] = 'Red'
        self.server_info['AlarmSummary']['__Output']['Warning'] = 'Yellow'
        self.server_info['AlarmSummary']['__Output']['Info'] = 'Blue'
        self.server_info['AlarmSummary']['__Output']['Cleared'] = 'Green'

        for key in ['Critical', 'Warning', 'Info', 'Cleared']:
            if key in server_mo['AlarmSummary']:
                self.server_info['AlarmSummary'][key] = server_mo['AlarmSummary'][key]

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

    def add_host_eth_info(self):
        self.server_info['HostEthInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'adapter_host_eth_interface',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_host_eth_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        for managed_object in managed_objects:
            interface_info = self.adapter_host_eth_interface_handler.get_info(
                managed_object
            )

            mac_info = {}
            mac_info['InterfaceDn'] = interface_info['Dn']
            mac_info['InterfaceName'] = interface_info['Dn'].split('/')[-1]
            mac_info['MacAddress'] = interface_info['MacAddress'].lower()
            mac_info['AdapterModel'] = None
            mac_info['AdapterPciSlot'] = None

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            interface_info['AdapterModel'] = None
            interface_info['AdapterPid'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if managed_object['Moid'] in adapter_info['HostEthIfsIds']:
                    if 'Name' in adapter_info:
                        interface_info['AdapterName'] = adapter_info['Name']
                    if 'PciSlot' in adapter_info:
                        interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                        mac_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    if 'Model' in adapter_info:
                        interface_info['AdapterModel'] = adapter_info['Model']
                        mac_info['AdapterModel'] = adapter_info['Model']
                    if 'Pid' in adapter_info:
                        interface_info['Pid'] = adapter_info['Pid']

            self.server_info['HostEthInfo'].append(
                interface_info
            )

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
        self.server_info['HostFcInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'adapter_host_fc_interface',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_host_fc_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
            return

        for managed_object in managed_objects:
            interface_info = self.adapter_host_fc_interface_handler.get_info(
                managed_object
            )

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            interface_info['AdapterModel'] = None
            interface_info['AdapterPid'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if managed_object['Moid'] in adapter_info['HostFcIfsIds']:
                    if 'Name' in adapter_info:
                        interface_info['AdapterName'] = adapter_info['Name']
                    if 'PciSlot' in adapter_info:
                        interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    if 'Model' in adapter_info:
                        interface_info['AdapterModel'] = adapter_info['Model']
                    if 'Pid' in adapter_info:
                        interface_info['Pid'] = adapter_info['Pid']

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

    def add_kvm_info(self, server_mo):
        self.server_info['KvmInfo'] = {}
        self.server_info['KvmInfo']['KvmIpAddresses'] = server_mo['KvmIpAddresses']
        self.server_info['KvmInfo']['KvmServerStateEnabled'] = server_mo['KvmServerStateEnabled']
        self.server_info['KvmInfo']['KvmVendor'] = server_mo['KvmVendor']
        self.server_info['KvmInfo']['TunneledKvm'] = server_mo['TunneledKvm']

    def add_license_info(self, server_mo):
        for tag in server_mo['Tags']:
            if tag['Key'] == 'Intersight.LicenseTier':
                self.server_info['LicenseInfo'] = {}
                self.server_info['LicenseInfo']['Tier'] = tag['Value']

    def add_tags_info(self, server_mo):
        self.server_info['Tags'] = []
        for tag in server_mo['Tags']:
            if tag['Key'] == 'Intersight.LicenseTier':
                continue
            self.server_info['Tags'].append(
                tag
            )

        self.server_info['Tags'] = sorted(
            self.server_info['Tags'],
            key=lambda i: (
                i['Key'].lower(),
                i['Value'].lower()
            )
        )

    def add_locator_info(self, server_mo):
        self.server_info['LocatorLedOn'] = self.locator_handler.is_locator_led_on(
            server_mo['LocatorLed']
        )

    def get_management_ip(self, server_mo):
        if 'KvmIpAddresses' in server_mo:
            for kvm_ip in server_mo['KvmIpAddresses']:
                if kvm_ip['ClassId'] == 'compute.IpAddress':
                    return kvm_ip['Address']
        return None

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

    def add_memory_info(self):
        self.server_info['MemoryInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'memory',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_memory_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.server_info['MemoryInfo'].append(
                    self.memory_unit_handler.get_memory_unit_info(
                        managed_object
                    )
                )

        self.server_info['MemoryInfo'] = sorted(
            self.server_info['MemoryInfo'],
            key=lambda i: i['MemoryId']
        )

        for memory_info in self.server_info['MemoryInfo']:
            if memory_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 5
                inventory_info['SubOrder'] = memory_info['MemoryId']
                inventory_info['Type'] = 'Memory'
                inventory_info['Name'] = 'Memory #%s' % (memory_info['MemoryId'])
                for key in ['Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in memory_info:
                        inventory_info[key] = memory_info[key]
                        if inventory_info[key] is None:
                            inventory_info[key] = ''

                if len(memory_info['Description']) > 0:
                    inventory_info['Model'] = '%s (%s)' % (
                        memory_info['Description'],
                        memory_info['Model'].strip()
                    )
                else:
                    inventory_info['Model'] = memory_info['Model'].strip()

                inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                inventory_info['ServerType'] = self.server_info['Type']
                inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                self.server_info['Inventory'].append(
                    inventory_info
                )

    def add_pci_info(self):
        self.server_info['PciDevicesInfo'] = []
        self.server_info['PciModels'] = []
        self.server_info['PciSearch'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'pci',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_pci_info',
                'No cache: %s' % (self.server_info['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.server_info['PciDevicesInfo'].append(
                    self.pci_handler.get_info(
                        managed_object
                    )
                )

                model = self.pci_handler.get_model(
                    managed_object
                )
                if model is not None:
                    if model not in self.server_info['PciSearch']:
                        self.server_info['PciSearch'].append(
                            model
                        )

                pid = self.pci_handler.get_pid(
                    managed_object
                )
                if pid is not None:
                    if pid not in self.server_info['PciSearch']:
                        self.server_info['PciSearch'].append(
                            pid
                        )

                    if pid not in self.server_info['PciModels']:
                        self.server_info['PciModels'].append(
                            pid
                        )

                if pid is None and model is not None:
                    if model not in self.server_info['PciModels']:
                        self.server_info['PciModels'].append(
                            model
                        )

        self.server_info['PciDevicesInfo'] = sorted(
            self.server_info['PciDevicesInfo'],
            key=lambda i: i['Dn']
        )

        for pci_info in self.server_info['PciDevicesInfo']:
            inventory_info = {}
            inventory_info['Order'] = 8
            inventory_info['SubOrder'] = pci_info['SlotId']
            inventory_info['Type'] = 'PCI Adapter'
            inventory_info['Name'] = 'PCI Slot %s' % (pci_info['SlotId'])
            for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                inventory_info[key] = ''
                if key in pci_info:
                    inventory_info[key] = pci_info[key]
                    if inventory_info[key] is None:
                        inventory_info[key] = ''

            inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
            inventory_info['ServerType'] = self.server_info['Type']
            inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
            inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

            self.server_info['Inventory'].append(
                inventory_info
            )

    def add_pci_node_info(self):
        self.server_info['PciNodesInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'pci_node',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            return

        for managed_object in managed_objects:
            pci_node_info = self.pci_node_handler.get_info(
                managed_object
            )

            self.server_info['PciNodesInfo'].append(
                pci_node_info
            )

            if pci_node_info['Model'] not in self.server_info['PciModels']:
                self.server_info['PciModels'].append(
                    pci_node_info['Model']
                )

            if pci_node_info['Model'] not in self.server_info['PciSearch']:
                self.server_info['PciSearch'].append(
                    pci_node_info['Model']
                )

        for pci_node_info in self.server_info['PciNodesInfo']:
            inventory_info = {}
            inventory_info['Order'] = 9
            inventory_info['SubOrder'] = pci_node_info['SlotId']
            inventory_info['Type'] = 'PCI Node'
            inventory_info['Name'] = 'Slot %s' % (pci_node_info['SlotId'])
            for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                inventory_info[key] = ''
                if key in pci_node_info:
                    inventory_info[key] = pci_node_info[key]
                    if inventory_info[key] is None:
                        inventory_info[key] = ''

            inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
            inventory_info['ServerType'] = self.server_info['Type']
            inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
            inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

            self.server_info['Inventory'].append(
                inventory_info
            )

    def add_pci_node_gpu_info(self):
        for pci_node_info in self.server_info['PciNodesInfo']:
            pci_node_info['NumGpus'] = 0

            for gcard_moid in pci_node_info['GraphicsCardsMoids']:
                for gcard_info in self.server_info['GraphicsCardInfo']:
                    if gcard_info['Moid'] == gcard_moid:
                        pci_node_info['NumGpus'] = pci_node_info['NumGpus'] + int(gcard_info['NumGpus'])

    def add_power_info(self):
        self.server_info['Power'] = self.cache_handler.get_intersight_cache_entry(
            'power',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if self.server_info['Power'] is None:
            self.log.error(
                'add_power_info',
                'No cache: %s' % (self.server_info['Moid'])
            )

    def add_profile_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'profile',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_profile_info',
                'No cache: %s' % (self.server_info['Moid'])
            )

        if len(managed_objects) == 0:
            self.server_info['ProfileInfo'] = None
            return

        if len(managed_objects) > 1:
            self.log.error(
                'add_profile_info',
                'Unexpected count of profile objects: %s' % (self.server_info['Moid'])
            )
            return

        self.server_info['ProfileInfo'] = self.server_profile_handler.get_info(
            managed_objects[0]
        )

        self.search_item_handler.set_get_filter(
            "IndexMotypes eq 'policy.AbstractPolicy' and Profiles/any(a:a/Moid eq '%s')" % (self.server_info['ProfileInfo']['Moid'])
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

        return

    def add_psu_info(self, server_mo, imc_enabled):
        if self.server_info['Type'] == 'Blade':
            return

        if self.server_info['Type'] == 'Rack':
            self.server_info['PsuInfo'] = []

            managed_objects = self.cache_handler.get_intersight_cache_entry(
                'psu',
                subdirectory=self.server_info['Moid'],
                check_ttl=False
            )
            if managed_objects is None:
                self.log.error(
                    'add_psu_info',
                    'No cache: %s' % (server_mo['Moid'])
                )
            else:
                for managed_object in managed_objects:
                    self.server_info['PsuInfo'].append(
                        self.psu_handler.get_info(
                            managed_object
                        )
                    )

            self.server_info['PsuInfo'] = sorted(
                self.server_info['PsuInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['PsuOn'] = 0
            for psu_info in self.server_info['PsuInfo']:
                if psu_info['On']:
                    self.server_info['PsuOn'] = self.server_info['PsuOn'] + 1

            self.server_info['PsuCount'] = len(server_mo['Psus'])
            self.server_info['PsuSummary'] = '%s/%s' % (
                self.server_info['PsuOn'],
                self.server_info['PsuCount']
            )
            self.server_info['PsuHealthy'] = True
            if self.server_info['PsuOn'] < self.server_info['PsuCount']:
                self.server_info['PsuHealthy'] = False

            for psu_info in self.server_info['PsuInfo']:
                if psu_info['On']:
                    inventory_info = {}
                    inventory_info['Order'] = 12
                    inventory_info['SubOrder'] = psu_info['Id']
                    inventory_info['Type'] = 'PSU'
                    inventory_info['Id'] = psu_info['Id']
                    inventory_info['Name'] = 'PSU #%s' % (psu_info['Id'])
                    for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                        inventory_info[key] = ''
                        if key in psu_info:
                            inventory_info[key] = psu_info[key]
                            if inventory_info[key] is None:
                                inventory_info[key] = ''

                    inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                    inventory_info['ServerType'] = self.server_info['Type']
                    inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                    inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                    self.server_info['Inventory'].append(
                        inventory_info
                    )

            if imc_enabled:
                managed_objects = self.cache_handler.get_intersight_cache_entry(
                    'psu-imc',
                    subdirectory=self.server_info['Moid'],
                    check_ttl=False
                )
                if managed_objects is not None:
                    for managed_object in managed_objects:
                        for inventory_info in self.server_info['Inventory']:
                            if inventory_info['Type'] == 'PSU':
                                if managed_object['Name'] == 'PSU%s' % (inventory_info['Id']):
                                    inventory_info['Pid'] = managed_object['Product ID']

    def add_setting_id(self):
        self.server_info['ServerSettingId'] = self.compute_server_setting_handler.get_id_by_device_moid(
            self.server_info['DeviceMoId']
        )

    def add_state_flag(self):
        color = ':'
        if self.server_info['OperPowerState'] == 'on':
            state = 'P+'
            color = '%sGG' % (color)
        else:
            state = 'P-'
            color = '%sRR' % (color)

        if self.server_info['AlarmSummary']['Warning'] == 0 and self.server_info['AlarmSummary']['Critical'] == 0 and self.server_info['AlarmSummary']['Info'] == 0:
            alarm_state = 'H'
            alarm_color = 'G'.rjust(len(alarm_state), 'G')
            state = '%s %s' % (state, alarm_state)
            color = '%s.%s' % (color, alarm_color)
        if self.server_info['AlarmSummary']['Warning'] == 0 and self.server_info['AlarmSummary']['Critical'] == 0 and self.server_info['AlarmSummary']['Info'] > 0:
            alarm_state = 'I(%s)' % (self.server_info['AlarmSummary']['Info'])
            alarm_color = 'B'.rjust(len(alarm_state), 'B')
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

        if 'LocatorLedOn' in self.server_info:
            if self.server_info['LocatorLedOn']:
                state = '%s L' % (state)
                color = '%s..' % (color)

        self.server_info['FlagState'] = state
        self.server_info['__Output']['FlagState'] = color

    def add_storage_virtual_disk_info(self, virtual_drives_mo, physical_disks_usage_mo, disk_groups_mo):
        self.server_info['VirtualDisks'] = self.storage_virtual_drive_handler.get_info(
            virtual_drives_mo,
            storage_controllers_info=self.server_info['StorageControllerInfo']
        )

        for virtual_disk_info in self.server_info['VirtualDisks']:
            virtual_disk_info['PhysicalDiskIds'] = []
            virtual_disk_info['PhysicalDiskMoids'] = []

            if virtual_disk_info['PhysicalDiskCount'] > 0:
                if physical_disks_usage_mo is not None:
                    for physical_disk_usage_mo in physical_disks_usage_mo:
                        if physical_disk_usage_mo['StorageVirtualDrive']['Moid'] == virtual_disk_info['Moid']:
                            virtual_disk_info['PhysicalDiskIds'].append(
                                physical_disk_usage_mo['PhysicalDrive']
                            )

            if virtual_disk_info['PhysicalDiskCount'] == 0:
                if disk_groups_mo is not None:
                    for disk_group_mo in disk_groups_mo:
                        for disk_group_vd_mo in disk_group_mo['VirtualDrives']:
                            if disk_group_vd_mo['Moid'] == virtual_disk_info['Moid']:
                                for disk_group_span_mo in disk_group_mo['Spans']:
                                    for physical_disk_mo in disk_group_span_mo['PhysicalDisks']:
                                        virtual_disk_info['PhysicalDiskMoids'].append(
                                            physical_disk_mo['Moid']
                                        )
                                        virtual_disk_info['PhysicalDiskCount'] = virtual_disk_info['PhysicalDiskCount'] + 1

        self.server_info['VirtualDiskCount'] = len(
            self.server_info['VirtualDisks']
        )

        self.server_info['VirtualDiskCapacity'] = self.storage_virtual_drive_handler.get_virtual_drives_size(
            self.server_info['VirtualDisks']
        )
        self.server_info['VirtualDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['VirtualDiskCapacity']
        )

    def add_storage_physical_disk_info(self, physical_disks_mo):
        self.server_info['PhysicalDiskInfo'] = self.storage_physical_disk_handler.get_info(
            physical_disks_mo,
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllerInfo']
        )
        self.server_info['PhysicalDiskCount'] = len(
            self.server_info['PhysicalDiskInfo']
        )
        self.server_info['PhysicalDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            self.server_info['PhysicalDiskInfo']
        )
        self.server_info['PhysicalDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['PhysicalDiskCapacity']
        )

        for disk_info in self.server_info['PhysicalDiskInfo']:
            if disk_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 7
                inventory_info['SubOrder'] = disk_info['DiskId']
                inventory_info['Type'] = 'Disk'
                inventory_info['Name'] = 'Disk #%s' % (disk_info['DiskId'])
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in disk_info:
                        inventory_info[key] = disk_info[key]
                        if inventory_info[key] is None:
                            inventory_info[key] = ''

                inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                inventory_info['ServerType'] = self.server_info['Type']
                inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                self.server_info['Inventory'].append(
                    inventory_info
                )

    def add_storage_info(self, server):
        start_time = int(time.time() * 1000)

        storage_controllers_mo = self.cache_handler.get_intersight_cache_entry(
            'storage_controller',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if storage_controllers_mo is None:
            self.log.error(
                'add_storage_info',
                'No storage controller cache: %s' % (self.server_info['Moid'])
            )
            return

        virtual_drives_mo = self.cache_handler.get_intersight_cache_entry(
            'virtual_drive',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if virtual_drives_mo is None:
            self.log.error(
                'add_storage_info',
                'No virtual drive cache: %s' % (self.server_info['Moid'])
            )
            return

        physical_disks_mo = self.cache_handler.get_intersight_cache_entry(
            'physical_disk',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if physical_disks_mo is None:
            self.log.error(
                'add_storage_info',
                'No physical disk cache: %s' % (self.server_info['Moid'])
            )
            return

        physical_disks_usage_mo = self.cache_handler.get_intersight_cache_entry(
            'physical_disk_usage',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if physical_disks_usage_mo is None:
            self.log.error(
                'add_storage_info',
                'No physical disk usage cache: %s' % (self.server_info['Moid'])
            )
            return

        disk_groups_mo = self.cache_handler.get_intersight_cache_entry(
            'disk_group',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if disk_groups_mo is None:
            self.log.error(
                'add_storage_info',
                'No disk group cache: %s' % (self.server_info['Moid'])
            )
            return

        self.log.debug(
            'add_storage_info',
            'Storage (disk): %s' % (int(time.time() * 1000) - start_time)
        )

        if self.server_info['Type'] == 'Rack':
            self.server_info['StorageControllerInfo'] = self.storage_controller_handler.get_board_info(
                storage_controllers_mo,
                physical_disks_mo=physical_disks_mo
            )

        if self.server_info['Type'] == 'Blade':
            self.server_info['StorageControllerInfo'] = self.storage_controller_handler.get_blade_info(
                controllers=storage_controllers_mo
            )

        for controller_info in self.server_info['StorageControllerInfo']:
            if controller_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 6
                inventory_info['SubOrder'] = controller_info['PciSlot']
                inventory_info['Type'] = 'Storage Controller'
                inventory_info['Name'] = 'Storage Controller #%s' % (controller_info['PciSlot'])
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in controller_info:
                        inventory_info[key] = controller_info[key]
                        if inventory_info[key] is None:
                            inventory_info[key] = ''

                for server_inventory_info in self.server_info['Inventory']:
                    if server_inventory_info['Type'] == 'PCI Adapter':
                        if server_inventory_info['SubOrder'] == controller_info['PciSlot']:
                            if len(server_inventory_info['Pid']) > 0 and len(inventory_info['Pid']) == 0:
                                inventory_info['Pid'] = server_inventory_info['Pid']

                            if len(server_inventory_info['Pid']) == 0 and len(inventory_info['Pid']) > 0:
                                server_inventory_info['Pid'] = inventory_info['Pid']

                            if len(server_inventory_info['Serial']) > 0 and len(inventory_info['Serial']) == 0:
                                inventory_info['Serial'] = server_inventory_info['Serial']

                            if len(server_inventory_info['Serial']) == 0 and len(inventory_info['Serial']) > 0:
                                server_inventory_info['Serial'] = inventory_info['Serial']

                inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
                inventory_info['ServerType'] = self.server_info['Type']
                inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
                inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

                self.server_info['Inventory'].append(
                    inventory_info
                )

        if self.server_info['StorageControllerInfo'] is None:
            self.server_info['StorageControllerCount'] = 0
        else:
            self.server_info['StorageControllerCount'] = len(self.server_info['StorageControllerInfo'])

        self.add_storage_virtual_disk_info(virtual_drives_mo, physical_disks_usage_mo, disk_groups_mo)
        self.add_storage_physical_disk_info(physical_disks_mo)

        self.server_info['StorageDrives'] = '%sC %sD %sVD' % (
            self.server_info['StorageControllerCount'],
            self.server_info['PhysicalDiskCount'],
            self.server_info['VirtualDiskCount']
        )

        self.server_info['StorageCapacity'] = 'R %s , VD %s' % (
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

        self.server_info['StorageSummary'] = '%sC %sD %sVD R%s L%s' % (
            self.server_info['StorageControllerCount'],
            self.server_info['PhysicalDiskCount'],
            self.server_info['VirtualDiskCount'],
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

    def add_thermal_info(self):
        self.server_info['Thermal'] = self.cache_handler.get_intersight_cache_entry(
            'thermal',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if self.server_info['Thermal'] is None:
            self.log.error(
                'add_thermal_info',
                'No cache: %s' % (self.server_info['Moid'])
            )

    def add_tpm_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'tpm',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_tpm_info',
                'No cache'
            )
            return

        self.server_info['TpmInfo'] = []
        for managed_object in managed_objects:
            self.server_info['TpmInfo'].append(
                self.equipment_tpm_handler.get_info(
                    managed_object
                )
            )

    def add_workflow_info(self, workflow_days):
        self.server_info['Workflow'] = {}
        self.server_info['Workflow']['Days'] = int(workflow_days / 86400)
        self.server_info['Workflow']['Running'] = None
        self.server_info['Workflow']['LatestMoid'] = None
        self.server_info['Workflow']['Last'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'workflow',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_workflow_info',
                'No cache'
            )
            return

        latest_create_time = None
        for managed_object in managed_objects:
            workflow_info = self.workflow_handler.get_info(
                managed_object
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

    def add_workflow_flag(self, workflow_days):
        state = ''
        color = ':'
        if workflow_days is not None:
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

    def get_server_info(self, server_mo, settings):
        self.server_info = {}
        self.server_info['__Output'] = {}
        if 'state' not in settings:
            settings['state'] = False
        self.server_info['StateEnabled'] = settings['state']
        self.server_info['IntersightObject'] = server_mo

        imc_enabled = False
        if 'imc' in settings:
            imc_enabled = settings['imc']

        redfish_enabled = False
        if 'redfish' in settings:
            redfish_enabled = settings['redfish']

        keys = [
            'Moid',
            'Ancestors',
            'DeviceMoId',
            'Name',
            'Model',
            'Serial',
            'ManagementMode',
            'OperPowerState',
            'NumCpus',
            'NumCpuCores',
            'NumThreads',
            'AvailableMemory',
            'TotalMemory',
            'Vendor'
        ]
        for key in keys:
            self.server_info[key] = server_mo[key]

        self.server_info['Cpu'] = '%sS %sC %sT' % (
            self.server_info['NumCpus'],
            self.server_info['NumCpuCores'],
            self.server_info['NumThreads']
        )

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

        try:
            usage = int(self.server_info['UsedMemory'] * 100 / self.server_info['TotalMemory'])
            self.server_info['UsedMemoryPct'] = usage
            self.server_info['UsedMemoryPctUnit'] = '%s%%' % (usage)
        except BaseException:
            self.server_info['UsedMemoryPct'] = '--'
            self.server_info['UsedMemoryPctUnit'] = '--'

        self.server_info['ChassisMoid'] = None
        if server_mo['ObjectType'] == 'compute.RackUnit':
            self.server_info['Type'] = 'Rack'
            self.server_info['TypeModel'] = '(R) %s' % (self.server_info['Model'])

        if server_mo['ObjectType'] == 'compute.Blade':
            self.server_info['Type'] = 'Blade'
            self.server_info['TypeModel'] = '(B) %s' % (server_mo['Model'])
            self.server_info['ChassisMoid'] = server_mo['EquipmentChassis']['Moid']

        self.server_info['Connected'] = False

        self.server_info['Inventory'] = []
        inventory_info = {}
        inventory_info['Order'] = 1
        inventory_info['SubOrder'] = 1
        inventory_info['Type'] = 'Server'
        if server_mo['ObjectType'] == 'compute.RackUnit':
            inventory_info['Name'] = 'Rack Server'
        if server_mo['ObjectType'] == 'compute.Blade':
            inventory_info['Name'] = 'Blade Server'
        for key in ['Model', 'Vendor', 'Serial', 'Pid']:
            inventory_info[key] = ''
            if key in self.server_info:
                inventory_info[key] = self.server_info[key]
                if inventory_info[key] is None:
                    inventory_info[key] = ''

        if len(inventory_info['Pid']) == 0:
            inventory_info['Pid'] = inventory_info['Model']

        self.server_info['InventoryServerPid'] = inventory_info['Pid']
        self.server_info['InventoryServerSerial'] = inventory_info['Serial']

        inventory_info['ChassisMoid'] = self.server_info['ChassisMoid']
        inventory_info['ServerType'] = self.server_info['Type']
        inventory_info['ServerPid'] = self.server_info['InventoryServerPid']
        inventory_info['ServerSerial'] = self.server_info['InventoryServerSerial']

        self.server_info['Inventory'].append(
            inventory_info
        )

        self.add_group_info()
        self.add_health_info(server_mo)
        self.add_kvm_info(server_mo)
        self.add_license_info(server_mo)
        self.add_tags_info(server_mo)
        self.server_info['ManagementIp'] = self.get_management_ip(server_mo)
        self.add_management_options()

        if 'advisory' in settings and settings['advisory']:
            start_time = int(time.time() * 1000)
            self.add_advisory_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (advisory): %s' % (duration)
            )

        if 'alarm' in settings and settings['alarm']:
            start_time = int(time.time() * 1000)
            self.add_alarm_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (alarm): %s' % (duration)
            )

        if 'board' in settings and settings['board']:
            start_time = int(time.time() * 1000)
            self.add_board_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (board): %s' % (duration)
            )

        if 'boot' in settings and settings['boot']:
            start_time = int(time.time() * 1000)
            self.add_boot_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (boot): %s' % (duration)
            )

        if 'connector' in settings and settings['connector']:
            start_time = int(time.time() * 1000)
            self.add_connector_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (connector): %s' % (duration)
            )

        if 'contract' in settings and settings['contract']:
            start_time = int(time.time() * 1000)
            self.add_contract_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (contract): %s' % (duration)
            )

        if 'cpu' in settings and settings['cpu']:
            start_time = int(time.time() * 1000)
            self.add_cpu_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (cpu): %s' % (duration)
            )

        if 'fan' in settings and settings['fan']:
            start_time = int(time.time() * 1000)
            self.add_fan_module_info()
            self.add_fan_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (fan): %s' % (duration)
            )

        if 'fw' in settings and settings['fw']:
            start_time = int(time.time() * 1000)
            self.add_firmware_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (fw): %s' % (duration)
            )

        if 'hcl' in settings and settings['hcl']:
            start_time = int(time.time() * 1000)
            self.add_hcl_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (hcl): %s' % (duration)
            )

        if 'locator' in settings and settings['locator']:
            start_time = int(time.time() * 1000)
            self.add_locator_info(server_mo)
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (locator): %s' % (duration)
            )

        if 'memory' in settings and settings['memory']:
            start_time = int(time.time() * 1000)
            self.add_memory_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (memory): %s' % (duration)
            )

        if 'pci' in settings and settings['pci']:
            start_time = int(time.time() * 1000)
            self.add_pci_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (pci): %s' % (duration)
            )

            start_time = int(time.time() * 1000)
            self.add_pci_node_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (pci_node): %s' % (duration)
            )

        if 'gpu' in settings and settings['gpu']:
            start_time = int(time.time() * 1000)
            self.add_gpu_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (gpu): %s' % (duration)
            )

            start_time = int(time.time() * 1000)
            self.add_gcard_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (gcard): %s' % (duration)
            )

            self.add_pci_node_gpu_info()

            if 'pci' not in settings or not settings['pci']:
                if 'PciDevicesInfo' in self.server_info:
                    del self.server_info['PciDevicesInfo']

        if 'net' in settings and settings['net']:
            if server_mo['ObjectType'] == 'compute.RackUnit':
                start_time = int(time.time() * 1000)
                self.add_cimc_info()
                duration = int(time.time() * 1000) - start_time
                self.log.debug(
                    'get_server_info',
                    'Duration (cimc): %s' % (duration)
                )

            start_time = int(time.time() * 1000)
            self.add_adapters_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (adapters): %s' % (duration)
            )

            start_time = int(time.time() * 1000)
            self.add_ext_eth_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (eth): %s' % (duration)
            )

            start_time = int(time.time() * 1000)
            self.add_host_eth_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (host-eth): %s' % (duration)
            )

            start_time = int(time.time() * 1000)
            self.add_host_fc_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (fc): %s' % (duration)
            )

        if 'power' in settings and settings['power']:
            start_time = int(time.time() * 1000)
            self.add_power_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (power): %s' % (duration)
            )

        if 'profile' in settings and settings['profile']:
            start_time = int(time.time() * 1000)
            self.add_profile_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (profile): %s' % (duration)
            )

        if 'psu' in settings and settings['psu']:
            start_time = int(time.time() * 1000)
            self.add_psu_info(server_mo, imc_enabled)
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (psu): %s' % (duration)
            )

        if 'server_setting_id' in settings and settings['server_setting_id']:
            start_time = int(time.time() * 1000)
            self.add_setting_id()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (settings): %s' % (duration)
            )

        if 'storage' in settings and settings['storage']:
            start_time = int(time.time() * 1000)
            self.add_storage_info(server_mo)
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (storage): %s' % (duration)
            )

        if 'thermal' in settings and settings['thermal']:
            start_time = int(time.time() * 1000)
            self.add_thermal_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (thermal): %s' % (duration)
            )

        if 'workflow' in settings and settings['workflow'] is not None:
            start_time = int(time.time() * 1000)
            self.add_workflow_info(
                settings['workflow']
            )
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (workflow): %s' % (duration)
            )

        if 'tpm' in settings and settings['tpm']:
            start_time = int(time.time() * 1000)
            self.add_tpm_info()
            if not settings['board']:
                del self.server_info['BoardInfo']
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (tpm): %s' % (duration)
            )

        if 'state' in settings and settings['state']:
            start_time = int(time.time() * 1000)
            self.add_flags(settings['workflow'])
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (flags): %s' % (duration)
            )

        self.server_info['Inventory'] = sorted(
            self.server_info['Inventory'],
            key=lambda i: (
                i['Order'],
                i['SubOrder']
            )
        )

        self.log.set_log(
            'server_info.%s' % (server_mo['Moid']),
            self.server_info,
            json_conversion=True
        )

        return self.server_info
