from lib.aci.proto.nd.instance.api import ProtocolNdInstanceApi
from lib.aci.proto.nd.instance.info import ProtocolNdInstanceInfo


class ProtocolNdInstance(ProtocolNdInstanceApi, ProtocolNdInstanceInfo):
    def __init__(self):
        ProtocolNdInstanceApi.__init__(self)
        ProtocolNdInstanceInfo.__init__(self)
