from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.ethernet_physical_port.info import EthernetPhysicalPortInfo


class EthernetPhysicalPort(IntersightCommon, EthernetPhysicalPortInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'ether physicalport'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EthernetPhysicalPortInfo.__init__(self)