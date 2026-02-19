from lib.nexus.vpc.keepalive.output import VpcKeepaliveOutput
from lib.nexus.vpc.role.output import VpcRoleOutput
from lib.nexus.vpc.state.output import VpcStateOutput

class VpcOutput(
        VpcKeepaliveOutput,
        VpcRoleOutput,
        VpcStateOutput
    ):
    def __init__(self):
        VpcKeepaliveOutput.__init__(self)
        VpcRoleOutput.__init__(self)
        VpcStateOutput.__init__(self)
