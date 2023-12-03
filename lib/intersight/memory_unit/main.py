from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.memory_unit.info import MemoryUnitInfo


class MemoryUnit(IntersightCommon, MemoryUnitInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'memory unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        MemoryUnitInfo.__init__(self)
