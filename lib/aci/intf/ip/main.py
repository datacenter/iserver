from lib.aci.intf.ip.v4.address.main import AddressIpv4
from lib.aci.intf.ip.v4.intf.main import InterfaceIpv4
from lib.aci.intf.ip.v6.address.main import AddressIpv6
from lib.aci.intf.ip.v6.intf.main import InterfaceIpv6


class InterfaceIp(AddressIpv4, InterfaceIpv4, AddressIpv6, InterfaceIpv6):
    def __init__(self):
        AddressIpv4.__init__(self)
        InterfaceIpv4.__init__(self)
        AddressIpv6.__init__(self)
        InterfaceIpv6.__init__(self)
