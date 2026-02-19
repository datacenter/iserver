from lib.nexus.pc.database.output import PcDatabaseOutput
from lib.nexus.pc.lb.output import PcLbOutput
from lib.nexus.pc.state.output import PcStateOutput
from lib.nexus.pc.traffic.output import PcTrafficOutput

class PcOutput(
        PcDatabaseOutput,
        PcLbOutput,
        PcStateOutput,
        PcTrafficOutput
    ):
    def __init__(self):
        PcDatabaseOutput.__init__(self)
        PcLbOutput.__init__(self)
        PcStateOutput.__init__(self)
        PcTrafficOutput.__init__(self)
