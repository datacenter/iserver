from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.ethernet_port_channel.info import EthernetPortChannelInfo


class EthernetPortChannel(IntersightCommon, EthernetPortChannelInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'ether portchannel'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EthernetPortChannelInfo.__init__(self)