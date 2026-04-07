from lib import log_helper

from lib.intersight import cache as intersight_cache
from lib.intersight.fi_mo import FiMo
from lib.intersight.fi_info import FiInfo
from lib.intersight.network_element import main as network_element
from lib.intersight.network_element_summary import main as network_element_summary
from lib.intersight.ethernet_physical_port import main as ethernet_physical_port
from lib.intersight.ethernet_port_channel import main as ethernet_port_channel
from lib.intersight.equipment_fan_module import main as equipment_fan_module
from lib.intersight.equipment_fan import main as equipment_fan
from lib.intersight.equipment_psu import main as equipment_psu
from lib.intersight.storage_item import main as storage_item


class Fi(FiMo, FiInfo):
    def __init__(self, iaccount, log_id=None):
        FiMo.__init__(self)
        FiInfo.__init__(self)

        self.log_handler = log_helper.Log(log_id=log_id)
        self.log_id = log_id

        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )
        self.iaccount = iaccount

        self.fi_handler = network_element.NetworkElement(iaccount, log_id=log_id)
        self.network_element_summary_handler = network_element_summary.NetworkElementSummary(iaccount, log_id=log_id)
        self.ethernet_physical_port_handler = ethernet_physical_port.EthernetPhysicalPort(iaccount, log_id=log_id)
        self.ethernet_port_channel_handler = ethernet_port_channel.EthernetPortChannel(iaccount, log_id=log_id)
        self.fan_module_handler = equipment_fan_module.EquipmentFanModule(iaccount, log_id=log_id)
        self.fan_handler = equipment_fan.EquipmentFan(iaccount, log_id=log_id)
        self.psu_handler = equipment_psu.EquipmentPsu(iaccount, log_id=log_id)
        self.storage_handler = storage_item.StorageItem(iaccount, log_id=log_id)