from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_fan_module.info import EquipmentFanModuleInfo


class EquipmentFanModule(IntersightCommon, EquipmentFanModuleInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment fanmodule'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EquipmentFanModuleInfo.__init__(self)
