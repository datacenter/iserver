import time

from lib import ip_helper
from lib import log_helper

from lib.intersight import compute_blade
from lib.intersight import equipment_chassis
from lib.intersight import cache as intersight_cache
from lib.intersight.chassis_mo import ChassisMo
from lib.intersight.chassis_info import ChassisInfo

from lib.intersight import equipment_fan_module
from lib.intersight import equipment_fan
from lib.intersight import equipment_fan_control
from lib.intersight import equipment_psu
from lib.intersight import equipment_psu_control
from lib.intersight import power_control_state
from lib.intersight import equipment_iocard
from lib.intersight import ethernet_host_port
from lib.intersight import ethernet_network_port
from lib.intersight import ethernet_physical_port
from lib.intersight import compute_blade
from lib.intersight import adapter_unit
from lib.intersight import adapter_ext_eth_interface
from lib.intersight import cond_alarm
from lib.intersight import tam_advisory_instance
from lib.intersight import asset_device_contract_information
from lib.intersight import chassis_profile
from lib.intersight import network_element_summary


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
