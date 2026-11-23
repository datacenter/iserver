from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_tpm.info import EquipmentTpmInfo


class EquipmentTpm(IntersightCommon, EquipmentTpmInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment tpm'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EquipmentTpmInfo.__init__(self)
