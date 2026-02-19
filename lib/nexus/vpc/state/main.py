from lib.nexus.vpc.state.api import VpcStateApi
from lib.nexus.vpc.state.info import VpcStateInfo


class VpcState(
        VpcStateApi,
        VpcStateInfo
        ):
    def __init__(self):
        VpcStateApi.__init__(self)
        VpcStateInfo.__init__(self)
