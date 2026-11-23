from lib.aci.l2out.event.api import L2OutEventApi
from lib.aci.l2out.event.info import L2OutEventInfo


class L2OutEvent(L2OutEventApi, L2OutEventInfo):
    def __init__(self):
        L2OutEventApi.__init__(self)
        L2OutEventInfo.__init__(self)
