from lib.aci.intf.virtual_port_channel.audit.api import InterfaceVirtualPortChannelAuditApi
from lib.aci.intf.virtual_port_channel.audit.info import InterfaceVirtualPortChannelAuditInfo


class InterfaceVirtualPortChannelAudit(InterfaceVirtualPortChannelAuditApi, InterfaceVirtualPortChannelAuditInfo):
    def __init__(self):
        InterfaceVirtualPortChannelAuditApi.__init__(self)
        InterfaceVirtualPortChannelAuditInfo.__init__(self)
