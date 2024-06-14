from lib.aci.intf.ip.v4.address.api import AddressIpv4Api
from lib.aci.intf.ip.v4.address.info import AddressIpv4Info


class AddressIpv4(AddressIpv4Api, AddressIpv4Info):
    def __init__(self):
        AddressIpv4Api.__init__(self)
        AddressIpv4Info.__init__(self)
