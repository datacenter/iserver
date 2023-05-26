from lib.aci.proto.bgp.instance.api import ProtocolBgpInstanceApi
from lib.aci.proto.bgp.instance.info import ProtocolBgpInstanceInfo


class ProtocolBgpInstance(ProtocolBgpInstanceApi, ProtocolBgpInstanceInfo):
    def __init__(self):
        ProtocolBgpInstanceApi.__init__(self)
        ProtocolBgpInstanceInfo.__init__(self)
