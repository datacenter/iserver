from lib import log_helper

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
from lib.intersight.compute_blade import main as compute_blade
from lib.intersight.compute_rack import main as compute_rack
from lib.intersight.cond_alarm import main as cond_alarm
from lib.intersight.cond_hclstatus import main as cond_hclstatus
from lib.intersight.cond_hclstatus_detail import main as cond_hclstatus_detail
from lib.intersight.compute_board import main as compute_board
from lib.intersight.compute_server_setting import main as compute_server_setting
from lib.intersight.equipment_chassis import main as equipment_chassis
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

from lib.intersight.compute_mo import ComputeMo
from lib.intersight.compute_info import ComputeInfo
from lib.intersight.compute_context import ComputeContext


class Compute(ComputeMo, ComputeInfo, ComputeContext):
    def __init__(self, iaccount, log_id=None):
        ComputeMo.__init__(self)
        ComputeInfo.__init__(self)
        ComputeContext.__init__(self)

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
