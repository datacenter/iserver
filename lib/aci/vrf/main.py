from lib.aci.vrf.api import VrfApi
from lib.aci.vrf.info import VrfInfo


class Vrf(VrfApi, VrfInfo):
    def __init__(self):
        VrfApi.__init__(self)
        VrfInfo.__init__(self)
