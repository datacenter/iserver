from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.tam_security_advisory.info import TamSecurityAdvisoryInfo


class TamSecurityAdvisory(IntersightCommon, TamSecurityAdvisoryInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'tam securityadvisory'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        TamSecurityAdvisoryInfo.__init__(self)
