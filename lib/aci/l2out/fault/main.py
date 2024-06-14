from lib.aci.l2out.fault.api import L2OutFaultApi
from lib.aci.l2out.fault.info import L2OutFaultInfo


class L2OutFault(L2OutFaultApi, L2OutFaultInfo):
    def __init__(self):
        L2OutFaultApi.__init__(self)
        L2OutFaultInfo.__init__(self)
