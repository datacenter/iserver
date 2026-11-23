from lib.aci.proto.hsrp.interface.stats.main import ProtocolHsrpInterfaceStats
from lib.aci.proto.hsrp.interface.api import ProtocolHsrpInterfaceApi
from lib.aci.proto.hsrp.interface.info import ProtocolHsrpInterfaceInfo


class ProtocolHsrpInterface(ProtocolHsrpInterfaceApi, ProtocolHsrpInterfaceInfo, ProtocolHsrpInterfaceStats):
    def __init__(self):
        ProtocolHsrpInterfaceApi.__init__(self)
        ProtocolHsrpInterfaceInfo.__init__(self)
        ProtocolHsrpInterfaceStats.__init__(self)
