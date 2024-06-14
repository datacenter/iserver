from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.processor_unit.info import ProcessorUnitInfo


class ProcessorUnit(IntersightCommon, ProcessorUnitInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'processor unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        ProcessorUnitInfo.__init__(self)
