import time

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
from lib.intersight import storage_physical_disk_usage
from lib.intersight import storage_virtual_drive
from lib.intersight import storage_controller
from lib.intersight import tam_advisory_definition
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
        self.chassis = None

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

    def add_alarm_info(self, include_cleared=False):
        self.server_info['AlarmInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'alarm',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_alarm_info',
                'No cache'
            )
            return

        for managed_object in managed_objects:
            alarm_info = self.cond_alarm_handler.get_info(
                managed_object
            )
            if alarm_info['Severity'] == 'Cleared' and not include_cleared:
                continue

            self.server_info['AlarmInfo'].append(
                alarm_info
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
                'No cache'
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
                'No cache'
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

        self.server_info['BoardInfo'] = self.compute_board_handler.get_compute_board_info(
            managed_objects[0]
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

        if len(managed_objects) != 1:
            self.log.error(
                'add_boot_info',
                'Unexpected number of boot device boot mode objects'
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

    def add_chassis_object(self, server_mo):
        if self.chassis is not None:
            return

        self.chassis = self.equipment_chassis_handler.get(
            server_mo['EquipmentChassis']['Moid']
        )

    def add_chassis_info(self):
        if self.chassis is not None:
            self.server_info['ChassisInfo'] = self.equipment_chassis_handler.get_summary(
                self.chassis
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
                'No cache'
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
                'No cache'
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
                'No cache'
            )
        else:
            for managed_object in managed_objects:
                self.server_info['CpuInfo'].append(
                    self.processor_unit_handler.get_processor_unit_info(
                        managed_object
                    )
                )

        self.server_info['CpuInfo'] = sorted(
            self.server_info['CpuInfo'],
            key=lambda i: i['ProcessorId']
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
                'No cache'
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
            for adapter_info in self.server_info['AdaptersInfo']:
                if managed_object['Moid'] in adapter_info['ExtEthIfsIds']:
                    interface_info['AdapterName'] = adapter_info['Name']
                    interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    mac_info['AdapterModel'] = adapter_info['Model']
                    mac_info['AdapterPciSlot'] = adapter_info['PciSlot']

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

    def add_fan_info(self):
        if self.server_info['Type'] == 'Blade':
            if self.chassis is None:
                self.server_info['FanSummary'] = ''
                self.server_info['FanHealthy'] = True
                self.server_info['FanInfo'] = []
                return

            self.server_info['FanInfo'] = []

            # for fan_module in self.chassis['Fanmodules']:
            #     self.server_info['FanInfo'].append(
            #         self.fan_handler.get_fan_info(
            #             fan_module['Moid']
            #         )
            #     )

            # self.server_info['FanInfo'] = sorted(
            #     self.server_info['FanInfo'],
            #     key=lambda i: i['Dn']
            # )

            # self.server_info['FanOn'] = 0
            # for fan_module in self.chassis['Fanmodules']:
            #     if self.fan_handler.get_fan_state(fan_module['Moid']):
            #         self.server_info['FanOn'] = self.server_info['FanOn'] + 1

            # self.server_info['FanCount'] = len(self.chassis['Fanmodules'])
            # self.server_info['FanSummary'] = '%s/%s' % (
            #     self.server_info['FanOn'],
            #     self.server_info['FanCount']
            # )
            # self.server_info['FanHealthy'] = True
            # if self.server_info['FanOn'] < self.server_info['FanCount']:
            #     self.server_info['FanHealthy'] = False

        if self.server_info['Type'] == 'Rack':
            self.server_info['FanInfo'] = []

            managed_objects = self.cache_handler.get_intersight_cache_entry(
                'fanmodule',
                subdirectory=self.server_info['Moid'],
                check_ttl=False
            )
            if managed_objects is None:
                self.log.error(
                    'add_fan_info',
                    'No cache'
                )
            else:
                for managed_object in managed_objects:
                    self.server_info['FanInfo'].append(
                        self.fan_handler.get_fan_info(
                            managed_object
                        )
                    )

            self.server_info['FanInfo'] = sorted(
                self.server_info['FanInfo'],
                key=lambda i: i['Dn']
            )

            self.server_info['FanOn'] = 0
            for fan_module_info in self.server_info['FanInfo']:
                if fan_module_info['On']:
                    self.server_info['FanOn'] = self.server_info['FanOn'] + 1

            self.server_info['FanCount'] = len(self.server_info['FanInfo'])
            self.server_info['FanSummary'] = '%s/%s' % (
                self.server_info['FanOn'],
                self.server_info['FanCount']
            )
            self.server_info['FanHealthy'] = True
            if self.server_info['FanOn'] < self.server_info['FanCount']:
                self.server_info['FanHealthy'] = False

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
                'No cache'
            )
            return

        for managed_object in managed_objects:
            self.server_info['FirmwarewComponents'].append(
                self.running_firmware_handler.get_info(
                    managed_object
                )
            )

        self.server_info['FirmwareVersion'] = self.running_firmware_handler.get_firmware_version(
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

    def add_gpu_info(self):
        self.server_info['GpuInfo'] = []
        for pci_device_info in self.server_info['PciDevicesInfo']:
            if '-GPU-' in pci_device_info['Pid']:
                self.server_info['GpuInfo'].append(
                    pci_device_info
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
                'No cache'
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
                'No cache'
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
            for adapter_info in self.server_info['AdaptersInfo']:
                if managed_object['Moid'] in adapter_info['HostEthIfsIds']:
                    interface_info['AdapterName'] = adapter_info['Name']
                    interface_info['AdapterPciSlot'] = adapter_info['PciSlot']
                    mac_info['AdapterModel'] = adapter_info['Model']
                    mac_info['AdapterPciSlot'] = adapter_info['PciSlot']

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
                'No cache'
            )
            return

        for managed_object in managed_objects:
            interface_info = self.adapter_host_fc_interface_handler.get_info(
                managed_object
            )

            interface_info['AdapterName'] = None
            interface_info['AdapterPciSlot'] = None
            for adapter_info in self.server_info['AdaptersInfo']:
                if managed_object['Moid'] in adapter_info['HostFcIfsIds']:
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

    def add_locator_info(self, server_mo):
        self.server_info['LocatorLedOn'] = False

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'locator',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_locator_info',
                'No cache'
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log.error(
                'add_locator_info',
                'Unexpected object count: %s' % (self.server_info['Moid'])
            )
            return

        self.server_info['LocatorLedOn'] = self.locator_handler.get_locator_led(
            managed_objects[0]
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
                'No cache'
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

        # if self.server_info['Type'] == 'Rack':
        #     self.server_info['MemoryInfo'] = self.memory_unit_handler.get_memory_units_info()

        # if self.server_info['Type'] == 'Blade':
        #     chassis_memory_info = self.memory_unit_handler.get_memory_units_info()
        #     memory_info = []

        #     for item in chassis_memory_info:
        #         if item['ServerId'] == server['Moid']:
        #             memory_info.append(item)

        #     self.server_info['MemoryInfo'] = memory_info

    def add_pci_info(self):
        self.server_info['PciDevicesInfo'] = []
        self.server_info['PciModels'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'pci',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_pci_info',
                'No cache'
            )
        else:
            for managed_object in managed_objects:
                self.server_info['PciDevicesInfo'].append(
                    self.pci_handler.get_pci_info(
                        managed_object
                    )
                )

                self.server_info['PciModels'].append(
                    self.pci_handler.get_pci_model(
                        managed_object
                    )
                )

        self.server_info['PciDevicesInfo'] = sorted(
            self.server_info['PciDevicesInfo'],
            key=lambda i: i['Dn']
        )

    def add_power_info(self):
        self.server_info['Power'] = self.cache_handler.get_intersight_cache_entry(
            'power',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if self.server_info['Power'] is None:
            self.log.error(
                'add_power_info',
                'No cache'
            )

        # if self.server_info['Redfish']['Enabled']:
        #     self.server_info['Power'] = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
        #         self.server_info['Serial'],
        #         'power'
        #     )

        # if self.server_info['UCSM']['Enabled']:
        #     self.server_info['Power'] = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
        #         self.server_info['Serial'],
        #         'power'
        #     )

    def add_profile_info(self):
        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'profile',
            subdirectory=self.server_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log.error(
                'add_profile_info',
                'No cache'
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

    def add_psu_info(self, server_mo):
        if self.server_info['Type'] == 'Blade':
            if self.chassis is None:
                self.server_info['PsuSummary'] = ''
                self.server_info['PsuHealthy'] = True
                self.server_info['PsuInfo'] = []
                return

            # self.server_info['PsuInfo'] = []

            # for psu in self.chassis['Psus']:
            #     self.server_info['PsuInfo'].append(
            #         self.psu_handler.get_psu_info(
            #             psu['Moid']
            #         )
            #     )

            # self.server_info['PsuInfo'] = sorted(
            #     self.server_info['PsuInfo'],
            #     key=lambda i: i['Dn']
            # )

            # self.server_info['PsuOn'] = 0
            # for psu in self.chassis['Psus']:
            #     if self.psu_handler.get_psu_state(psu['Moid']):
            #         self.server_info['PsuOn'] = self.server_info['PsuOn'] + 1

            # self.server_info['PsuCount'] = len(self.chassis['Psus'])
            # self.server_info['PsuSummary'] = '%s/%s' % (
            #     self.server_info['PsuOn'],
            #     self.server_info['PsuCount']
            # )
            # self.server_info['PsuHealthy'] = True
            # if self.server_info['PsuOn'] < self.server_info['PsuCount']:
            #     self.server_info['PsuHealthy'] = False

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
                    'No cache'
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

    def add_storage_virtual_disk_info(self, virtual_drives_mo, physical_disks_usage_mo):
        self.server_info['VirtualDisks'] = self.storage_virtual_drive_handler.get_virtual_drives_info(
            virtual_drives_mo,
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )

        for virtual_disk_info in self.server_info['VirtualDisks']:
            virtual_disk_info['PhysicalDiskIds'] = []

            if virtual_disk_info['PhysicalDiskCount'] > 0:
                if physical_disks_usage_mo is not None:
                    for physical_disk_usage_mo in physical_disks_usage_mo:
                        if physical_disk_usage_mo['StorageVirtualDrive']['Moid'] == virtual_disk_info['Moid']:
                            virtual_disk_info['PhysicalDiskIds'].append(
                                physical_disk_usage_mo['PhysicalDrive']
                            )

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
        self.server_info['PhysicalDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            physical_disks_mo,
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['PhysicalDiskCount'] = len(
            self.server_info['PhysicalDisks']
        )
        self.server_info['PhysicalDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            self.server_info['PhysicalDisks']
        )
        self.server_info['PhysicalDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['PhysicalDiskCapacity']
        )

    def add_storage_info(self, server):
        start_time = int(time.time() * 1000)

        storage_controllers_mo = None
        if self.server_info['Type'] == 'Rack':
            storage_server_id = server['Board']['Moid']
            if self.cache_handler.intersight_cache_enabled:
                storage_controllers_mo = self.cache_handler.get_intersight_cache_entry(
                    'storage_controller',
                    subdirectory=server['Moid']
                )

            if storage_controllers_mo is None:
                storage_controllers_mo = self.storage_controller_handler.get_board_storage_controllers(
                    server['Board']['Moid'],
                    cache=True
                )
                if storage_controllers_mo is not None:
                    self.cache_handler.set_intersight_cache_entry(
                        'storage_controller',
                        storage_controllers_mo,
                        subdirectory=server['Moid']
                    )

        if self.server_info['Type'] == 'Blade':
            storage_server_id = server['Moid']
            if self.cache_handler.intersight_cache_enabled:
                storage_controllers_mo = self.cache_handler.get_intersight_cache_entry(
                    'storage_controller',
                    subdirectory=server['Moid']
                )

            if storage_controllers_mo is None:
                storage_controllers_mo = self.storage_controller_handler.get_blade_storage_controllers(
                    self.server_info['Moid'],
                    cache=True
                )
                if storage_controllers_mo is not None:
                    self.cache_handler.set_intersight_cache_entry(
                        'storage_controller',
                        storage_controllers_mo,
                        subdirectory=server['Moid']
                    )

        virtual_drives_mo = None
        if self.cache_handler.intersight_cache_enabled:
            virtual_drives_mo = self.cache_handler.get_intersight_cache_entry(
                'virtual_drive',
                subdirectory=server['Moid']
            )

        if virtual_drives_mo is None:
            virtual_drives_mo = self.storage_virtual_drive_handler.get_virtual_drives(
                storage_server_id,
                cache=True
            )
            if virtual_drives_mo is not None:
                self.cache_handler.set_intersight_cache_entry(
                    'virtual_drive',
                    virtual_drives_mo,
                    subdirectory=server['Moid']
                )

        physical_disks_mo = None
        if self.cache_handler.intersight_cache_enabled:
            physical_disks_mo = self.cache_handler.get_intersight_cache_entry(
                'physical_disk',
                subdirectory=server['Moid']
            )

        if physical_disks_mo is None:
            physical_disks_mo = self.storage_physical_disk_handler.get_compute_disks(
                storage_server_id,
                cache=True
            )
            if physical_disks_mo is not None:
                self.cache_handler.set_intersight_cache_entry(
                    'physical_disk',
                    physical_disks_mo,
                    subdirectory=server['Moid']
                )

        physical_disks_usage_mo = None
        if self.cache_handler.intersight_cache_enabled:
            physical_disks_usage_mo = self.cache_handler.get_intersight_cache_entry(
                'physical_disk_usage',
                subdirectory=server['Moid']
            )

        if physical_disks_usage_mo is None:
            if virtual_drives_mo is not None:
                virtual_drive_moids = []
                for virtual_drive_mo in virtual_drives_mo:
                    virtual_drive_moids.append(
                        virtual_drive_mo['Moid']
                    )

                if len(virtual_drive_moids) > 0:
                    virtual_drive_moids_list = []
                    for virtual_drive_moid in virtual_drive_moids:
                        virtual_drive_moids_list.append('\'%s\'' % (virtual_drive_moid))
                    virtual_drive_moids_filter = ', '.join(virtual_drive_moids_list)
                    self.storage_physical_disk_usage_handler.set_get_filter(
                        "StorageVirtualDrive/Moid in (%s)" % (virtual_drive_moids_filter)
                    )

                    physical_disks_usage_mo = self.storage_physical_disk_usage_handler.get_all()
                    if physical_disks_usage_mo is not None:
                        self.cache_handler.set_intersight_cache_entry(
                            'physical_disk_usage',
                            physical_disks_usage_mo,
                            subdirectory=server['Moid']
                        )

        self.log.debug(
            'add_storage_info',
            'Storage (disk): %s' % (int(time.time() * 1000) - start_time)
        )

        if self.server_info['Type'] == 'Rack':
            self.server_info['StorageControllersInfo'] = self.storage_controller_handler.get_board_storage_controllers_info(
                storage_controllers_mo,
                physical_disks_mo=physical_disks_mo
            )

        if self.server_info['Type'] == 'Blade':
            self.server_info['StorageControllersInfo'] = self.storage_controller_handler.get_blade_storage_controllers_info(
                controllers=storage_controllers_mo
            )

        if self.server_info['StorageControllersInfo'] is None:
            self.server_info['StorageControllersCount'] = 0
        else:
            self.server_info['StorageControllersCount'] = len(self.server_info['StorageControllersInfo'])

        self.add_storage_virtual_disk_info(virtual_drives_mo, physical_disks_usage_mo)
        self.add_storage_physical_disk_info(physical_disks_mo)

        self.server_info['StorageDrives'] = '%sC %sD %sVD' % (
            self.server_info['StorageControllersCount'],
            self.server_info['PhysicalDiskCount'],
            self.server_info['VirtualDiskCount']
        )

        self.server_info['StorageCapacity'] = 'R %s , VD %s' % (
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

        self.server_info['StorageSummary'] = '%sC %sD %sVD R%s L%s' % (
            self.server_info['StorageControllersCount'],
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
                'No cache'
            )

        # self.server_info['Thermal'] = None

        # if self.server_info['Redfish']['Enabled']:
        #     if self.server_info['OperPowerState'] == 'on':
        #         self.server_info['Thermal'] = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
        #             self.server_info['Serial'],
        #             'thermal'
        #         )

        # if self.server_info['UCSM']['Enabled']:
        #     self.server_info['Thermal'] = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
        #         self.server_info['Serial'],
        #         'thermal'
        #     )

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
            'TotalMemory'
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

        usage = int(self.server_info['UsedMemory'] * 100 / self.server_info['TotalMemory'])
        self.server_info['UsedMemoryPct'] = usage
        self.server_info['UsedMemoryPctUnit'] = '%s%%' % (usage)

        if server_mo['ObjectType'] == 'compute.RackUnit':
            self.server_info['Type'] = 'Rack'
            self.server_info['TypeModel'] = '(R) %s' % (self.server_info['Model'])

        if server_mo['ObjectType'] == 'compute.Blade':
            self.server_info['Type'] = 'Blade'
            self.server_info['TypeModel'] = '(B) %s' % (server_mo['Model'])

        self.server_info['Connected'] = False

        self.add_group_info()
        self.add_health_info(server_mo)
        self.add_kvm_info(server_mo)
        self.add_license_info(server_mo)
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

        if 'chassis' in settings and settings['chassis']:
            start_time = int(time.time() * 1000)
            self.add_chassis_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (chassis): %s' % (duration)
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

        if 'gpu' in settings and settings['gpu']:
            start_time = int(time.time() * 1000)
            self.add_gpu_info()
            duration = int(time.time() * 1000) - start_time
            self.log.debug(
                'get_server_info',
                'Duration (gpu): %s' % (duration)
            )

            if 'pci' not in settings or not settings['pci']:
                if 'PciDevicesInfo' in self.server_info:
                    del self.server_info['PciDevicesInfo']

        if 'net' in settings and settings['net']:
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
            self.add_psu_info(server_mo)
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

        self.log.set_log(
            'server_info.%s' % (server_mo['Moid']),
            self.server_info,
            json_conversion=True
        )

        return self.server_info
