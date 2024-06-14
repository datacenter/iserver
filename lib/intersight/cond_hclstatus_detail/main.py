from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.cond_hclstatus_detail.info import CondHclStatusDetailInfo


class CondHclStatusDetail(IntersightCommon, CondHclStatusDetailInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'cond hclstatusdetail'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        CondHclStatusDetailInfo.__init__(self)
