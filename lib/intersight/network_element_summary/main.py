from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.network_element_summary.info import NetworkElementSummaryInfo


class NetworkElementSummary(IntersightCommon, NetworkElementSummaryInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'network elementsummary'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        NetworkElementSummaryInfo.__init__(self)
