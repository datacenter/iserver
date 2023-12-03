from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.compute_blade.info import ComputeBladeInfo


class ComputeBlade(IntersightCommon, ComputeBladeInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'compute blade'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        ComputeBladeInfo.__init__(self)
