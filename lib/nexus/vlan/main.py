from lib.nexus.vlan.api import VlanApi
from lib.nexus.vlan.info import VlanInfo


class Vlan(
        VlanApi,
        VlanInfo
        ):
    def __init__(self):
        VlanApi.__init__(self)
        VlanInfo.__init__(self)
