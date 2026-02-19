from lib.nexus.vpc.keepalive.api import VpcKeepaliveApi
from lib.nexus.vpc.keepalive.info import VpcKeepaliveInfo


class VpcKeepalive(
        VpcKeepaliveApi,
        VpcKeepaliveInfo
        ):
    def __init__(self):
        VpcKeepaliveApi.__init__(self)
        VpcKeepaliveInfo.__init__(self)
