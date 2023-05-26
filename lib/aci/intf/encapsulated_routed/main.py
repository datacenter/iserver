from lib.aci.intf.encapsulated_routed.api import InterfaceEncapsulatedRoutedApi
from lib.aci.intf.encapsulated_routed.info import InterfaceEncapsulatedRoutedInfo


class InterfaceEncapsulatedRouted(InterfaceEncapsulatedRoutedApi, InterfaceEncapsulatedRoutedInfo):
    def __init__(self):
        InterfaceEncapsulatedRoutedApi.__init__(self)
        InterfaceEncapsulatedRoutedInfo.__init__(self)
