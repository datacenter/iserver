from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_fan.info import EquipmentFanInfo


class EquipmentFan(IntersightCommon, EquipmentFanInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment fan'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EquipmentFanInfo.__init__(self)
