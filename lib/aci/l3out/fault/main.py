from lib.aci.l3out.fault.api import L3OutFaultApi
from lib.aci.l3out.fault.info import L3OutFaultInfo


class L3OutFault(L3OutFaultApi, L3OutFaultInfo):
    def __init__(self):
        L3OutFaultApi.__init__(self)
        L3OutFaultInfo.__init__(self)
