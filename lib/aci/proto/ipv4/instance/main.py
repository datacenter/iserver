from lib.aci.proto.ipv4.instance.api import ProtocolIpv4InstanceApi
from lib.aci.proto.ipv4.instance.info import ProtocolIpv4InstanceInfo


class ProtocolIpv4Instance(ProtocolIpv4InstanceApi, ProtocolIpv4InstanceInfo):
    def __init__(self):
        ProtocolIpv4InstanceApi.__init__(self)
        ProtocolIpv4InstanceInfo.__init__(self)
