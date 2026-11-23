from lib.nexus.cdp.api import CdpApi
from lib.nexus.cdp.info import CdpInfo


class Cdp(
        CdpApi,
        CdpInfo
        ):
    def __init__(self):
        CdpApi.__init__(self)
        CdpInfo.__init__(self)
