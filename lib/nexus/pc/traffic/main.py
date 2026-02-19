from lib.nexus.pc.traffic.api import PcTrafficApi
from lib.nexus.pc.traffic.info import PcTrafficInfo


class PcTraffic(
        PcTrafficApi,
        PcTrafficInfo
        ):
    def __init__(self):
        PcTrafficApi.__init__(self)
        PcTrafficInfo.__init__(self)
