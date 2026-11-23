from lib.aci.proto.lacp.instance.api import ProtocolLacpInstanceApi
from lib.aci.proto.lacp.instance.info import ProtocolLacpInstanceInfo


class ProtocolLacpInstance(ProtocolLacpInstanceApi, ProtocolLacpInstanceInfo):
    def __init__(self):
        ProtocolLacpInstanceApi.__init__(self)
        ProtocolLacpInstanceInfo.__init__(self)
