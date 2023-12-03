from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.compute_board.info import ComputeBoardInfo


class ComputeBoard(IntersightCommon, ComputeBoardInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'compute board'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        ComputeBoardInfo.__init__(self)
