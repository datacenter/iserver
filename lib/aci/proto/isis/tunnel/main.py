from lib.aci.proto.isis.tunnel.api import ProtocolIsisTunnelApi
from lib.aci.proto.isis.tunnel.info import ProtocolIsisTunnelInfo


class ProtocolIsisTunnel(ProtocolIsisTunnelApi, ProtocolIsisTunnelInfo):
    def __init__(self):
        ProtocolIsisTunnelApi.__init__(self)
        ProtocolIsisTunnelInfo.__init__(self)
