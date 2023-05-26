from lib.aci.intf.lacp.instance.main import InterfaceLacpInstance
from lib.aci.intf.lacp.stats.main import InterfaceLacpStats
from lib.aci.intf.lacp.api import InterfaceLacpApi
from lib.aci.intf.lacp.info import InterfaceLacpInfo


class InterfaceLacp(InterfaceLacpInstance, InterfaceLacpStats, InterfaceLacpApi, InterfaceLacpInfo):
    def __init__(self):
        InterfaceLacpInstance.__init__(self)
        InterfaceLacpStats.__init__(self)
        InterfaceLacpApi.__init__(self)
        InterfaceLacpInfo.__init__(self)
