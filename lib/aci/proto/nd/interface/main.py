from lib.aci.proto.nd.interface.api import ProtocolNdInterfaceApi
from lib.aci.proto.nd.interface.info import ProtocolNdInterfaceInfo
from lib.aci.proto.nd.interface.stats.main import ProtocolNdInstanceStats


class ProtocolNdInterface(ProtocolNdInterfaceApi, ProtocolNdInterfaceInfo, ProtocolNdInstanceStats):
    def __init__(self):
        ProtocolNdInterfaceApi.__init__(self)
        ProtocolNdInterfaceInfo.__init__(self)
        ProtocolNdInstanceStats.__init__(self)
