from lib.nexus.mon.api.api import MonApiApi
from lib.nexus.mon.api.info import MonApiInfo


class MonApi(
        MonApiApi,
        MonApiInfo
        ):
    def __init__(self):
        MonApiApi.__init__(self)
        MonApiInfo.__init__(self)
