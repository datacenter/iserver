from lib.aci.vrf.fault.api import VrfFaultApi
from lib.aci.vrf.fault.info import VrfFaultInfo


class VrfFault(VrfFaultApi, VrfFaultInfo):
    def __init__(self):
        VrfFaultApi.__init__(self)
        VrfFaultInfo.__init__(self)
