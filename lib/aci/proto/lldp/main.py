from lib.aci.proto.lldp.instance.main import ProtocolLldpInstance
from lib.aci.proto.lldp.stats.main import ProtocolLldpStats
from lib.aci.proto.lldp.context import ProtocolLldpContext
from lib.aci.proto.lldp.info import ProtocolLldpInfo
from lib.aci.proto.lldp.event.main import ProtocolLldpEvent
from lib.aci.proto.lldp.fault.main import ProtocolLldpFault


class ProtocolLldp(ProtocolLldpInstance, ProtocolLldpStats, ProtocolLldpContext, ProtocolLldpInfo, ProtocolLldpEvent, ProtocolLldpFault):
    def __init__(self):
        ProtocolLldpInstance.__init__(self)
        ProtocolLldpStats.__init__(self)
        ProtocolLldpContext.__init__(self)
        ProtocolLldpInfo.__init__(self)
        ProtocolLldpEvent.__init__(self)
        ProtocolLldpFault.__init__(self)
