from lib.aci.proto.lldp.stats.api import ProtocolLldpStatsApi
from lib.aci.proto.lldp.stats.info import ProtocolLldpStatsInfo


class ProtocolLldpStats(ProtocolLldpStatsApi, ProtocolLldpStatsInfo):
    def __init__(self):
        ProtocolLldpStatsApi.__init__(self)
        ProtocolLldpStatsInfo.__init__(self)
