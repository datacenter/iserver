from lib.aci.proto.bfd.instance.api import ProtocolBfdInstanceApi
from lib.aci.proto.bfd.instance.info import ProtocolBfdInstanceInfo


class ProtocolBfdInstance(ProtocolBfdInstanceApi, ProtocolBfdInstanceInfo):
    def __init__(self):
        ProtocolBfdInstanceApi.__init__(self)
        ProtocolBfdInstanceInfo.__init__(self)
