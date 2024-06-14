from lib import log_helper

from lib.intersight import cache as intersight_cache
from lib.intersight.chassis_mo import ChassisMo
from lib.intersight.chassis_info import ChassisInfo

from lib.intersight.adapter_unit import main as adapter_unit
from lib.intersight.adapter_ext_eth_interface import main as adapter_ext_eth_interface
from lib.intersight.asset_device_contract_information import main as asset_device_contract_information
from lib.intersight.chassis_profile import main as chassis_profile
from lib.intersight.compute_blade import main as compute_blade
from lib.intersight.cond_alarm import main as cond_alarm
from lib.intersight.equipment_chassis import main as equipment_chassis
from lib.intersight.equipment_expander_module import main as equipment_expander_module
from lib.intersight.equipment_fan_module import main as equipment_fan_module
from lib.intersight.equipment_fan import main as equipment_fan
from lib.intersight.equipment_fan_control import main as equipment_fan_control
from lib.intersight.equipment_iocard import main as equipment_iocard
from lib.intersight.equipment_psu import main as equipment_psu
from lib.intersight.equipment_psu_control import main as equipment_psu_control
from lib.intersight.ethernet_host_port import main as ethernet_host_port
from lib.intersight.ethernet_network_port import main as ethernet_network_port
from lib.intersight.ethernet_physical_port import main as ethernet_physical_port
from lib.intersight.network_element_summary import main as network_element_summary
from lib.intersight.power_control_state import main as power_control_state
from lib.intersight.tam_advisory_instance import main as tam_advisory_instance


class Chassis(ChassisMo, ChassisInfo):
    def __init__(self, iaccount, log_id=None):
        ChassisMo.__init__(self)
        ChassisInfo.__init__(self)

        self.log_handler = log_helper.Log(log_id=log_id)
        self.log_id = log_id

        self.chassis_handler = equipment_chassis.EquipmentChassis(iaccount, log_id=log_id)
        self.chassis_handler.set_get_expand('RegisteredDevice')
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

        self.iocard_handler = equipment_iocard.EquipmentIoCard(iaccount, log_id=log_id)
        self.expander_module_handler = equipment_expander_module.EquipmentExpanderModule(iaccount, log_id=log_id)
        self.ether_host_port_handler = ethernet_host_port.EthernetHostPort(iaccount, log_id=log_id)
        self.ether_network_port_handler = ethernet_network_port.EthernetNetworkPort(iaccount, log_id=log_id)
        self.ether_physical_port_handler = ethernet_physical_port.EthernetPhysicalPort(iaccount, log_id=log_id)
        self.fan_module_handler = equipment_fan_module.EquipmentFanModule(iaccount, log_id=log_id)
        self.fan_handler = equipment_fan.EquipmentFan(iaccount, log_id=log_id)
        self.fan_control_handler = equipment_fan_control.EquipmentFanControl(iaccount, log_id=log_id)
        self.psu_handler = equipment_psu.EquipmentPsu(iaccount, log_id=log_id)
        self.psu_control_handler = equipment_psu_control.EquipmentPsuControl(iaccount, log_id=log_id)
        self.power_control_state_handler = power_control_state.PowerControlState(iaccount, log_id=log_id)
        self.compute_blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.adapter_unit_handler = adapter_unit.AdapterUnit(iaccount, log_id=log_id)
        self.adapter_ext_eth_interface_handler = adapter_ext_eth_interface.AdapterExtEthInterface(iaccount, log_id=log_id)
        self.cond_alarm_handler = cond_alarm.CondAlarm(iaccount, log_id=log_id)
        self.tam_advisory_instance_handler = tam_advisory_instance.TamAdvisoryInstance(iaccount, log_id=log_id)
        self.asset_device_contract_information_handler = asset_device_contract_information.AssetDeviceContractInformation(iaccount, log_id=log_id)
        self.chassis_profile_handler = chassis_profile.ChassisProfile(iaccount, log_id=log_id)
        self.network_element_summary_handler = network_element_summary.NetworkElementSummary(iaccount, log_id=log_id)
