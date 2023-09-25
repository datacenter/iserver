import time

from lib import ip_helper
from lib import log_helper
from lib import my_servers_helper

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
from lib.intersight import cache as intersight_cache
from lib.intersight import compute_blade
from lib.intersight import compute_rack
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

from lib.intersight.compute_mo import ComputeMo
from lib.intersight.compute_info import ComputeInfo


class Compute(ComputeMo, ComputeInfo):
    def __init__(self, iaccount, log_id=None):
        ComputeMo.__init__(self)
        ComputeInfo.__init__(self)

        self.log_handler = log_helper.Log(log_id=log_id)
        self.log_id = log_id

        self.rack_handler = compute_rack.ComputeRack(iaccount, log_id=log_id)
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )
        self.iaccount = iaccount

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
