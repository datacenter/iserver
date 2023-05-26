from lib.aci.l2out.api import L2OutApi
from lib.aci.l2out.info import L2OutInfo


class L2Out(L2OutApi, L2OutInfo):
    def __init__(self):
        L2OutApi.__init__(self)
        L2OutInfo.__init__(self)
