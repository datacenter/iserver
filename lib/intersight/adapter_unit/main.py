from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.adapter_unit.info import AdapterUnitInfo

class AdapterUnit(IntersightCommon, AdapterUnitInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        AdapterUnitInfo.__init__(self)
