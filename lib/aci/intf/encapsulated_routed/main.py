from lib.aci.intf.encapsulated_routed.api import InterfaceEncapsulatedRoutedApi
from lib.aci.intf.encapsulated_routed.info import InterfaceEncapsulatedRoutedInfo
from lib.aci.intf.encapsulated_routed.audit.main import InterfaceEncapsulatedRoutedAudit
from lib.aci.intf.encapsulated_routed.event.main import InterfaceEncapsulatedRoutedEvent
from lib.aci.intf.encapsulated_routed.fault.main import InterfaceEncapsulatedRoutedFault


class InterfaceEncapsulatedRouted(
        InterfaceEncapsulatedRoutedApi,
        InterfaceEncapsulatedRoutedInfo,
        InterfaceEncapsulatedRoutedAudit,
        InterfaceEncapsulatedRoutedEvent,
        InterfaceEncapsulatedRoutedFault
        ):
    def __init__(self):
        InterfaceEncapsulatedRoutedApi.__init__(self)
        InterfaceEncapsulatedRoutedInfo.__init__(self)
        InterfaceEncapsulatedRoutedAudit.__init__(self)
        InterfaceEncapsulatedRoutedEvent.__init__(self)
        InterfaceEncapsulatedRoutedFault.__init__(self)
