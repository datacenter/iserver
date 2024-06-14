from lib.nexus.lacp.api import LacpApi
from lib.nexus.lacp.info import LacpInfo


class Lacp(
        LacpApi,
        LacpInfo
        ):
    def __init__(self):
        LacpApi.__init__(self)
        LacpInfo.__init__(self)
