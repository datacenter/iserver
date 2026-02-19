from lib.nexus.pc.database.main import PcDatabase
from lib.nexus.pc.lb.main import PcLb
from lib.nexus.pc.state.main import PcState
from lib.nexus.pc.traffic.main import PcTraffic


class Pc(
        PcDatabase,
        PcLb,
        PcState,
        PcTraffic
        ):
    def __init__(self):
        PcDatabase.__init__(self)
        PcLb.__init__(self)
        PcState.__init__(self)
        PcTraffic.__init__(self)
