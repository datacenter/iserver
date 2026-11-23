from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_iocard.info import EquipmentIoCardInfo


class EquipmentIoCard(IntersightCommon, EquipmentIoCardInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'equipment iocard'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        EquipmentIoCardInfo.__init__(self)
