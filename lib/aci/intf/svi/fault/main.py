from lib.aci.intf.svi.fault.api import InterfaceSviFaultApi
from lib.aci.intf.svi.fault.info import InterfaceSviFaultInfo


class InterfaceSviFault(InterfaceSviFaultApi, InterfaceSviFaultInfo):
    def __init__(self):
        InterfaceSviFaultApi.__init__(self)
        InterfaceSviFaultInfo.__init__(self)
