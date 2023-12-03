from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.ethernet_host_port.info import EthernetHostPortInfo


class EthernetHostPort(IntersightCommon, EthernetHostPortInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'ether hostport'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EthernetHostPortInfo.__init__(self)
