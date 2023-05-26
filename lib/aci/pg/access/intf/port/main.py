from lib.aci.pg.access.intf.port.api import PolicyGroupAccessInterfacePortApi
from lib.aci.pg.access.intf.port.info import PolicyGroupAccessInterfacePortInfo


class PolicyGroupAccessInterfacePort(PolicyGroupAccessInterfacePortApi, PolicyGroupAccessInterfacePortInfo):
    def __init__(self):
        PolicyGroupAccessInterfacePortApi.__init__(self)
        PolicyGroupAccessInterfacePortInfo.__init__(self)
