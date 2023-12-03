from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_fan_control.info import EquipmentFanControlInfo


class EquipmentFanControl(IntersightCommon, EquipmentFanControlInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment fancontrol'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EquipmentFanControlInfo.__init__(self)
