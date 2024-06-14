from lib.aci.proto.isis.interface.api import ProtocolIsisInterfaceApi
from lib.aci.proto.isis.interface.info import ProtocolIsisInterfaceInfo


class ProtocolIsisInterface(ProtocolIsisInterfaceApi, ProtocolIsisInterfaceInfo):
    def __init__(self):
        ProtocolIsisInterfaceApi.__init__(self)
        ProtocolIsisInterfaceInfo.__init__(self)
