from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.cond_hclstatus.info import CondHclStatusInfo


class CondHclStatus(IntersightCommon, CondHclStatusInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'cond hclstatus'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        CondHclStatusInfo.__init__(self)
