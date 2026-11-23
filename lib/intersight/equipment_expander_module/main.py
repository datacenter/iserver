from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_expander_module.info import EquipmentExpanderModuleInfo


class EquipmentExpanderModule(IntersightCommon, EquipmentExpanderModuleInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'equipment expandermodule'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        EquipmentExpanderModuleInfo.__init__(self)
