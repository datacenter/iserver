from lib.nexus.lldp.api import LldpApi
from lib.nexus.lldp.info import LldpInfo


class Lldp(
        LldpApi,
        LldpInfo
        ):
    def __init__(self):
        LldpApi.__init__(self)
        LldpInfo.__init__(self)
