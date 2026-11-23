from lib.aci.vrf.event.api import VrfEventApi
from lib.aci.vrf.event.info import VrfEventInfo


class VrfEvent(VrfEventApi, VrfEventInfo):
    def __init__(self):
        VrfEventApi.__init__(self)
        VrfEventInfo.__init__(self)
