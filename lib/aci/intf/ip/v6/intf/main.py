from lib.aci.intf.ip.v6.intf.api import InterfaceIpv6Api
from lib.aci.intf.ip.v6.intf.info import InterfaceIpv6Info


class InterfaceIpv6(InterfaceIpv6Api, InterfaceIpv6Info):
    def __init__(self):
        InterfaceIpv6Api.__init__(self)
        InterfaceIpv6Info.__init__(self)
