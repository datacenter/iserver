from lib.aci.proto.lldp.instance.api import ProtocolLldpInstanceApi
from lib.aci.proto.lldp.instance.info import ProtocolLldpInstanceInfo


class ProtocolLldpInstance(ProtocolLldpInstanceApi, ProtocolLldpInstanceInfo):
    def __init__(self):
        ProtocolLldpInstanceApi.__init__(self)
        ProtocolLldpInstanceInfo.__init__(self)
