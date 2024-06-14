from lib.aci.proto.cdp.interface.stats.main import ProtocolCdpInterfaceStats
from lib.aci.proto.cdp.interface.api import ProtocolCdpInterfaceApi
from lib.aci.proto.cdp.interface.info import ProtocolCdpInterfaceInfo


class ProtocolCdpInterface(ProtocolCdpInterfaceApi, ProtocolCdpInterfaceInfo, ProtocolCdpInterfaceStats):
    def __init__(self):
        ProtocolCdpInterfaceApi.__init__(self)
        ProtocolCdpInterfaceInfo.__init__(self)
        ProtocolCdpInterfaceStats.__init__(self)
