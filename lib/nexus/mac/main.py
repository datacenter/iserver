from lib.nexus.mac.api import MacApi
from lib.nexus.mac.info import MacInfo


class Mac(
        MacApi,
        MacInfo
        ):
    def __init__(self):
        MacApi.__init__(self)
        MacInfo.__init__(self)
