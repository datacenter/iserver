from lib.aci.l3out.event.api import L3OutEventApi
from lib.aci.l3out.event.info import L3OutEventInfo


class L3OutEvent(L3OutEventApi, L3OutEventInfo):
    def __init__(self):
        L3OutEventApi.__init__(self)
        L3OutEventInfo.__init__(self)
