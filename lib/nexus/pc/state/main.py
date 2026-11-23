from lib.nexus.pc.state.api import PcStateApi
from lib.nexus.pc.state.info import PcStateInfo


class PcState(
        PcStateApi,
        PcStateInfo
        ):
    def __init__(self):
        PcStateApi.__init__(self)
        PcStateInfo.__init__(self)
