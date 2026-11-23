from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.ethernet_network_port.info import EthernetNetworkPortInfo


class EthernetNetworkPort(IntersightCommon, EthernetNetworkPortInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'ether networkport'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EthernetNetworkPortInfo.__init__(self)