from lib.aci.proto.bfd.interface.api import ProtocolBfdInterfaceApi
from lib.aci.proto.bfd.interface.info import ProtocolBfdInterfaceInfo


class ProtocolBfdInterface(ProtocolBfdInterfaceApi, ProtocolBfdInterfaceInfo):
    def __init__(self):
        ProtocolBfdInterfaceApi.__init__(self)
        ProtocolBfdInterfaceInfo.__init__(self)
