from lib.aci.proto.bfd.session.stats.api import ProtocolBfdSessionStatsApi
from lib.aci.proto.bfd.session.stats.info import ProtocolBfdSessionStatsInfo


class ProtocolBfdSessionStats(ProtocolBfdSessionStatsApi, ProtocolBfdSessionStatsInfo):
    def __init__(self):
        ProtocolBfdSessionStatsApi.__init__(self)
        ProtocolBfdSessionStatsInfo.__init__(self)
