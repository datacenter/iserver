from lib.osp.router.api import OspRouterApi
from lib.osp.router.info import OspRouterInfo


class OspRouter(
        OspRouterApi,
        OspRouterInfo
        ):
    def __init__(self):
        OspRouterApi.__init__(self)
        OspRouterInfo.__init__(self)
