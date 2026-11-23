from lib.nexus.vpc.role.api import VpcRoleApi
from lib.nexus.vpc.role.info import VpcRoleInfo


class VpcRole(
        VpcRoleApi,
        VpcRoleInfo
        ):
    def __init__(self):
        VpcRoleApi.__init__(self)
        VpcRoleInfo.__init__(self)
