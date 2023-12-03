from lib.osp.role.api import OspRoleApi
from lib.osp.role.info import OspRoleInfo


class OspRole(
        OspRoleApi,
        OspRoleInfo
        ):
    def __init__(self):
        OspRoleApi.__init__(self)
        OspRoleInfo.__init__(self)
