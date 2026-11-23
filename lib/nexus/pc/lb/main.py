from lib.nexus.pc.lb.api import PcLbApi
from lib.nexus.pc.lb.info import PcLbInfo


class PcLb(
        PcLbApi,
        PcLbInfo
        ):
    def __init__(self):
        PcLbApi.__init__(self)
        PcLbInfo.__init__(self)
