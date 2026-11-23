from lib.nexus.vpc.keepalive.main import VpcKeepalive
from lib.nexus.vpc.role.main import VpcRole
from lib.nexus.vpc.state.main import VpcState


class Vpc(
        VpcKeepalive,
        VpcRole,
        VpcState
        ):
    def __init__(self):
        VpcKeepalive.__init__(self)
        VpcRole.__init__(self)
        VpcState.__init__(self)
