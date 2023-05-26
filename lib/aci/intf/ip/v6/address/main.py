from lib.aci.intf.ip.v6.address.api import AddressIpv6Api
from lib.aci.intf.ip.v6.address.info import AddressIpv6Info


class AddressIpv6(AddressIpv6Api, AddressIpv6Info):
    def __init__(self):
        AddressIpv6Api.__init__(self)
        AddressIpv6Info.__init__(self)
