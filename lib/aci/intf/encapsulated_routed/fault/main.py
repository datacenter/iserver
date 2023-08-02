from lib.aci.intf.encapsulated_routed.fault.api import InterfaceEncapsulatedRoutedFaultApi
from lib.aci.intf.encapsulated_routed.fault.info import InterfaceEncapsulatedRoutedFaultInfo


class InterfaceEncapsulatedRoutedFault(InterfaceEncapsulatedRoutedFaultApi, InterfaceEncapsulatedRoutedFaultInfo):
    def __init__(self):
        InterfaceEncapsulatedRoutedFaultApi.__init__(self)
        InterfaceEncapsulatedRoutedFaultInfo.__init__(self)
