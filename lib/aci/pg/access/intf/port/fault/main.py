from lib.aci.pg.access.intf.port.fault.api import PolicyGroupAccessInterfacePortFaultApi
from lib.aci.pg.access.intf.port.fault.info import PolicyGroupAccessInterfacePortFaultInfo


class PolicyGroupAccessInterfacePortFault(PolicyGroupAccessInterfacePortFaultApi, PolicyGroupAccessInterfacePortFaultInfo):
    def __init__(self):
        PolicyGroupAccessInterfacePortFaultApi.__init__(self)
        PolicyGroupAccessInterfacePortFaultInfo.__init__(self)
