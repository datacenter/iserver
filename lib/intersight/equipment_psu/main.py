from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_psu.info import EquipmentPsuInfo


class EquipmentPsu(IntersightCommon, EquipmentPsuInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'equipment psu'
        self.cache_key = 'psu'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id, cache_key=self.cache_key)
        EquipmentPsuInfo.__init__(self)
