from lib.aci.intf.encapsulated_routed.event.api import InterfaceEncapsulatedRoutedEventApi
from lib.aci.intf.encapsulated_routed.event.info import InterfaceEncapsulatedRoutedEventInfo


class InterfaceEncapsulatedRoutedEvent(InterfaceEncapsulatedRoutedEventApi, InterfaceEncapsulatedRoutedEventInfo):
    def __init__(self):
        InterfaceEncapsulatedRoutedEventApi.__init__(self)
        InterfaceEncapsulatedRoutedEventInfo.__init__(self)
