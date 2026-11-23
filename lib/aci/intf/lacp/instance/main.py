from lib.aci.intf.lacp.instance.api import InterfaceLacpInstanceApi
from lib.aci.intf.lacp.instance.info import InterfaceLacpInstanceInfo


class InterfaceLacpInstance(InterfaceLacpInstanceApi, InterfaceLacpInstanceInfo):
    def __init__(self):
        InterfaceLacpInstanceApi.__init__(self)
        InterfaceLacpInstanceInfo.__init__(self)
