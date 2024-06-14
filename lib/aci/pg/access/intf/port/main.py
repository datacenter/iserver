from lib.aci.pg.access.intf.port.api import PolicyGroupAccessInterfacePortApi
from lib.aci.pg.access.intf.port.info import PolicyGroupAccessInterfacePortInfo
from lib.aci.pg.access.intf.port.audit.main import PolicyGroupAccessInterfacePortAudit
from lib.aci.pg.access.intf.port.event.main import PolicyGroupAccessInterfacePortEvent
from lib.aci.pg.access.intf.port.fault.main import PolicyGroupAccessInterfacePortFault
from lib.aci.pg.access.intf.port.node.main import PolicyGroupAccessInterfacePortNode


class PolicyGroupAccessInterfacePort(
        PolicyGroupAccessInterfacePortApi,
        PolicyGroupAccessInterfacePortInfo,
        PolicyGroupAccessInterfacePortAudit,
        PolicyGroupAccessInterfacePortEvent,
        PolicyGroupAccessInterfacePortFault,
        PolicyGroupAccessInterfacePortNode
        ):
    def __init__(self):
        PolicyGroupAccessInterfacePortApi.__init__(self)
        PolicyGroupAccessInterfacePortInfo.__init__(self)
        PolicyGroupAccessInterfacePortAudit.__init__(self)
        PolicyGroupAccessInterfacePortEvent.__init__(self)
        PolicyGroupAccessInterfacePortFault.__init__(self)
        PolicyGroupAccessInterfacePortNode.__init__(self)
