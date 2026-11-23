from lib.aci.proto.ipv6.instance.api import ProtocolIpv6InstanceApi
from lib.aci.proto.ipv6.instance.info import ProtocolIpv6InstanceInfo


class ProtocolIpv6Instance(ProtocolIpv6InstanceApi, ProtocolIpv6InstanceInfo):
    def __init__(self):
        ProtocolIpv6InstanceApi.__init__(self)
        ProtocolIpv6InstanceInfo.__init__(self)
