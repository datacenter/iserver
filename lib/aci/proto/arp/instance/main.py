from lib.aci.proto.arp.instance.api import ProtocolArpInstanceApi
from lib.aci.proto.arp.instance.info import ProtocolArpInstanceInfo


class ProtocolArpInstance(ProtocolArpInstanceApi, ProtocolArpInstanceInfo):
    def __init__(self):
        ProtocolArpInstanceApi.__init__(self)
        ProtocolArpInstanceInfo.__init__(self)
