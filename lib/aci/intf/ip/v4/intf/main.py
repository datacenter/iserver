from lib.aci.intf.ip.v4.intf.api import InterfaceIpv4Api
from lib.aci.intf.ip.v4.intf.info import InterfaceIpv4Info


class InterfaceIpv4(InterfaceIpv4Api, InterfaceIpv4Info):
    def __init__(self):
        InterfaceIpv4Api.__init__(self)
        InterfaceIpv4Info.__init__(self)
