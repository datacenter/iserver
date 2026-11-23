from lib.osp.network.api import OspNetworkApi
from lib.osp.network.info import OspNetworkInfo


class OspNetwork(
        OspNetworkApi,
        OspNetworkInfo
        ):
    def __init__(self):
        OspNetworkApi.__init__(self)
        OspNetworkInfo.__init__(self)
