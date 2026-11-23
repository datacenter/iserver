from lib.nexus.vrf.api import VrfApi
from lib.nexus.vrf.info import VrfInfo


class Vrf(
        VrfApi,
        VrfInfo
        ):
    def __init__(self):
        VrfApi.__init__(self)
        VrfInfo.__init__(self)
