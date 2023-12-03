from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_psu_control.info import EquipmentPsuControlInfo


class EquipmentPsuControl(IntersightCommon, EquipmentPsuControlInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'equipment psucontrol'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        EquipmentPsuControlInfo.__init__(self)
