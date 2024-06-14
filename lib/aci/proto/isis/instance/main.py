from lib.aci.proto.isis.instance.api import ProtocolIsisInstanceApi
from lib.aci.proto.isis.instance.info import ProtocolIsisInstanceInfo


class ProtocolIsisInstance(ProtocolIsisInstanceApi, ProtocolIsisInstanceInfo):
    def __init__(self):
        ProtocolIsisInstanceApi.__init__(self)
        ProtocolIsisInstanceInfo.__init__(self)
