from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.tam_advisory_instance.info import TamAdvisoryInstanceInfo


class TamAdvisoryInstance(IntersightCommon, TamAdvisoryInstanceInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'tam advisoryinstance'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        TamAdvisoryInstanceInfo.__init__(self)
