from lib.aci.pg.access.intf.port.event.api import PolicyGroupAccessInterfacePortEventApi
from lib.aci.pg.access.intf.port.event.info import PolicyGroupAccessInterfacePortEventInfo


class PolicyGroupAccessInterfacePortEvent(PolicyGroupAccessInterfacePortEventApi, PolicyGroupAccessInterfacePortEventInfo):
    def __init__(self):
        PolicyGroupAccessInterfacePortEventApi.__init__(self)
        PolicyGroupAccessInterfacePortEventInfo.__init__(self)
