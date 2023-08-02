from lib.aci.bd.fault.api import BridgeDomainFaultApi
from lib.aci.bd.fault.info import BridgeDomainFaultInfo


class BridgeDomainFault(BridgeDomainFaultApi, BridgeDomainFaultInfo):
    def __init__(self):
        BridgeDomainFaultApi.__init__(self)
        BridgeDomainFaultInfo.__init__(self)
