from lib.aci.proto.lldp.instance.main import ProtocolLldpInstance
from lib.aci.proto.lldp.stats.main import ProtocolLldpStats
from lib.aci.proto.lldp.context import ProtocolLldpContext
from lib.aci.proto.lldp.info import ProtocolLldpInfo


class ProtocolLldp(ProtocolLldpInstance, ProtocolLldpStats, ProtocolLldpContext, ProtocolLldpInfo):
    def __init__(self):
        ProtocolLldpInstance.__init__(self)
        ProtocolLldpStats.__init__(self)
        ProtocolLldpContext.__init__(self)
        ProtocolLldpInfo.__init__(self)
