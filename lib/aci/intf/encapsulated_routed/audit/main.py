from lib.aci.intf.encapsulated_routed.audit.api import InterfaceEncapsulatedRoutedAuditApi
from lib.aci.intf.encapsulated_routed.audit.info import InterfaceEncapsulatedRoutedAuditInfo


class InterfaceEncapsulatedRoutedAudit(InterfaceEncapsulatedRoutedAuditApi, InterfaceEncapsulatedRoutedAuditInfo):
    def __init__(self):
        InterfaceEncapsulatedRoutedAuditApi.__init__(self)
        InterfaceEncapsulatedRoutedAuditInfo.__init__(self)
