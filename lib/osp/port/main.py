from lib.osp.port.api import OspPortApi
from lib.osp.port.info import OspPortInfo


class OspPort(
        OspPortApi,
        OspPortInfo
        ):
    def __init__(self):
        OspPortApi.__init__(self)
        OspPortInfo.__init__(self)
