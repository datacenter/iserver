from lib.osp.user.api import OspUserApi
from lib.osp.user.info import OspUserInfo


class OspUser(
        OspUserApi,
        OspUserInfo
        ):
    def __init__(self):
        OspUserApi.__init__(self)
        OspUserInfo.__init__(self)
